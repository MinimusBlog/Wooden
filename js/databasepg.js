const { Client } = require('pg');

const client = new Client({
    host: '192.168.1.35',
    user: 'postgres',
    port: 5432,
    password: 'rot360prav',
    database: 'postgres'
});

client.connect();

client.query('SELECT * FROM wood.products', (err, res) => {
    if (!err) {
        console.log(res.rows);
    } else {
        console.error(err.message);
    }
    client.end();
});