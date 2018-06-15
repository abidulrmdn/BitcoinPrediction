const express = require('express');
const app = express();

const mysql = require('mysql');
const pool = mysql.createPool({
  host: 'YourServersIpAddress',
  user: 'YourServersIpAddress-Sql-username',
  password: 'YourServersIpAddress-Sql-usernames-password',
  database: 'hackathon',
});

const request = require('request');

app.get('/twitter/:hashtag', (req, res) => {
  res.set('Access-Control-Allow-Origin', '*');
  pool.getConnection((err, connection) => {
    connection.query('SELECT * FROM twitter WHERE hashtag = ? ORDER BY timestamp ASC LIMIT 10000', [req.params['hashtag']], function (error, results, fields) {
      if (error) throw error;
      res.json(results);
    });
  });
});

app.post('/twitter/:hashtag', (req, res) => {
  if (!('hashtag' in req.params) || !req.params['hashtag'].match(/^[0-9a-z]+$/)) {
    res.json({'error': true});
    return;
  }

  request.post(
    'http://10.148.0.2:3000/twitter/' + req.params['hashtag'],
    {
      json: {},
    },
    function (error, response, body) {
      console.log(body)
    }
  );
  res.json({});
});

app.listen(80, () => console.log('Example app listening on port 80!'));
