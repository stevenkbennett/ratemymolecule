# Dockerfile for RateMyMolecule.
FROM python:3.7.3

# Change current working directory.
WORKDIR /app

# Copy current directory into container at /app.
ADD . /app

# Install dependencies.
RUN pip install -r requirements.txt

# Start uWSGI.
CMD ["uwsgi", "app.ini"]