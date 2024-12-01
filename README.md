## README.MD: Data Analysis Script for Tapanuli Tengah (Tapteng) 2023

This script analyzes data related to Tapanuli Tengah Regency (Tapteng) in 2023. It focuses on exploring the relationship between the area (luas wilayah) of each kecamatan (district) and the number of villages (jumlah desa).

**Requirements:**

* Python 3.x
* pandas library
* seaborn library
* matplotlib library

**Data Files:**

* `data/tapteng-2023-jumlah-desa.csv`: This file is assumed to contain data on the number of villages per kecamatan.
* `data/tapteng-2023-luas-kecamatan.csv`: This file is assumed to contain data on the area of each kecamatan.

**Script Functionality:**

1. **Data Loading and Cleaning:**
    * The script reads data from the specified CSV files using pandas.
    * It merges the dataframes based on a common column (likely "Kecamatan") if they are separate files.
    * The `clean_data` function removes rows with missing values (NaN).

2. **Data Exploration:**
    * The script creates two visualizations:
        * **Scatter Plot:** This plot visualizes the relationship between the area and number of villages for each kecamatan.
        * **Normal Distribution Plots:** These plots show the distribution of area and number of villages across all kecamatans.

3. **Output:**
    * The script displays the column names of the cleaned data (`data.columns`).
    * It then generates and displays the scatter plot and normal distribution plots.

**Running the Script:**

1. Ensure you have the required libraries installed (`pandas`, `seaborn`, `matplotlib`).
2. Place the script and data files in the same directory.
3. Run the script from the command line using `python your_script.py`.

**Customization:**

* You can modify the script to include additional data analysis tasks or visualizations.
* Update the file paths (`DATA_DIR`, `JUMLAH_DESA`, `LUAS_WILAYAH`) to reflect the actual location of your data files.

**Note:**

* This script assumes a basic understanding of Python and data analysis with pandas and seaborn.

I hope this README provides a clear overview of the script's functionality and how to use it for analyzing data related to Tapanuli Tengah.
