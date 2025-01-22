### **README: ECoG Data ERP Analysis**

## **Project Overview**
This project analyzes ECoG (Electrocorticography) data to compute the **Event-Related Potential (ERP)** for different trials associated with specific finger movements. The analysis involves aligning brain activity data with movement events, calculating the average ERP for each finger, and visualizing the results.

---

## **Project Structure**

| **File Name**               | **Description**                                                                                 |
|-----------------------------|---------------------------------------------------------------------------------------------|
| `brain_data_channel_one.csv` | Contains the ECoG brain activity data recorded as a time series from a single electrode.      |
| `events_file_ordered.csv`    | Lists trial events with the start time, peak time, and associated finger for each movement.   |
| `fingers_erp_mean_output.csv` | The output file containing the averaged ERP matrix for each finger.                          |
| `Main.ipynb`                 | The main Jupyter Notebook that processes the data, computes the ERP, generates visualizations, and saves results. |
| `finger_data.csv`            | (Optional or additional) Could represent auxiliary data related to finger movement analysis.  |

---

## **How It Works**
1. **Input Files:**
   - **`events_file_ordered.csv`**:
     - Contains details of movement trials.
     - Columns:
       - `Start`: Start time of the trial (index in the time series).
       - `Peak`: Peak time of the movement.
       - `Finger`: Finger identifier (1 to 5).
   - **`brain_data_channel_one.csv`**:
     - Contains the ECoG signals as a single-column time series.

2. **Output File:**
   - **`fingers_erp_mean_output.csv`**:
     - The ERP matrix (5 rows x 1201 columns) representing the averaged brain activity for each finger across trials.

3. **Main Notebook (`Main.ipynb`):**
   - Processes the input files to extract relevant signal windows for each trial.
   - Aligns and averages the ECoG signals to compute the ERP for each finger.
   - Visualizes the ERP results using Matplotlib.
   - Saves the ERP matrix in CSV format for further analysis.

---

## **How to Run**
### **Prerequisites**
- Install the required Python libraries:
  ```bash
  pip install numpy pandas matplotlib
  ```

### **Steps**
1. Place the input files (`brain_data_channel_one.csv` and `events_file_ordered.csv`) in the same directory as `Main.ipynb`.
2. Open the notebook in Jupyter:
   ```bash
   jupyter notebook Main.ipynb
   ```
3. Run the cells step by step or all at once.

### **Output**
- A graph showing the averaged ERP for each finger.
- A CSV file (`fingers_erp_mean_output.csv`) containing the ERP matrix.

---

## **ERP Matrix Details**
- The matrix is 5x1201:
  - **5 rows:** One for each finger (Finger 1 to Finger 5).
  - **1201 columns:** Time points from -200ms to +1000ms relative to the trial start.
- Each cell represents the averaged brain activity at a specific time point for a specific finger.

---

## **Project Author**
- **Prepared by:** Shahar Pal
- **Email:** [shaharpal9@gmail.com]
- **Date:** January 2025
- **Field:** Neuro-data Analysis

