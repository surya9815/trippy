# Use the official Node.js image as a base image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the React application
RUN npm run build

# Expose port 3000 to the outside world
EXPOSE 3000

# Set the command to run the React application
CMD ["npm", "start"]
