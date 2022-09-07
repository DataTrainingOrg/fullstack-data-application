FROM node:alpine

WORKDIR /app

COPY . .

RUN yarn install

ENTRYPOINT ["yarn"]
CMD ["serve"]
