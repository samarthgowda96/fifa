# fifa
To build

docker build -t flaskapp .

To run

docker run -d --name p1 -p 5000:5000 flaskapp

To Stop and Re-build the container

docker container stop p1 && docker container rm p1 && docker build -t flaskapp . && docker run -d --name p1 -p 5000:5000 flaskapp
