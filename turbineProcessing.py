import pandas as pd
# Loads the CSV file
df = pd.read_csv('telemetry_data_in.csv')
# Averages the temperature of the results in each group after being grouped by ID
avg_temp = df.groupby("turbine_id")["temperature_c"].mean()
# Finds the maximum vibration of the results in each group after being grouped by ID
max_vib = df.groupby("turbine_id")["vibration_mm_s"].max()

# For each turbineID crafts a pandas Dataframe with fields for average temperature and maximum vibration
result = pd.DataFrame({
    "avg_temp": avg_temp,
    "max_vibration": max_vib
})

# Creates a list of the turbine IDs that are anomalies
anomalies = result.index[
    (result["avg_temp"] > 85.0) |
    (result["max_vibration"] > 15.0)
].tolist()

# Prints the anomaly IDs
print("Turbines failing anomaly rules:")
print(anomalies)


