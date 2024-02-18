// AOS.init(); // Подключение библиотеки анимаций
// window.addEventListener('load', AOS.refresh)

// $(function() {
//       AOS.init();s
//  });


//! Подключение к БД
const { Client } = require('pg');

//* экземпляр клиента PostgreSQL
const client = new Client({
  user: 'User',
  host: 'localhost',
  database: 'wooden',
  password: '12345',
  port: 5432, //* Порт по умолчанию для PostgreSQL
});

//* Подключение к базе данных
client.connect()
  .then(() => console.log('Connected to PostgreSQL'))
  .catch(err => console.error('Connection error', err.stack));

//* Пример выполнения SQL-запроса
client.query('SELECT * FROM your_table')
  .then(result => console.log(result.rows))
  .catch(err => console.error('Query error', err.stack));

//* Закрытие соединения с базой данных
client.end()
  .then(() => console.log('Connection closed'))
  .catch(err => console.error('Error closing connection', err.stack));


// const navToggle = document.querySelector('#nav-toggle');
// const navList = document.querySelector('#nav-list');

// navToggle.addEventListener('click', () => {
//   navList.toggleAttribute('hidden');
// });

