import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Define file paths with descriptive variable names
DATA_DIR = "data"  # Assuming data files are in a folder named "data"
JUMLAH_DESA = "tapteng-2023-jumlah-desa.csv"
LUAS_WILAYAH = "tapteng-2023-luas-kecamatan.csv"


def load_data():
    """
    Reads and merges pagu and realisasi dataframes.

    Returns:
        pd.DataFrame: Merged dataframe containing pagu and realisasi data.
    """

    jumlah_desa_df = pd.read_csv(f"{DATA_DIR}/{JUMLAH_DESA}",)
    luas_wilayah_df = pd.read_csv(f"{DATA_DIR}/{LUAS_WILAYAH}", )

    merged_df = jumlah_desa_df.merge(luas_wilayah_df, on=["Kecamatan",])

    return merged_df


def clean_data(df):
    """
    Drops rows with missing values (NaN).

    Args:
        df (pd.DataFrame): Dataframe to clean.

    Returns:
        pd.DataFrame: Cleaned dataframe with missing values removed.
    """

    return df.dropna()



def plot_scatter(df, x_col, y_col):
    """
    Creates a scatter plot of two columns from the dataframe.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        x_col (str): Name of the column for the x-axis.
        y_col (str): Name of the column for the y-axis.
    """

    sns.scatterplot(x=x_col, y=y_col, data=df, alpha=0.7)
    plt.xlabel(f"{x_col.title()}")
    plt.ylabel(f"{y_col.title()}")
    plt.title(f"Scatter Plot of {x_col.title()} vs. {y_col.title()}")
    plt.show()


def plot_normal_distribution(df, col):
    """
    Creates a histogram with a normal distribution curve for a specific column.

    Args:
        df (pd.DataFrame): Dataframe containing the data.
        col (str): Name of the column to analyze.
    """

    plt.figure(figsize=(8, 6))
    sns.histplot(df[col], kde=True, color="blue", bins=30, stat="density", linewidth=0)
    plt.title(f"Normal Distribution of {col.title()}", fontsize=16)
    plt.xlabel(f"{col.title()}", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    data = load_data()
    data = clean_data(data)
    print(data.columns)

    plot_scatter(data, "Luas Wilayah", "Jumlah Desa")
    plot_normal_distribution(data, "Luas Wilayah")
    plot_normal_distribution(data, "Jumlah Desa")