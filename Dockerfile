# base image
FROM python:3.11.5-alpine

# update Linux Alpine image
RUN apk update && apk upgrade

# create directory in the image
RUN mkdir /Project13OC

# Copy file
COPY . /Project13OC

# change directory in the image
WORKDIR /Project13OC

# create virtual environnement
RUN python -m venv /venv

# activate virtuel environnement
SHELL ["/bin/sh", "-c"]
RUN source /venv/bin/activate

# update pip
RUN pip install --upgrade pip

# Install dependancies
RUN pip install -r requirements.txt

# update staticfiles folder in case of modification of files in static folder
RUN python3 manage.py collectstatic --noinput

# port where the Django app runs  
EXPOSE 8000

# launch django web server
CMD ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "oc_lettings_site.wsgi"] # with live log on console

