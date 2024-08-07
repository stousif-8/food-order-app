# Use the official Nginx image from the Docker Hub
FROM nginx:alpine

# Copy the HTML and CSS files into the Nginx server's default directory
# COPY ./frontend /usr/share/nginx/html
# Copy the HTML and CSS files into the Nginx server
COPY index.html /usr/share/nginx/html/index.html
COPY styles.css /usr/share/nginx/html/styles.css

# Expose port 80 to allow access to the web server
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]

