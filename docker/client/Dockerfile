# Use the official Node.js image as a base
FROM node:20 AS build

# Set the working directory inside the container
WORKDIR /web/client

# Copy package.json and package-lock.json
COPY ../../web/client . 

# Install dependencies
RUN npm install

# Expose port 4200 for Angular development server
EXPOSE 4200/tcp

# Command to run the Angular development server
CMD ["sleep", "infinity"]
#CMD ["npm", "run", "start", "--", "--host", "0.0.0.0", "--poll", "500"]
