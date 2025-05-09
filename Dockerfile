# Use the official Python 3 image from Docker Hub
FROM python:3

# Set the working directory in the container
WORKDIR /app

# Define a build argument for the bot token
ARG BOT_TOKEN

# Set the environment variable using the build argument
ENV key=$BOT_TOKEN

# Copy the current directory contents into the container
COPY . /app

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run your application
CMD ["python", "bot.py"]