def discover_root_cause(df):

    evidence = []

    lubrication = df["lubrication_level_pct"].mean() \
        if "lubrication_level_pct" in df.columns else 100

    vibration = df["vibration_mm_s"].mean() \
        if "vibration_mm_s" in df.columns else 0

    temperature = df["temperature_C"].mean() \
        if "temperature_C" in df.columns else 0

    pressure = df["pressure_bar"].mean() \
        if "pressure_bar" in df.columns else 5

    if lubrication < 50:
        evidence.append(
            "Low lubrication level detected"
        )

        if vibration > 5:
            evidence.append(
                "High vibration supports bearing friction"
            )

        if temperature > 80:
            evidence.append(
                "High temperature supports increased friction"
            )

        return {
            "root_cause": "Low Lubrication",
            "confidence": 87,
            "evidence": evidence,
            "recommendation":
                "Restore lubrication and inspect bearing assembly"
        }

    if vibration > 5:
        return {
            "root_cause": "Bearing Degradation",
            "confidence": 82,
            "evidence": [
                "Excessive vibration detected"
            ],
            "recommendation":
                "Inspect bearing assembly"
        }

    if temperature > 85:
        return {
            "root_cause": "Overheating",
            "confidence": 80,
            "evidence": [
                "Temperature exceeds safe operating range"
            ],
            "recommendation":
                "Inspect cooling system"
        }

    if pressure < 3 or pressure > 8:
        return {
            "root_cause": "Pressure Instability",
            "confidence": 78,
            "evidence": [
                "Abnormal pressure detected"
            ],
            "recommendation":
                "Inspect pressure and hydraulic system"
        }

    return {
        "root_cause": "Normal Operation",
        "confidence": 90,
        "evidence": [
            "Sensor values are within expected ranges"
        ],
        "recommendation":
            "Continue normal monitoring"
    }
