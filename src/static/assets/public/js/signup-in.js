// Show/Hide Password
document.querySelectorAll('.togglePassword').forEach(function(button) {
    button.addEventListener('click', function () {
        let targetPasswordId = button.getAttribute('data-target-password');
        let targetIconId = button.getAttribute('data-target-icon');
        let targetIconSlashId = button.getAttribute('data-target-icon-slash');
        togglePasswordVisibility(targetPasswordId, targetIconId, targetIconSlashId);
    });
});

function togglePasswordVisibility(passwordId, toggleIconId, toggleIconSlashId) {
    const password = document.getElementById(passwordId);
    const toggleIcon = document.getElementById(toggleIconId);
    const toggleIconSlash = document.getElementById(toggleIconSlashId);

    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);

    // Toggle icons
    toggleIcon.classList.toggle('hidden');
    toggleIconSlash.classList.toggle('hidden');
}

function validateForm(formId) {
    var phone = document.getElementById("phone").value;
    var password = document.getElementById("password").value;
    var confirmPassword = document.getElementById("confirm-password") ? document.getElementById("confirm-password").value : null;

    var errorMessages = document.querySelectorAll('.error-message');
    var inputFields = document.querySelectorAll('input');
    errorMessages.forEach(function(error) {
        error.remove();
    });
    inputFields.forEach(function(input) {
        input.classList.remove("input-error");
    });

    var isValid = true;

    // Phone number validation
    var phonePattern = /^[0-9]{10}$/; // فرض بر این است که شماره تلفن باید 10 رقمی باشد
    if (!phonePattern.test(phone)) {
        showError("phone-error", "لطفا یک شماره تلفن معتبر وارد کنید");
        isValid = false;
    }

    // Check the password field
    if (password == "") {
        showError("password-error", "لطفا رمز عبور خود را وارد کنید");
        isValid = false;
    }

    // If it's the signup form, validate confirm password
    if (formId === 'signup' && confirmPassword === null) {
        showError("confirm-password-error", "لطفا تایید رمز عبور را وارد کنید");
        isValid = false;
    }

    // Check password confirmation (only in signup form)
    if (formId === 'signup' && password !== confirmPassword) {
        showError("confirm-password-error", "رمز عبور و تایید آن باید یکسان باشند");
        isValid = false;
    }

    // Check password length
    if (password.length < 6) {
        showError("password-error", "رمز عبور باید حداقل 6 کاراکتر باشد");
        isValid = false;
    }

    return isValid;
}

function showError(errorId, message) {
    var errorElement = document.createElement("span");
    errorElement.classList.add("error-message");
    errorElement.textContent = message;

    // Add error class to input for border color change
    var inputElement = document.getElementById(errorId.replace("-error", ""));
    inputElement.classList.add("input-error");

    // Find the error element and append the error message
    var errorContainer = document.getElementById(errorId);
    errorContainer.innerHTML = ''; // Clear previous errors
    errorContainer.appendChild(errorElement);
}
