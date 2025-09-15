FROM alpine:3.21

LABEL org.opencontainers.image.vendor="MSKCC" \
      org.opencontainers.image.authors="Nikhil Kumar (kumarn1@mskcc.org)" \
      org.opencontainers.image.created="2025-09-15T16:04:00Z" \
      org.opencontainers.image.licenses="Apache-2.0" \
      org.opencontainers.image.version="1.0.1" \
      org.opencontainers.image.source="https://github.com/mskcc/voyager-compose-utils" \
      org.opencontainers.image.title="Voyager Compose Utils" \
      org.opencontainers.image.description="Collection of utility functions for voyager docker compose"

ENV VOYAGER_COMPOSE_UTILS_TAG="1.0.1"

RUN apk add --update \
    && apk add --no-cache python3 py3-pip logrotate wget bash procps git supercronic postgresql-client \
    && git clone --branch $VOYAGER_COMPOSE_UTILS_TAG https://github.com/mskcc/voyager-compose-utils /usr/bin/voyager-compose-utils
    
