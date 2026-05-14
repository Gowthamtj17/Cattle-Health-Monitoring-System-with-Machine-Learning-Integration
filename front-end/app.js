// Import Firebase functions
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.14.0/firebase-app.js";
import { getDatabase, ref, onValue } from "https://www.gstatic.com/firebasejs/10.14.0/firebase-database.js";

// Your web app's Firebase configuration
const firebaseConfig = {
    apiKey: "",
    authDomain: "",
    databaseURL: "",
    projectId: "",
    storageBucket: "",
    messagingSenderId: "",
    appId: "",
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = getDatabase(app); // For Realtime Database

// Fetch data from Firebase Realtime Database
function fetchData() {
    const dbRef = ref(db, 'cattle_health_predictions'); // Reference to your table

    onValue(dbRef, (snapshot) => {
        const data = snapshot.val();
        if (data) {
            // Get all entries
            const entries = Object.entries(data);

            // Check if there are any entries
            if (entries.length === 0) {
                console.error("No entries found in database.");
                return;
            }

            // Get the last entry (latest data at the bottom)
            const lastEntry = entries[entries.length - 1];
            const cattleData = lastEntry[1].Health_Data; // Access Health_Data
            const timestamp = lastEntry[1].Timestamp;   // Access Timestamp (outside Health_Data)

            // Update HTML with cattle data
            document.getElementById('heart-rate').innerText = cattleData.HeartRate_BPM || 'N/A';
            document.getElementById('skin-temp').innerText = cattleData.SkinTemp_Celsius || 'N/A';
            document.getElementById('behavior').innerText = cattleData.Behavior || 'N/A';
            document.getElementById('health-status').innerText = cattleData.Health_Status || 'N/A';
            
            // Display predicted diseases correctly
            const diseasesElement = document.getElementById('predicted-diseases');
            const predictedDiseases = cattleData.Predicted_Diseases;
            if (predictedDiseases) {
                diseasesElement.innerHTML = ""; // Clear previous content
                Object.values(predictedDiseases).forEach((disease, index) => {
                    const diseaseItem = document.createElement('p');
                    diseaseItem.innerHTML = `<strong>Disease ${index + 1}:</strong> ${disease}`;
                    diseasesElement.appendChild(diseaseItem);
                });
            } else {
                diseasesElement.innerText = 'No specific disease detected';
            }


            const analysisData = cattleData.Activity_Analysis;
            document.getElementById('low-activity').innerText = analysisData.Low_Activity ? 'true' : 'false';
            document.getElementById('very-low-activity').innerText = analysisData.Very_Low_Activity ? 'true' : 'false';
            document.getElementById('localized-temp-rise').innerText = analysisData.Localized_Temp_Rise ? 'true' : 'false';
            document.getElementById('moderate-heart-rate').innerText = analysisData.Moderate_Heart_Rate ? 'true' : 'false';

            // Display timestamp from database (outside Health_Data)
            const formattedTimestamp = timestamp ? new Date(timestamp).toLocaleString() : 'N/A';
            document.getElementById('timestamp-db').innerText = formattedTimestamp;

            // Display current timestamp
            const currentTime = new Date().toLocaleString(); // Get current time in local format
            document.getElementById('current-time').innerText = currentTime;

        } else {
            console.error("No data available");
        }
    }, (error) => {
        console.error("Error fetching data:", error);
    });
}

// Call fetchData on page load
fetchData();