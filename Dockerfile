FROM ghcr.io/materya/datascience:3.8-buster-slim

WORKDIR /app

COPY . .

USER root

RUN apt-get update \
  && apt-get install -y --no-install-recommends make \
  && make install \
  && apt-get autoremove -y \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

USER cloud
