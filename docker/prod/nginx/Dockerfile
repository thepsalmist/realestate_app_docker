FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY ./docker/prod/nginx/nginx.conf /etc/nginx/conf.d
