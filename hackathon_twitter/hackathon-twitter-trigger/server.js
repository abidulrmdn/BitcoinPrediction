const express = require('express');
const app = express();

const util = require('util');
const child_process = require('child_process');

app.post('/twitter/:hashtag', (req, res) => {
  console.log(req.params['hashtag']);
  console.log('docker service create --name=hackathon-twitter-' + req.params['hashtag'] + ' YourServersIpAddress:5000/hackathon-twitter node /usr/src/app/twitter.js ' + req.params['hashtag']);
  child_process.exec('docker service create --name=hackathon-twitter-' + req.params['hashtag'] + ' YourServersIpAddress:5000/hackathon-twitter node /usr/src/app/twitter.js ' + req.params['hashtag']);
  res.json({});
});

app.listen(3000, () => console.log('Example app listening on port 3000!'));
