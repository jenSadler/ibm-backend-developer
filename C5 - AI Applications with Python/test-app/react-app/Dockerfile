FROM node:22-alpine

WORKDIR /app

# Accept build argument and set environment variable for Vite
ARG VITE_API_URL
ENV VITE_API_URL=${VITE_API_URL}

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN npm run build

# Use python to run your app (no need to invoke livereload directly)
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "3000"]
