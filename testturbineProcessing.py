import pandas as pd

df = pd.read_csv('mock_telemetry_data.csv')

avg_temp = df.groupby("turbine_id")["temperature"].mean()
max_vib = df.groupby("turbine_id")["vibration"].max()

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


