import { auth, db } from './firebase-config.js'; // Import auth and db
import { createUserWithEmailAndPassword, signInWithEmailAndPassword, sendPasswordResetEmail, signOut } from "https://www.gstatic.com/firebasejs/10.14.0/firebase-auth.js";
import { getDocs, collection } from "https://www.gstatic.com/firebasejs/10.14.0/firebase-firestore.js";

document.addEventListener('DOMContentLoaded', () => {
    // Login Functionality
    const loginForm = document.getElementById('loginForm');
    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            signInWithEmailAndPassword(auth, email, password)
                .then((userCredential) => {
                    // Redirect to home page
                    window.location.href = "home.html";
                })
                .catch((error) => {
                    alert(error.message);
                });
        });
    }

    // Signup Functionality
    const signupForm = document.getElementById('signupForm');
    if (signupForm) {
        signupForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('signupEmail').value;
            const password = document.getElementById('signupPassword').value;

            createUserWithEmailAndPassword(auth, email, password)
                .then((userCredential) => {
                    // Redirect to login page
                    window.location.href = "index.html";
                })
                .catch((error) => {
                    alert(error.message);
                });
        });
    }

    // Forgot Password Functionality
    const forgotPasswordForm = document.getElementById('forgotPasswordForm');
    if (forgotPasswordForm) {
        forgotPasswordForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = document.getElementById('forgotEmail').value;

            sendPasswordResetEmail(auth, email)
                .then(() => {
                    alert("Password reset email sent!");
                })
                .catch((error) => {
                    alert(error.message);
                });
        });
    }

    // Home Page Logic
    const cattleDataDiv = document.getElementById('cattleData');
    if (cattleDataDiv) {
        const fetchCattleData = async () => {
            const querySnapshot = await getDocs(collection(db, "cattleData"));
            let html = '<h3>Cattle Details</h3>';
            querySnapshot.forEach((doc) => {
                const data = doc.data();
                html += `
                    <div class="cattle">
                        <h4>${data.name}</h4>
                        <p>Status: ${data.healthStatus}</p>
                        ${data.healthStatus === 'Unhealthy' ? `<p>Predicted Disease: ${data.disease}</p>` : ''}
                    </div>
                `;
            });
            cattleDataDiv.innerHTML = html;
        };
        fetchCattleData();
    }

    // Logout Functionality
    const logoutBtn = document.getElementById('logoutBtn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', () => {
            signOut(auth).then(() => {
                window.location.href = "index.html";
            }).catch((error) => {
                alert(error.message);
            });
        });
    }
});

function toggleMenu() {
    document.getElementById("navMenu").classList.toggle("show");
}
