# pull official base image
FROM python:3.7-alpine

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv

# Create a non-root user.  It doesn't own the source files,
# and so can't modify the application.
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Create site wordking dir
WORKDIR /home/appuser/personal_site

# Copy project
COPY . .

# Needed in Alpine to install additional dependencies that get Django to work
RUN apk add --no-cache \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

USER appuser

RUN pipenv sync

EXPOSE 80/tcp

# set environment varibles
ENTRYPOINT ["sh", "/home/appuser/personal_site/entrypoint.sh"]
