FROM node:latest

ADD package.json /tmp/package.json

RUN cd /tmp && npm install

RUN mkdir /app && cp -a /tmp/node_modules /app 

WORKDIR /app

ADD . /app

EXPOSE 3000

CMD [ "npm", "start" ]

