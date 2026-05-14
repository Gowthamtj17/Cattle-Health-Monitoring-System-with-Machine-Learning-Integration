import firebase_admin
from firebase_admin import credentials, db
import random
from datetime import datetime, timedelta

# Step 1: Initialize Firebase app
cred = credentials.Certificate("backend/FireBase_Folder/credentials.json")

try:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://cattle-health-monitoring-ai-default-rtdb.asia-southeast1.firebasedatabase.app/'
    })
except ValueError:
    print("Firebase app already initialized.")

def simulate_heart_rate():
    """Simulate heart rate readings in BPM."""
    return random.randint(35, 98)

def simulate_activity_data():
    """Simulate activity data from MPU6050 sensor."""
    activity_x = round(random.uniform(-0.5, 0.25), 2)
    activity_y = round(random.uniform(-0.5, 0.25), 2)
    activity_z = round(random.uniform(-0.2, 0.2), 2)
    return activity_x, activity_y, activity_z

def simulate_skin_temp():
    """Simulate skin temperature readings."""
    return round(random.uniform(32.0, 40.5), 1)

def generate_test_data(num_samples=150):
    """Generate a simulated dataset and push it to Firebase."""
    start_time = datetime(2024, 8, 15, 6, 0)
    
    ref = db.reference('cattle_health_monitoring')  
    
    for i in range(num_samples):
        timestamp = start_time + timedelta(minutes=i * 5)
        heart_rate = simulate_heart_rate()
        activity_x, activity_y, activity_z = simulate_activity_data()
        skin_temp = simulate_skin_temp()
        
        # Data to be pushed to Firebase
        data = {
            "Timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "HeartRate_BPM": heart_rate,
            "Activity_X": activity_x,
            "Activity_Y": activity_y,
            "Activity_Z": activity_z,
            "SkinTemp_Celsius": skin_temp,
        }
        
        # Check if the data for this timestamp already exists
        existing_data_ref = db.reference('cattle_health_monitoring')
        existing_data = existing_data_ref.order_by_child('Timestamp').equal_to(data['Timestamp']).get()

        if existing_data:
            print(f"Data for Timestamp {data['Timestamp']} already exists, skipping push.")
            continue
        
        # Push the data to Firebase
        ref.push(data)
        print(f"Data pushed for timestamp: {data['Timestamp']}")

    print("All data has been uploaded successfully!")

# Generate and push the test dataset to Firebase
generate_test_data(250)
