**Install Docker CE:**

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install -y docker-ce
```

**Init Docker Swarm:**

```
docker swarm init --advertise-addr YourServersIpAddress
```

**Join Docker Swarm:**

```
docker swarm join --token your-token-here YourServersIpAddress:2377
```

**Add hackathon-twitter to Registry:**

```
docker run -d -p5000:5000 registry
docker build . -t YourServersIpAddress:5000/hackathon-twitter
docker push YourServersIpAddress:5000/hackathon-twitter
```

**Setup Docker Registry for Workers:**

```
echo '{ "insecure-registries":["YourServersIpAddress:5000"] }' > /etc/docker/daemon.json
service docker restart
```

**Create or Update hackathon-twitter Service**

```
docker service create --name=hackathon-twitter-asdfg YourServersIpAddress:5000/hackathon-twitter node /usr/src/app/twitter.js asdfg
docker service update --image YourServersIpAddress:5000/hackathon-twitter hackathon-twitter-asdfg
```

**Run hackathon-twitter-api**

```
docker build -t hackathon-twitter-api .
docker run -d --name hackathon-twitter-api -p80:80 hackathon-twitter-api
```

**Run hackathon-twitter-trigger**

```
nohup nodejs server.js &
```
