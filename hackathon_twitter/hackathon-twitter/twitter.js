const puppeteer = require('puppeteer');

const mysql = require('mysql');
const connection = mysql.createConnection({
  host: 'YourServersIpAddress',
  user: 'YourServersIpAddress-Sql-username',
  password: 'YourServersIpAddress-Sql-usernames-password',
  database: 'hackathon',
});
connection.connect();

const moment = require('moment-timezone');

let hashtag = process.argv[2];

(async () => {
  const browser = await puppeteer.launch({
    args: ['--no-sandbox'],
    executablePath: '/usr/bin/chromium-browser',
  });
  const page = await browser.newPage();
  await page.goto('https://twitter.com/hashtag/' + hashtag);

  await page.waitFor(5000);

  let count = 0;
  while (true) {
    let tweets = await page.evaluate(() => {
      var data = $('#stream-items-id .stream-item').map(function() {
        $('.twitter-hashflag-container, .twitter-timeline-link', this).remove();
        return {
          username: $('.username', this).text(),
          timestamp: $('._timestamp', this).attr('data-time'),
          text: $.trim($('.content .tweet-text', this).text()),
        };
      });
      return data.toArray();
    });

    tweets = tweets.slice(count, tweets.length);
    if (tweets.length === 0) {
      break;
    }

    tweets.forEach(async (tweet) => {
      await connection.query('INSERT INTO twitter SET ?', {
        hashtag: hashtag,
        text: tweet.text,
        username: tweet.username,
        timestamp: moment(tweet.timestamp * 1000).tz('UTC').format('YYYY-MM-DD HH:mm:ss'),
      }, async (error, results, fields) => {
        if (error) {
          await page.waitFor(300000); // 5 minutes
          throw error;
        }
        console.log(results.insertId);
      });
    });

    count += tweets.length;
    if (count >= 1000) {
      break;
    }

    await page.evaluate(() => {
      $('html, body').scrollTop($(document).height());
    });
    await page.waitFor(5000);
  }

  await browser.close();
  await connection.end();
})();
