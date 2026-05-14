def predict_disease(features):
    diseases = []
    
    # Predict Bovine Respiratory Disease (BRD)
    if features['HeartRate_BPM'] > 85 and features['SkinTemp_Celsius'] > 39.0 and low_activity(features):
        diseases.append('Bovine Respiratory Disease (BRD)')
        
    # Predict Mastitis
    if localized_temp_rise(features) and moderate_heart_rate(features):
        diseases.append('Mastitis')
        
    # Predict Heat Stress
    if features['SkinTemp_Celsius'] > 40.0 and features['HeartRate_BPM'] > 90 and low_activity(features):
        diseases.append('Heat Stress')
        
    # Predict Foot and Mouth Disease (FMD)
    if features['HeartRate_BPM'] > 90 and features['SkinTemp_Celsius'] > 39.5 and very_low_activity(features):
        diseases.append('Foot and Mouth Disease (FMD)')
        
    # Additional diseases based on research findings
    if features['SkinTemp_Celsius'] > 39.5 and features['HeartRate_BPM'] < 60:
        diseases.append('Ketosis')
        
    if low_activity(features):
        diseases.append('Lameness')
        
    # If no specific disease is detected
    if not diseases:
        diseases.append('No specific disease detected')
    
    return diseases

def low_activity(features):
    return features['Activity_X'] < 0.1 and features['Activity_Y'] < 0.1

def very_low_activity(features):
    return features['Activity_X'] < 0.05 and features['Activity_Y'] < 0.05

def localized_temp_rise(features):
    return features['SkinTemp_Celsius'] > 38.5

def moderate_heart_rate(features):
    return 70 < features['HeartRate_BPM'] < 85

def determine_behavior(test_case):
    if test_case['Activity_X'] < 1 and test_case['Activity_Y'] < 1 and test_case['Activity_Z'] < 1:
        return 'Sleeping'
    elif test_case['Activity_X'] > 2:
        return 'Standing'
    else:
        return 'Sitting'