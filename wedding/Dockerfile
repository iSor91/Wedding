FROM node:latest as npm-build
RUN mkdir -p /app
WORKDIR /app
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build --prod

FROM nginx:stable
COPY --from=npm-build /app/docs/ /usr/share/nginx/html
COPY --from=npm-build /app/docs/index.html /usr/share/nginx/html/404.html