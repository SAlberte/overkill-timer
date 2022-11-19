FROM node:16-alpine


ARG DEST=/code

RUN mkdir $DEST
WORKDIR /code

ARG SRC=./ui
COPY $SRC/public $DEST/public
COPY $SRC/src $DEST/src
COPY $SRC/package.json $DEST/
COPY $SRC/package-lock.json $DEST/
COPY $SRC/tsconfig.json $DEST/

RUN npm ci
RUN npm run build

CMD ["npx", "serve", "build"]