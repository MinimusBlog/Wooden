// document.addEventListener('DOMContentLoaded', function() {
//     var swiper = new Swiper(".mySwiper", {
//         spaceBetween: 30,
//         navigation: {
//             nextEl: ".swiper-button-next",
//             prevEl: ".swiper-button-prev",
//         },
//         pagination: {
//             el: ".swiper-pagination",
//         },
//         mousewheel: true,
//         keyboard: true,
//     });
// });

// const { default: Swiper } = require("swiper");

// const swiper = new Swiper('.swiper', {
//     direction: "vertical",
//     loop: true,
//     pagination: {
//         el: 'swiper-pagination',
//     },
//     navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     },
//     scrollbar: {
//         el: '.swiper-scrollbar',
//     },
// });


document.addEventListener('DOMContentLoaded', function() {
    const swiper = new Swiper('.swiper', {
        direction: 'horizontal', // направление прокрутки слайдов
        loop: true, // круговой слайдер
        speed: 500, // скорость переключения слайдов
        effect: 'slider', // эффект переключения слайдов
        slidesPerView: 1, // количество видимых слайдов
        pagination: { // настройки пагинации (точек)
            el: '.swiper-pagination',
            clickable: true,
        },
        navigation: { // настройки навигации (стрелок)
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        mousewheel: true, // использование колеса мыши для прокрутки слайдов
        keyboard: true, // использование клавиатуры для навигации по слайдам
    });
});



// "use strict"
// //==========================================

// //! ============== 1 вариант SWIPER ==============
// const swiper = new Swiper('.swiper', {

//     //! Основные настройки 
//     direction: 'horizontal', // 'vertical', 'horizontal'
//     loop: true, // true - круговой слайдер, false - слайдер с конечными положениями
//     speed: 500, // скорость переключения слайдов
//     effect: 'slider', // cards, coverflow, flip, fade, cube
//     // initialSlide: 2, // Начинаем со 2 слайдера
//     // freeMode: true, // можно перетаскивать как ленту
//     slidesPerView: 1, // кол-во активных слайдов
//     // centeredSlides: true, // центрирование слайдов
    
//     //! Пагинация (точки)
//     pagination: {
//         el: '.swiper-pagination',
//         clickable: true, // true - Пагинация становится кликабельной
//     },

//     //! Кнопки вперед и назад 
//     navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     },

//     //! Автоматическое перелистывание
//     // autoplay: {
//     //     delay: 1000, //Задержка перед перелистыванием 1с = 1000мл/с
//     // },
// });

