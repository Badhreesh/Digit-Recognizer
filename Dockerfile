FROM python:3.6-slim-stretch

# set a directory for the app
WORKDIR /usr/src/app

# copy all the files to the container
COPY . .

# Install OpenCv's runtime dependencies and other dependencies
RUN apt-get update && \
    apt-get -y install libglib2.0-0 --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt

# Run the image as a non-root user
RUN adduser --disabled-password myuser
USER myuser

# run the command
CMD gunicorn --bind 0.0.0.0:$PORT wsgi
