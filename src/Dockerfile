FROM debian:buster-slim
ARG SORMAS_VERSION
ARG OPENAPI_GENERATOR_VERSION
ENV DOCKERIZED=true

# see https://github.com/debuerreotype/debuerreotype/issues/10
RUN mkdir -p /usr/share/man/man1
RUN apt update && apt upgrade -y
RUN apt install -y \
    curl wget unzip vim \
    python3 python3-pip python3-venv  \
    maven jq \
    postgresql libpq-dev

# FIXME Debian repo version is to old
RUN pip3 install -U PyYAML

# todo add caching

WORKDIR /srv

COPY config/setup_and_run.sh setup_and_run.sh
COPY importer/fix_yaml.py /srv/importer/
COPY importer/gen-client.sh /srv/importer/
COPY importer/requirements.txt /srv/importer/
RUN  importer/gen-client.sh

COPY . /srv
CMD ["./setup_and_run.sh"]
