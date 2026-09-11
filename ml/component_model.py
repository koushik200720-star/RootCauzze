def predict_faulty_component(df):

    temperature = df["temperature_C"].mean() \
        if "temperature_C" in df.columns else 0

    vibration = df["vibration_mm_s"].mean() \
        if "vibration_mm_s" in df.columns else 0

    lubrication = df["lubrication_level_pct"].mean() \
        if "lubrication_level_pct" in df.columns else 100

    pressure = df["pressure_bar"].mean() \
        if "pressure_bar" in df.columns else 5

    if lubrication < 50:
        return "Lubrication System"

    if vibration > 5:
        return "Bearing Assembly"

    if temperature > 85:
        return "Cooling System"

    if pressure < 3 or pressure > 8:
        return "Pressure / Hydraulic System"

    return "None"
