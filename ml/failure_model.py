import pandas as pd


def detect_failure(df):
    """
    Basic failure detection.
    This will later be replaced/connected
    to the trained ML model.
    """

    sensor_columns = [
        "temperature_C",
        "vibration_mm_s",
        "pressure_bar",
        "current_A",
        "rpm"
    ]

    available_columns = [
        column for column in sensor_columns
        if column in df.columns
    ]

    if not available_columns:
        return {
            "status": "Unknown",
            "failure_probability": 0
        }

    abnormal_score = 0

    if "temperature_C" in df.columns:
        if df["temperature_C"].mean() > 80:
            abnormal_score += 1

    if "vibration_mm_s" in df.columns:
        if df["vibration_mm_s"].mean() > 5:
            abnormal_score += 1

    if "rpm" in df.columns:
        if df["rpm"].std() > 100:
            abnormal_score += 1

    probability = min(
        95,
        abnormal_score * 25
    )

    status = (
        "Abnormal"
        if probability >= 50
        else "Normal"
    )

    return {
        "status": status,
        "failure_probability": probability
    }
