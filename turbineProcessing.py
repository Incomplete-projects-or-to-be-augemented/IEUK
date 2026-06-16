import pandas as pd

df = pd.read_csv('mock_telemetry_data.csv')

tooHot = df[df["temperature"] > 85.0]
hotandShaky = tooHot[tooHot["vibration"] > 15.0]

failed = hotandShaky["turbine_id"].drop_duplicates()
print(f"{len(failed)} turbine IDs that failed the anomaly rules:")
print(failed.to_string(index=False))


