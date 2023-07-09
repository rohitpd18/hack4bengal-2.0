const showPasswordCheckbox = document.getElementById('show-password-checkbox');
const passwordInput = document.getElementById('password');

console.log("hiii")

showPasswordCheckbox.addEventListener('change', function() {
    // console.log("hiii")
    if (showPasswordCheckbox.checked) {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
});
