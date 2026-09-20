const passwordInput = document.getElementById('myPassword');
const toggleEye = document.getElementById('toggleEye');
const progressBar = document.getElementById('progressBar');
const feedbackMessage = document.getElementById('feedbackMessage');
const crackTimeText = document.getElementById('crackTime');

// Dictionnaire des cases de critères
const criteresUI = {
    longueur: document.getElementById('crit-longueur'),
    majuscules: document.getElementById('crit-majuscules'),
    minuscules: document.getElementById('crit-minuscule'),
    chiffres: document.getElementById('crit-chiffres'),
    speciaux: document.getElementById('crit-speciaux'),
    suites: document.getElementById('crit-suites')
};

// --- GESTION DE L'OEIL (AFFICHER/MASQUER) ---
if (toggleEye && passwordInput) {
    toggleEye.addEventListener('click', () => {
        if (passwordInput.type === 'password') {
            passwordInput.type = 'text';
            toggleEye.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z"></path><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>';
        } else {
            passwordInput.type = 'password';
            toggleEye.innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" d="M3.98 8.223A10.477 10.477 0 001.934 12C3.226 16.338 7.244 19.5 12 19.5c.993 0 1.953-.138 2.863-.395M6.228 6.228A10.45 10.45 0 0112 4.5c4.756 0 8.773 3.162 10.065 7.498a10.523 10.523 0 01-4.293 5.774M6.228 6.228L3 3m3.228 3.228l3.65 3.65m7.894 7.894L21 21m-3.228-3.228l-3.65-3.65m0 0a3 3 0 10-4.243-4.243m4.242 4.242L9.88 9.88" />';
        }
    });
}

// --- FONCTION DE MISE A JOUR DES COULEURS DES CASES ---
function updateCritereBox(element, value, minOrange, minGreen, reverseLogic = false) {
    if (!element) return;
    
    // Nettoyage des classes
    element.classList.remove('border-red', 'border-orange', 'border-green');
    
    let colorClass = 'border-red';
    
    if (reverseLogic) {
        // Pour les suites : moins c'est élevé, mieux c'est
        if (value <= minGreen) colorClass = 'border-green';
        else if (value <= minOrange) colorClass = 'border-orange';
    } else {
        // Logique classique : plus c'est élevé, mieux c'est
        if (value >= minGreen) colorClass = 'border-green';
        else if (value >= minOrange) colorClass = 'border-orange';
    }
    
    element.classList.add(colorClass);
}

// --- APPEL API FASTAPI A CHAQUE FRAPPE ---
if (passwordInput) {
    passwordInput.addEventListener('input', async (e) => {
        const motDePasse = e.target.value;

        // Reset si vide
        if (motDePasse.length === 0) {
            progressBar.style.width = '0%';
            progressBar.style.backgroundColor = 'transparent';
            feedbackMessage.textContent = 'En attente de saisie...';
            feedbackMessage.style.color = '#6b7280';
            crackTimeText.textContent = 'Instantané';
            crackTimeText.style.color = '#EF4444';
            
            // Remise à zéro (gris) de toutes les cases
            Object.values(criteresUI).forEach(box => {
                if(box) box.className = 'bloc-les-bonnes-pratiques';
            });
            return;
        }

        // 1. Estimation temporelle avec zxcvbn
        if (typeof zxcvbn !== 'undefined') {
            const zxcvbnResult = zxcvbn(motDePasse);
            const times = zxcvbnResult.crack_times_display;
            crackTimeText.textContent = times.offline_slow_hashing_1e4_per_second;
            crackTimeText.style.color = zxcvbnResult.score >= 3 ? '#10b981' : '#EF4444';
        }

        // 2. Appel au backend FastAPI
        try {
            const response = await fetch('https://api-testeur-mdp.onrender.com/api/tester-mdp', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ mot_de_passe: motDePasse })
            });

            if (response.ok) {
                const data = await response.json();
                
                // --- Mise à jour de la jauge et du texte ---
                let color = '#ef4444'; // Rouge par défaut
                if (data.score >= 90) color = '#10b981'; // Vert
                else if (data.score >= 70) color = '#84cc16'; // Vert clair
                else if (data.score >= 40) color = '#f59e0b'; // Orange

                progressBar.style.width = data.score + '%';
                progressBar.style.backgroundColor = color;
                feedbackMessage.textContent = data.message;
                feedbackMessage.style.color = color;

                // --- Mise à jour des cases de critères (Rouge, Orange, Vert) ---
                const details = data.details;
                updateCritereBox(criteresUI.longueur, details.longueur, 8, 16);
                updateCritereBox(criteresUI.majuscules, details.nbMajuscule, 1, 3);
                updateCritereBox(criteresUI.minuscules, details.nbMinuscule, 1, 3);
                updateCritereBox(criteresUI.chiffres, details.nbNombres, 1, 3);
                updateCritereBox(criteresUI.speciaux, details.nbCaractereSpeciaux, 1, 2);
                
                // Pour les suites de lettres, la logique est inversée (nbMaxLettreConsecutive[0])
                updateCritereBox(criteresUI.suites, details.nbMaxLettreConsecutive[0], 2, 1, true);
            }
        } catch (error) {
            console.error("Erreur de connexion à l'API:", error);
            feedbackMessage.textContent = "Erreur de connexion au serveur.";
            feedbackMessage.style.color = "#ef4444";
        }
    });
}
