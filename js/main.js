//! Импорт скриптов
import "./script.js";
import "./switcher-pages.js";
import "./libs/swiper-bundle.min.js";
import "./gallery.js";

document.querySelector('#login__form').addEventListener('submit', async (event) => {
  event.preventDefault()

  const formData = new FormData(event.target)
  const username = formData.get('username')
  const password = formData.get('password')

  try {
    const response = await fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      body: new URLSearchParams({ username, password })
    })

    if (response.ok) {
      // Если вход успешен, перенаправляем пользователя на страницу личного кабинета
      location.href = '/lk'
    } else {
      // Если вводныны данные неверны, выводим ошибку
      alert('Invalid username or password')
    }
  } catch (err) {
    console.error(err)
    alert('Server error')
  }
})

//!Library


