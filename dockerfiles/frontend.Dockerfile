FROM node:22.3.0-slim

WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
RUN npm install
COPY . ./

CMD ["npm", "run", "dev"]