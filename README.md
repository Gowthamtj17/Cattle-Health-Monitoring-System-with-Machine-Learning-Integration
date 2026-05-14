# 🐄 Cattle Health Monitoring System with Machine Learning Integration

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/XGBoost-ML-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Firebase-Database-yellow?style=for-the-badge&logo=firebase" />
  <img src="https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-green?style=for-the-badge&logo=html5" />
</p>

> An intelligent, real-time cattle health monitoring system that leverages simulated IoT sensor data and machine learning (XGBoost) to predict early-stage cattle diseases — displayed through a responsive, multilingual web dashboard.

---

## 📌 Table of Contents

- [Problem Statement](#-problem-statement)
- [Project Solution](#-project-solution)
- [Impact](#-impact)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Machine Learning Model](#-machine-learning-model)
- [Dashboard Overview](#-dashboard-overview)
- [Diseases Covered](#-diseases-covered)
- [Future Enhancements](#-future-enhancements)
- [Contributing](#-contributing)

---

## ❗ Problem Statement

Livestock farming, particularly cattle rearing, is a cornerstone of agricultural economies worldwide. However, cattle health management remains one of the most reactive, labor-intensive, and high-risk challenges faced by farmers — especially smallholder and rural farmers in developing regions.

**Key challenges include:**

- **Late disease detection:** Farmers typically identify cattle illness only after visible symptoms appear, by which point the disease has already progressed significantly, reducing treatment effectiveness.
- **High economic losses:** Undetected diseases such as Mastitis, Bovine Respiratory Disease (BRD), and Foot-and-Mouth Disease (FMD) lead to reduced milk/meat production, veterinary costs, and cattle mortality.
- **Lack of continuous monitoring:** Manual health checks are infrequent, inconsistent, and unable to capture the subtle early physiological changes that precede disease onset.
- **Limited access to veterinary expertise:** Rural farmers often lack timely access to veterinarians, delaying diagnosis and treatment.
- **No data-driven decision making:** Health records are rarely digitized, making it impossible to identify patterns or predict outbreaks before they spread through a herd.

There is a critical need for an **affordable, automated, and intelligent system** that can continuously monitor cattle health indicators and provide early warnings to farmers.

---

## ✅ Project Solution

The **Cattle Health Monitoring System** addresses these challenges through a full-stack, data-driven approach combining simulated IoT sensor data, machine learning, and a user-friendly multilingual web dashboard.

### How It Works

1. **Data Simulation (IoT Layer):** Simulated sensor data mimics real-world IoT cattle health devices, capturing key biometric and behavioral indicators including:
   - Skin Temperature (°C)
   - Heart Rate (BPM)
   - Behavioral State (e.g., Sleeping, Active, Grazing)
   - Activity Level indicators (Low, Very Low)
   - Localized Temperature Rise flags

2. **Machine Learning Prediction (Backend):** An **XGBoost classifier** trained on cattle health datasets analyzes the incoming sensor readings to:
   - Classify the cattle's overall health status (Healthy / Unhealthy)
   - Predict specific diseases the cattle may be developing (e.g., Mastitis, Heat Stress, BRD)
   - Generate detailed health flags for nuanced risk assessment

3. **Data Storage (Firebase):** All health readings, predictions, and timestamps are stored in **Firebase Realtime Database**, enabling persistent, cloud-based health record management accessible from anywhere.

4. **Multilingual Web Dashboard (Frontend):** A clean, card-based HTML/CSS/JavaScript dashboard presents health data in real time:
   - **Login / Sign Up / Forgot Password** pages for secure user authentication
   - **Home page** displaying current cattle health metrics and ML predictions
   - **Detailed Health Panel** with granular flags (activity levels, temperature rise, heart rate status)
   - **Information Page** providing reference material on common cattle diseases with links to trusted sources
   - **Google Translate integration** for multilingual accessibility

---

## 🌍 Impact

### For Farmers
- **Early disease intervention** — detecting conditions like Mastitis days before visible symptoms, enabling timely veterinary treatment and reducing severity.
- **Reduced economic losses** — early detection prevents production drops (milk yield, weight gain) and expensive late-stage treatments.
- **Empowered decision-making** — farmers receive actionable, data-backed health alerts in their own language, reducing dependence on infrequent vet visits.

### For the Agricultural Sector
- **Scalable herd monitoring** — the system architecture can scale to monitor multiple cattle simultaneously, making it viable for large farms.
- **Digital health records** — Firebase-backed timestamped records enable trend analysis, herd-level health tracking, and data sharing with veterinarians.
- **Improved animal welfare** — continuous monitoring ensures cattle distress is detected and addressed promptly.

### For Society
- **Food security** — healthier cattle translates to more consistent milk and meat production, supporting food supply chains.
- **Rural technology access** — multilingual support and a simple UI lower the barrier to entry for non-technical, rural users.
- **Research potential** — anonymized health data can contribute to broader livestock disease research and AI model improvement.

### Measured Outcomes
- Improved disease prediction accuracy using XGBoost over baseline classifiers
- Reduced time-to-detection for early-stage cattle diseases
- Multi-language support enabling accessibility for diverse farming communities

---

## ✨ Features

- 🔐 **Authentication System** — Email/password Login, Sign Up, and Forgot Password flows
- 📊 **Real-time Health Dashboard** — displays behavior, skin temperature, heart rate, and predicted diseases
- 🤖 **ML Disease Prediction** — XGBoost model classifying health status and predicting specific cattle diseases
- 🔍 **Detailed Health Flags** — low activity, very low activity, localized temperature rise, moderate heart rate indicators
- 🌐 **Multilingual Support** — Google Translate integration for global accessibility
- 📚 **Disease Information Library** — reference cards for 6 major cattle diseases with trusted external links
- ☁️ **Firebase Backend** — cloud database for persistent health record storage
- 📱 **Responsive UI** — card-based layout that adapts across screen sizes

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Backend** | Python (Flask / Firebase Admin SDK) |
| **Machine Learning** | XGBoost, Scikit-learn, Pandas, NumPy |
| **Database** | Firebase Realtime Database |
| **ML Notebook** | Jupyter Notebook |
| **Multilingual** | Google Translate Widget |
| **Authentication** | Firebase Authentication |

---

## 🏗 System Architecture

```
┌─────────────────────────────────────────────────────┐
│                  Frontend (HTML/CSS/JS)              │
│  Login → Dashboard → Health Cards → Disease Info    │
└────────────────────────┬────────────────────────────┘
                         │ REST API calls
┌────────────────────────▼────────────────────────────┐
│               Backend (Python / Flask)              │
│  • Fetch simulated sensor data                      │
│  • Run XGBoost prediction model                     │
│  • Generate health flags & disease predictions      │
└──────────┬──────────────────────────────┬───────────┘
           │ Read/Write                   │ Read
┌──────────▼──────────┐       ┌───────────▼───────────┐
│  Firebase Realtime  │       │  XGBoost ML Model     │
│  Database           │       │  (Trained .pkl file)  │
│  (Health Records)   │       │                       │
└─────────────────────┘       └───────────────────────┘
```

---

## 📁 Project Structure

```
Cattle-Health-Monitoring-System/
│
├── backend/
│   ├── app.py                  # Flask application entry point
│   ├── model/
│   │   ├── train_model.ipynb   # Jupyter notebook for XGBoost training
│   │   └── cattle_model.pkl    # Trained XGBoost model
│   ├── firebase_config.py      # Firebase Admin SDK setup
│   └── requirements.txt        # Python dependencies
│
├── front-end/
│   ├── index.html              # Login page
│   ├── signup.html             # Sign up page
│   ├── forgot-password.html    # Password reset page
│   ├── home.html               # Main health dashboard
│   ├── information.html        # Cattle diseases information page
│   ├── css/
│   │   └── styles.css          # Styling for all pages
│   └── js/
│       ├── auth.js             # Authentication logic
│       ├── dashboard.js        # Health data fetching & display
│       └── firebase-config.js  # Firebase client config
│
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Node.js (optional, for local dev server)
- Firebase project with Realtime Database enabled
- Git

### 1. Clone the Repository

```bash
git clone https://github.com/Gowthamtj17/SmartCattleMLSystem.git
cd SmartCattleMLSystem
```

### 2. Set Up the Backend

```bash
cd backend
pip install -r requirements.txt
```

Configure Firebase by adding your Firebase service account credentials:

```bash
# Place your Firebase service account JSON file in backend/
# Update firebase_config.py with your project credentials
```

### 3. Run the Backend Server

```bash
python app.py
```

The backend server will start at `http://localhost:5000`.

### 4. Set Up the Frontend

Open `front-end/js/firebase-config.js` and replace the placeholder values with your Firebase project's web config:

```javascript
const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT.firebaseapp.com",
  databaseURL: "https://YOUR_PROJECT.firebaseio.com",
  projectId: "YOUR_PROJECT_ID",
  ...
};
```

### 5. Launch the Frontend

Open `front-end/index.html` in your browser, or serve it with a local server:

```bash
# Using Python's built-in server
cd front-end
python -m http.server 8080
```

Visit `http://localhost:8080` in your browser.

---

## 🤖 Machine Learning Model

### Algorithm: XGBoost (Extreme Gradient Boosting)

XGBoost was selected for its high accuracy on tabular health data, robustness to missing values, and ability to handle imbalanced datasets — common in medical/health prediction tasks.

### Input Features

| Feature | Description |
|---|---|
| `skin_temperature` | Measured skin temperature in °C |
| `heart_rate` | Heart rate in BPM |
| `behavior` | Encoded behavioral state (Sleeping, Active, Grazing) |
| `activity_level` | Activity intensity score |
| `temp_rise_flag` | Boolean: localized temperature rise detected |

### Output

| Output | Description |
|---|---|
| `health_status` | HEALTHY / UNHEALTHY |
| `predicted_disease` | Specific predicted disease (e.g., Mastitis, BRD, Heat Stress) |
| `low_activity` | Boolean health flag |
| `very_low_activity` | Boolean health flag |
| `localized_temp_rise` | Boolean health flag |
| `moderate_heart_rate` | Boolean health flag |

### Training

The model was trained and evaluated in `backend/model/train_model.ipynb`. Open the notebook to explore data preprocessing, feature engineering, model training, and evaluation metrics.

---

## 📊 Dashboard Overview

| Page | Description |
|---|---|
| **Login** | Secure email/password authentication with brand mascot |
| **Sign Up** | New user account creation |
| **Forgot Password** | Email-based password reset flow |
| **Home (Dashboard)** | Live cattle health card showing behavior, temperature, heart rate, disease predictions, and a detailed health flags panel |
| **Information** | Reference cards for 6 cattle diseases with links to NCBI, Wikipedia, and extension resources |

---

## 🦠 Diseases Covered

| Disease | Description |
|---|---|
| **Bovine Respiratory Disease (BRD)** | Common cause of illness and death in cattle, especially calves |
| **Mastitis** | Inflammation of the mammary gland and udder tissue |
| **Heat Stress** | Condition caused by high temperatures and humidity |
| **Foot and Mouth Disease (FMD)** | Severe, highly contagious viral disease of livestock |
| **Ketosis** | Metabolic disorder due to energy imbalance in cattle |
| **Lameness** | Abnormal gait due to injury or disease |

---

## 🔮 Future Enhancements

- [ ] **Real IoT hardware integration** — connect physical sensors (temperature, accelerometer, heart rate) via MQTT or BLE
- [ ] **Multi-cattle support** — dashboard to monitor and switch between multiple animals in a herd
- [ ] **Push notifications** — SMS/email alerts to farmers when health status turns UNHEALTHY
- [ ] **Historical trend charts** — time-series graphs of health metrics over days/weeks
- [ ] **Mobile application** — React Native or Flutter app for on-farm mobile access
- [ ] **Veterinarian portal** — role-based access for vets to review records remotely
- [ ] **Offline mode** — local caching for use in areas with poor internet connectivity
- [ ] **Model retraining pipeline** — automated retraining as new health data accumulates

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

---

## 👨‍💻 Author

**Gowtham TJ**
- GitHub: [@Gowthamtj17](https://github.com/Gowthamtj17)

---

<p align="center">Made with ❤️ for smarter, healthier cattle farming</p>
