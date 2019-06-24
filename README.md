# redis-uni
redis university


https://hub.docker.com/_/redis

docker run --name redis -d redis:5.0.5-alpine

or, better:
docker-compose up -d

docker exec -it redis 'redis-cli'
redis-cli> set hello world

python3 helloworld.py

course notes: notes.txt
