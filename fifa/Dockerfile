FROM ubuntu:18.04
LABEL MAINTAINER="sg37025p@pace.edu"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
 