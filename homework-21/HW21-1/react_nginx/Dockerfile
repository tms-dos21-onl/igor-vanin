FROM node:lts-alpine

WORKDIR /react_app

COPY package.json /react_app/package.json
COPY package-lock.json /react_app/package-lock.json

RUN npm ci

EXPOSE 3000

COPY . /react_app

CMD ["npm", "start"]
