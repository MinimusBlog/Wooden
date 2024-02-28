// AOS.init(); // Подключение библиотеки анимаций
// window.addEventListener('load', AOS.refresh)

// $(function() {
//       AOS.init();s
//  });


// const navToggle = document.querySelector('#nav-toggle');
// const navList = document.querySelector('#nav-list');

// navToggle.addEventListener('click', () => {
//   navList.toggleAttribute('hidden');
// });


// function openCategory(category) {
//     const categories = document.querySelectorAll('.category');
//     categories.forEach(cat => {
//         cat.classList.remove('selected');
//     });

//     const selectedCategory = document.querySelector(`.category[data-category="${category}"]`);
//     selectedCategory.classList.add('selected');

//     const products = document.querySelectorAll('.product__card');
//     products.forEach(product => {
//         const productCategories = product.classList;
//         if (category === 'all') {
//             product.style.visibility = 'visible';
//         } else if (category === 'home') {
//             if (productCategories.contains('home')) {
//                 product.style.visibility = 'visible';
//             } else {
//                 product.style.visibility = 'hidden';
//             }
//         } else if (productCategories.contains(category)) {
//             product.style.visibility = 'visible';
//         } else {
//             product.style.visibility = 'hidden';
//         }
//     });
// }

document.addEventListener('DOMContentLoaded', function() {
    openCategory('all');
});


function openCategory(category) {
    const categories = document.querySelectorAll('.category');
    categories.forEach(cat => {
        cat.classList.remove('selected');
    });

    const selectedCategory = document.querySelector(`.category[data-category="${category}"]`);
    selectedCategory.classList.add('selected');

    const allProductSections = document.querySelectorAll('.cards, .cards__toys, .cards__home, .cards__other');
    allProductSections.forEach(section => {
        if (category === 'all') {
            if (!section.classList.contains('cards')) {
                section.style.display = 'none';
            } else {
                section.style.display = 'block';
            }
        } else {
            if (section.classList.contains(`cards__${category}`)) {
                section.style.display = 'block';
            } else {
                section.style.display = 'none';
            }
        }
    });
}