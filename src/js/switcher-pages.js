function redirectToLoginPage() { //с иконки на форму авторизации
    window.location.href = 'pages/login.html';
}

function toggleLoginForm() {
    const loginForm = document.querySelector('.login-form');
    loginForm.classList.toggle('active');
}

document.addEventListener("DOMContentLoaded", function() {
    const galleryLink = document.querySelector('.header__link[href="#gallery"]');
    const gallerySection = document.getElementById('gallery');

    if (galleryLink && gallerySection) {
        galleryLink.addEventListener('click', function(event) {
            event.preventDefault(); // Prevent default link behavior
            const offsetTop = gallerySection.offsetTop; // Получаем вертикальное смещение элемента относительно верхней границы родительского элемента
            window.scrollTo({ top: offsetTop, behavior: "smooth" }); // Прокручиваем страницу к секции галереи с плавной анимацией
        });
    }
});
