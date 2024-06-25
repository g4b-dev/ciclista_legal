// validate.js

document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const password = document.querySelector('input[name="password"]');
    const confirmPassword = document.querySelector('input[name="confirm-password"]');

    form.addEventListener('submit', function (event) {
        if (password.value !== confirmPassword.value) {
            event.preventDefault();
            alert('As senhas não coincidem.');
        }
    });
});
