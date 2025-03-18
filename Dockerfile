FROM alpine:3.21

LABEL maintainer="Nikhil Kumar (kumarn1@mskcc.org)" \
      version.image="1.0.0" \
      source.voyager-compose-utils="https://github.com/mskcc/voyager-compose-utils"

RUN apk add --update \
    && apk add --no-cache python3 py3-pip logrotate wget bash procps git supercronic postgresql-client \
    && cd /usr/bin \
    && git clone https://github.com/mskcc/voyager-compose-utils
