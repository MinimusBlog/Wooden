function redirectToLoginPage() { //с иконки на форму авторизации
    window.location.href = 'pages/login.html';
}
function toggleLoginForm() {
    const loginForm = document.querySelector('.login-form');
    loginForm.classList.toggle('active');
}