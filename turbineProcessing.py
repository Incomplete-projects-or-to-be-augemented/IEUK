import pandas as pd

df = pd.read_csv('telemetry_data(in).csv')

avg_temp = df.groupby("turbine_id")["temperature_c"].mean()
max_vib = df.groupby("turbine_id")["vibration_mm_s"].max()

result = pd.DataFrame({
    "avg_temp": avg_temp,
    "max_vibration": max_vib
})

anomalies = result.index[
    (result["avg_temp"] > 85.0) &
    (result["max_vibration"] > 15.0)
].tolist()
print(result)
print("Turbines failing anomaly rules:")
print(anomalies)


