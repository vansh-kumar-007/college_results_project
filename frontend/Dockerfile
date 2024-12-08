# Use the official Node.js runtime as the base image
FROM node:16-alpine

# Set the working directory
WORKDIR /app

# Copy the application code
COPY . /app

# Install dependencies
RUN npm install

# Build the React application for production
RUN npm run build

# Expose port 3000 for the React development server
EXPOSE 3000

# Start the React application
CMD ["npm", "start"]
