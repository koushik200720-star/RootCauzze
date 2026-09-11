def predict_failure_type(df):

    temperature = df["temperature_C"].mean() \
        if "temperature_C" in df.columns else 0

    vibration = df["vibration_mm_s"].mean() \
        if "vibration_mm_s" in df.columns else 0

    pressure = df["pressure_bar"].mean() \
        if "pressure_bar" in df.columns else 0

    current = df["current_A"].mean() \
        if "current_A" in df.columns else 0

    lubrication = df["lubrication_level_pct"].mean() \
        if "lubrication_level_pct" in df.columns else 100

    if lubrication < 50:
        return "Lubrication Failure"

    if vibration > 5:
        return "Vibration Failure"

    if temperature > 85:
        return "Overheating Failure"

    if pressure < 3 or pressure > 8:
        return "Pressure Failure"

    if current > 15:
        return "Electrical Failure"

    return "No Failure"
