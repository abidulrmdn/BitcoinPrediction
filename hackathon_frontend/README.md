# Frontend for 2018 Hackathon - Team HK - Bitcoin Prediction

## Usage

1. Install node
```
brew install node
```

2. Install watchman to run the local test
```
brew install watchman
```

3. Install the dependencies
```
npm install
```

4. Start local test run
```
npm test
```

5. Start local webserver
```
npm start
```

6. Try the page for dummy result without API connection
 - The page will show "Price will go down" for keyword "dummy-buy"
 - The page will show "Price will go up" for keyword "dummy-no"
 - The page will show "Please try another keyword" for keyword "dummy-error"

7. Build static files
```
npm run build
```

8. Serve static files from inside a docker

docker run --name nginx -p80:80 -v ./build:/usr/share/nginx/html:ro -d nginx

[replace your local path above]
