# base image
FROM python:3.11.5-alpine

# create directory in the image
RUN mkdir /Project13OC

# Copy file
COPY . /Project13OC

# change directory
WORKDIR /Project13OC

# Install dependancies
RUN pip install -r requirements.txt

# update Linux image
RUN apk update && apk upgrade

# update staticfiles folder
RUN python3 manage.py collectstatic --noinput

# port where the Django app runs  
EXPOSE 8000

# launch django web server
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
