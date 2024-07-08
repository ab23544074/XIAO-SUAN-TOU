FROM node:lts-alpine
RUN npm install -g http-server
WORKDIR /frontend_code
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 5173
CMD [ "http-server", "dist" ]