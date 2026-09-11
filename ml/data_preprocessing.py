import pandas as pd
import numpy as np


def load_and_clean_data(file):
    """
    Load and clean the uploaded CSV file.
    """

    df = pd.read_csv(file)

    # Remove completely empty rows
    df = df.dropna(how="all")

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Convert timestamp if available
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(
            df["timestamp"],
            errors="coerce"
        )

    # Fill numerical missing values with median
    numerical_columns = df.select_dtypes(
        include=np.number
    ).columns

    for column in numerical_columns:
        df[column] = df[column].fillna(
            df[column].median()
        )

    # Fill categorical missing values
    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns

    for column in categorical_columns:
        if not df[column].mode().empty:
            df[column] = df[column].fillna(
                df[column].mode()[0]
            )

    return df


def get_data_quality_report(df):
    """
    Generate a basic data quality report.
    """

    report = {
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum())
    }

    return report
