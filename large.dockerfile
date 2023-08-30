# set base image (host OS)
FROM python:latest
ENV FLASK_ENV development
# set the working directory in the container
WORKDIR /chatApp
# copy the dependencies file to the working directory
COPY requirements.txt .
ENV TZ 'Israel'
# install dependencies
RUN pip install -r requirements.txt
ENV DATA_DIR='./data/'
ENV ROOMS_DIR=${DATA_DIR}'rooms/'
# copy the content of the local src directory to the working directory
COPY . .
# command to run on container start
CMD [ "python", "./chatApp.py" ]

