import os

import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def calc_mean_erp(
    trial_points=None, ecog_data=None, trial_points_file=None, ecog_data_file=None
):
    """
    Calculate the mean ERP for each finger based on trial points and ECoG data.
    The function accepts either raw data or file paths to load the data.

    Args:
        trial_points (pd.DataFrame): DataFrame containing "start", "peak", and "finger" columns.
        ecog_data (np.ndarray): 1D numpy array of ECoG signals.
        trial_points_file (str): Path to CSV file containing trial points.
        ecog_data_file (str): Path to CSV file containing ECoG data.

    Returns:
        np.ndarray: A 5x1201 matrix containing the averaged ERP for each finger.
    """

    if trial_points_file:
        if not os.path.exists(trial_points_file):
            raise FileNotFoundError(f"File not found: {trial_points_file}")
        trial_points = pd.read_csv(
            trial_points_file, header=None, names=["start", "peak", "finger"]
        )
    if ecog_data_file:
        if not os.path.exists(ecog_data_file):
            raise FileNotFoundError(f"File not found: {ecog_data_file}")
        ecog_data = pd.read_csv(ecog_data_file, header=None).iloc[:, 0].values

    if trial_points is None or ecog_data is None:
        raise ValueError(
            "Either trial_points and ecog_data, or their file paths, must be provided."
        )

    trial_points = trial_points.astype({"start": int, "peak": int, "finger": int})
    finger_signals = {finger: [] for finger in range(1, 6)}
    skipped_trials = 0

    for _, row in trial_points.iterrows():
        start_idx = row["start"]
        finger = row["finger"]
        block_start = start_idx - 200
        block_end = start_idx + 1000
        if block_start >= 0 and block_end < len(ecog_data):
            block = ecog_data[block_start : block_end + 1]
            finger_signals[finger].append(block)
        else:
            skipped_trials += 1

    if skipped_trials > 0:
        print(f"Skipped {skipped_trials} trials due to out-of-bounds time windows.")

    fingers_erp_mean = []
    time_points = np.linspace(-200, 1000, 1201)
    for finger in range(1, 6):
        if finger_signals[finger]:
            finger_mean = np.mean(finger_signals[finger], axis=0)
        else:
            finger_mean = np.zeros(1201)
        fingers_erp_mean.append(finger_mean)
        plt.plot(time_points, finger_mean, label=f"Finger {finger}")

    plt.title("Averaged ERP for Each Finger")
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.grid(True)

    output_file = "output_graph.png"
    plt.savefig(output_file)
    print(f"Graph saved as '{output_file}'")
    os.startfile(output_file)

    fingers_erp_mean = np.array(fingers_erp_mean)
    output_csv = "fingers_erp_mean_output.csv"
    pd.DataFrame(fingers_erp_mean).to_csv(output_csv, index=False, header=False)
    print(f"ERP matrix saved to {output_csv}")

    return fingers_erp_mean


if __name__ == "__main__":
    trial_points_file = "events_file_ordered.csv"
    ecog_data_file = "brain_data_channel_one.csv"

    erp_matrix = calc_mean_erp(
        trial_points_file=trial_points_file, ecog_data_file=ecog_data_file
    )
    print("Shape of the ERP matrix:", erp_matrix.shape)
    print("ERP matrix:\n", erp_matrix)
