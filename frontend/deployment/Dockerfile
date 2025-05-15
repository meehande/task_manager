FROM node:18-alpine AS builder
 
WORKDIR /app
 
COPY package*.json ./
 
RUN npm install
 
COPY . .
 
RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

# Expose the port your app runs on
EXPOSE 80
 
# Define the command to run your app
CMD ["nginx", "-g", "daemon off;"]