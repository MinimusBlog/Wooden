const http = require("http");
const fs = require("fs");
const path = require("path");
const port = 5432; // Порт для сервера

// Массив MIME-типов для расширений файлов
const mimeTypes = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'text/javascript',
    '.json': 'application/json',
    '.png': 'image/png',
    '.jpg': 'image/jpg',
    '.gif': 'image/gif',
};

// Функция для отправки статических файлов
function staticFile(res, filePath, ext) {
    res.setHeader('Content-Type', mimeTypes[ext]); // Убрано лишнее запятая после 'Content-Type'
    fs.readFile('./public' + filePath, (error, data) => {
        if (error) {
            res.statusCode = 404; // Исправлено на statusCode
            res.end();
        } else {
            res.end(data);
        }
    });
}

http.createServer(function (req, res) {
    let urlPath = req.url; // Переименовано в urlPath, чтобы не пересекаться с модулем url

    switch (urlPath) {
        case '/':
            console.log('index page');
            staticFile(res, '/index.html', '.html'); // Поправлен путь до index.html
            break;
        default:
            const extname = String(path.extname(urlPath)).toLowerCase(); // Переименовано в extname и исправлено на toLowerCase()
            if (extname in mimeTypes) staticFile(res, urlPath, extname); // Поправлено на extname
            else {
                res.statusCode = 404; // Исправлено на statusCode
                res.end();
            }
    }
}).listen(port, () => { // Исправлено на listen(port, () =>
    console.log(`Server is running on port ${port}`); // Добавлено обратные кавычки для использования шаблонных строк
});
