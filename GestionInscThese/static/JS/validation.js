

  const form = document.querySelector('form');
  const nom = document.getElementById('nom');
  const prenom = document.getElementById('prenom');
  const email = document.getElementById('email');
  const motDePasse = document.getElementById('mot_de_passe');
  const motDePasseConfirmation = document.getElementById('mot_de_passe_confirmation');

  function validateForm() {
    let isValid = true;

    // Vérifier si les champs sont vides
    if (nom.value === '') {
      nom.style.borderColor = 'red';
      isValid = false;
    } else {
      nom.style.borderColor = '';
    }

    if (prenom.value === '') {
      prenom.style.borderColor = 'red';
      isValid = false;
    } else {
      prenom.style.borderColor = '';
    }

    if (email.value === '') {
      email.style.borderColor = 'red';
      isValid = false;
    } else {
      email.style.borderColor = '';
    }

    if (motDePasse.value === '') {
      motDePasse.style.borderColor = 'red';
      isValid = false;
    } else {
      motDePasse.style.borderColor = '';
    }

    if (motDePasseConfirmation.value === '') {
      motDePasseConfirmation.style.borderColor = 'red';
      isValid = false;
    } else {
      motDePasseConfirmation.style.borderColor = '';
    }

    // Vérifier si les mots de passe correspondent
    if (motDePasse.value !== motDePasseConfirmation.value) {
      motDePasse.style.borderColor = 'red';
      motDePasseConfirmation.style.borderColor = 'red';
      isValid = false;
    }

    return isValid;
  }

  form.addEventListener('submit', function(event) {
    if (!validateForm()) {
      event.preventDefault();
    }
  });








/*
const form = document.getElementById('form');
const Nom = document.getElementById('Nom');
const Prenom = document.getElementById('Prenom');
const Email = document.getElementById('Email');
const password = document.getElementById('password');
const password2 = document.getElementById('password2');


form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});


const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const isValidEmail = email => {
    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

const validateInputs = () => {
    const nomeValue = Nom.value.trim();
    const prenomValue = Prenom.value.trim();

    const emailValue = Email.value.trim();
    const passwordValue = password.value.trim();
    const password2Value = password2.value.trim();

    if(nomeValue === '') {
        setError(nomeValue, 'Username is required');
    } else {
        setSuccess(nomeValue);
    }
    if(prenomValue === '') {
        setError(prenomValue, 'Username is required');
    } else {
        setSuccess(prenomValue);
    }

    if(emailValue === '') {
        setError(email, 'Email is required');
    } else if (!isValidEmail(emailValue)) {
        setError(email, 'Provide a valid email address');
    } else {
        setSuccess(email);
    }

    if(passwordValue === '') {
        setError(password, 'Password is required');
    } else if (passwordValue.length < 8 ) {
        setError(password, 'Password must be at least 8 character.')
    } else {
        setSuccess(password);
    }

    if(password2Value === '') {
        setError(password2, 'Please confirm your password');
    } else if (password2Value !== passwordValue) {
        setError(password2, "Passwords doesn't match");
    } else {
        setSuccess(password2);
    }

};

*/




/*
    <script>
    function validerFormulaire() {
        var nom = document.getElementById("nom").value;
        var prenom = document.getElementById("prenom").value;
        var email = document.getElementById("email").value;
        var motDePasse = document.getElementById("password").value;
        var motDePasseConfirmation = document.getElementById("password2").value;

        if (nom === "" || prenom === "" || email === "" || motDePasse === "" || motDePasseConfirmation === "") {
            alert("Tous les champs obligatoires doivent être remplis");
            return false;
        }

        if (motDePasse !== motDePasseConfirmation) {
            alert("Les deux champs de mot de passe doivent correspondre");
            return false;
        }

        return true;
    }
    </script>
*/