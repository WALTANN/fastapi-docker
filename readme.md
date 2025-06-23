It's my first practice project in iTMO at 2nd studys course. You can see microservices on Python with using FastAPI and docker. 

I used dockerfiles and docker-compose (dockerfile -> docker-compose), cos my docker-compose version is 1.29.2, if you have a new version docker-compose you can remove dockerfiles from directories and write docker-compose with inline, it's more than cool :)

You can see 3 dir with any mcrservices. Build project (`docker-compose up --build`) at mother-dir and you can check services on the ports 8000, 8001, 8002 at the .env:

- `Auth` - http://localhost:8000/docs (swagger)
- `Users` - http://localhost:8001/docs (swagger)
- `Prod` - http://localhost:8002/docs (swagger)

In the swagger you can check services with post-orders (pick try it out)

other routes:

http://localhost:8000/ring
http://localhost:8001/king
http://localhost:8002/hello
