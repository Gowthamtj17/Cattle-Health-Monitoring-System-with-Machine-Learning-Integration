import pandas as pd
import random
from datetime import datetime, timedelta

def get_activity_status(x, y, z):
    """Generate activity status based on MPU6050 sensor data."""
    if x < 0.2 and y < 0.2 and z < 0.2:
        return "Lying"
    elif x > 0.2 or y > 0.2 or z > 0.2:
        return "Standing"
    else:
        return "Sitting"

def simulate_heart_rate():
    """Simulate heart rate readings in BPM."""
    return random.randint(50, 100)  

def simulate_activity_data():
    """Simulate activity data from MPU6050 sensor."""
    activity_x = round(random.uniform(-1.0, 1.0), 2) 
    activity_y = round(random.uniform(-1.0, 1.0), 2)
    activity_z = round(random.uniform(-1.0, 1.0), 2)
    status = get_activity_status(activity_x, activity_y, activity_z)
    return activity_x, activity_y, activity_z, status

def simulate_skin_temp():
    """Simulate skin temperature readings."""
    return round(random.uniform(36.5, 41.0), 1)  

def simulate_sleep_tracking(heart_rate, activity_status):
    """Simulate sleep tracking data."""
    return "Sleeping" if activity_status == "Lying" and heart_rate < 60 else "Awake"

def determine_health_status(heart_rate, skin_temp, activity_status):
    """Determine the health status based on various parameters."""
    if (48 <= heart_rate <= 84) and (33.5 <= skin_temp <= 39.5) and (activity_status != "Lying"):
        return "Healthy"
    else:
        return "Unhealthy"

# Generate simulated data
data = []
start_time = datetime(2024, 8, 14, 6, 0)

for i in range(250):
    timestamp = start_time + timedelta(minutes=i * 5)
    
    heart_rate = simulate_heart_rate()
    activity_x, activity_y, activity_z, activity_status = simulate_activity_data()
    
    skin_temp = simulate_skin_temp()
    
    sleep_status = simulate_sleep_tracking(heart_rate, activity_status)
    
    health_status = determine_health_status(heart_rate, skin_temp, activity_status)
    
    row = {
        "Timestamp": timestamp,
        "HeartRate_BPM": heart_rate,
        "Activity_X": activity_x,
        "Activity_Y": activity_y,
        "Activity_Z": activity_z,
        "Activity_Status": activity_status,
        "SkinTemp_Celsius": skin_temp,
        "Sleep_Status": sleep_status,
        "Health_Status": health_status
    }
    
    data.append(row)

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("backend/ML/cattle_health_monitoring.csv", index=False)

print("Simulated dataset created successfully!")