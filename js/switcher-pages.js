//! Обновление страницы при нажатии на лого
function handleScroll() {
    var header = document.getElementById("myHeader");
    var sticky = header.offsetTop;
    if (window.scrollY > sticky) {
        header.classList.add("sticky");
    } else {
        header.classList.remove("sticky");
    }
}

window.addEventListener('scroll', handleScroll);


//! popup log in, reg..
document.addEventListener('DOMContentLoaded', function () {
    // Получение элементов DOM
    const loginLink = document.getElementById('login__link');
    const popupOverlay = document.querySelector('.popup__overlay');
    const popup = document.querySelector('.popup');
    const registerButton = document.querySelector('.toggle__form');
    const loginForm = document.getElementById('login__form');
    const registerForm = document.getElementById('register__form');

    //* Функция для сброса значений полей формы
    function resetForm(form) {
        form.querySelectorAll('input').forEach(input => {
            input.value = ''; //* Сбрасываем значение поля
        });
    }

    //* Обработчик события клика по ссылке для открытия попапа
    loginLink.addEventListener('click', function (event) {
        event.preventDefault(); 
        popupOverlay.style.display = 'block'; 
        popup.classList.remove('hidden'); 
        resetForm(loginForm); //* Сбрасываем значения полей формы входа
        resetForm(registerForm); //* Сбрасываем значения полей формы регистрации
        document.body.classList.add('modal__open'); //* Добавляем класс для блокировки прокрутки страницы
    });

    //* Обработчик события клика по кнопке закрытия попапа
    const closePopup = document.querySelector('.close__popup');
    closePopup.addEventListener('click', function () {
        popupOverlay.style.display = 'none'; //* Скрываем оверлей
        popup.classList.add('hidden'); //* Добавляем класс скрытия попапа
        document.body.classList.remove('modal__open'); //* Удаляем класс для разблокировки прокрутки страницы
    });

    //* Обработчик события отправки формы входа
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
        resetForm(loginForm); //* Сбрасываем значения полей формы входа
    });

    //* Обработчик события отправки формы регистрации
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault(); 
        resetForm(registerForm); //* Сбрасываем значения полей формы регистрации
    });

    //* Обработчик события клика по кнопке переключения формы
    registerButton.addEventListener('click', function () {
        if (loginForm.style.display === 'block') {
            loginForm.style.display = 'none';
            registerForm.style.display = 'block';
            registerButton.textContent = 'Войти';
        } else {
            registerForm.style.display = 'none';
            loginForm.style.display = 'block';
            registerButton.textContent = 'Зарегистрироваться';
        }
    });
});


document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('register__form');
    registerForm.addEventListener('submit', async function(event) {
        event.preventDefault(); // Предотвращаем стандартное поведение формы (перезагрузка страницы)
        
        const username = document.getElementById('register__username').value;
        const password = document.getElementById('register__password').value;

        try {
            const response = await fetch('/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ username, password })
            });

            if (response.ok) {
                const data = await response.json();
                console.log('User registered:', data.user);
                // Дополнительные действия, например, перенаправление на другую страницу
            } else {
                console.error('Registration failed');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });
});


//! переключение в нав меню на галерею
document.addEventListener("DOMContentLoaded", function() {
    const galleryLink = document.querySelector('.header__link[href="#gallery"]');
    const gallerySection = document.getElementById('gallery');

    if (galleryLink && gallerySection) {
        galleryLink.addEventListener('click', function(event) {
            event.preventDefault(); 
            const offsetTop = gallerySection.offsetTop; //* Получаем вертикальное смещение элемента относительно верхней границы родительского элемента
            window.scrollTo({ top: offsetTop, behavior: "smooth" }); // Прокручиваем страницу к секции галереи с плавной анимацией
        });
    }
});
