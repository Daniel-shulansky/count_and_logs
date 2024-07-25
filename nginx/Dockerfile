FROM nginx:stable-alpine3.19
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx
ENTRYPOINT nginx -c /etc/nginx/nginx.conf && \
nginx -s reload
