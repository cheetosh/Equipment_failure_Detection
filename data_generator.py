import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)

# Generate data for 10 devices over 100 days (every 6 hours)
timestamps = [datetime(2024, 1, 1) + timedelta(hours=6*i) for i in range(400)]
devices = [f"D{str(i).zfill(2)}" for i in range(1, 11)]

rows = []
for device in devices:
    base_temp = np.random.randint(60, 90)
    base_vib = np.random.uniform(0.2, 0.5)
    base_press = np.random.randint(25, 35)
    base_rpm = np.random.randint(1300, 1600)
    hours = np.random.randint(500, 1000)

    for ts in timestamps:
        temp = base_temp + np.random.normal(0, 10)
        vib = base_vib + np.random.normal(0, 0.1)
        press = base_press + np.random.normal(0, 5)
        rpm = base_rpm + np.random.normal(0, 50)
        hours += np.random.randint(1, 5)
        
        # Simulate failure probability (higher with high vibration/temp)
        fail_prob = (vib > 0.55 or temp > 100)
        failure = 1 if random.random() < 0.03 or fail_prob else 0
        
        rows.append([ts, device, temp, vib, press, rpm, hours, failure])

df = pd.DataFrame(rows, columns=[
    'timestamp', 'device_id', 'temp_c', 'vibration_g',
    'pressure_psi', 'rpm', 'hours_running', 'failure_next_7d'
])

df.to_csv('equipment_data.csv', index=False)
print("✅ Generated synthetic equipment_data.csv with", len(df), "rows")
print(df.head())
