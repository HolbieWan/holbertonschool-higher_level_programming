# Use the Alpine base image
FROM alpine:latest

# Install curl package
RUN apk --no-cache add curl

# Copy config.txt to /app directory in the container
COPY config.txt /app/config.txt

# Set the working directory
WORKDIR /app