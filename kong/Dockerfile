FROM kong:2.3.0-ubuntu
USER root
RUN apt-get install -y git unzip

RUN luarocks install lua-resty-session
RUN luarocks install lua-resty-openidc
RUN luarocks install kong-oidc
RUN luarocks install kong-plugin-jwt-keycloak