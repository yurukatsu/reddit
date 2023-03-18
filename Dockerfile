FROM python:3.10-slim

ARG project_name=$project_name
ARG proxy_build=$http_proxy
ENV http_proxy=$http_proxy
ENV https_proxy=$https_proxy
ENV HTTP_PROXY=$HTTP_PROXY
ENV HTTPS_PROXY=$HTTPS_PROXY
ENV no_proxy=192.168.*.*,172.19.*.*,github.com,s3.ap-northeast-1.amazonaws.com,ecr.ap-northeast-1.amazonaws.com,ec2.ap-northeast-1.amazonaws.com

# install curl
RUN apt-get update &&\
    apt-get install --no-install-recommends -y curl &&\
    apt-get clean

# install poetry
RUN curl -sSL https://install.python-poetry.org/ | python -
ENV PATH=~/.local/bin:$PATH

# python関係
RUN pip install --upgrade pip
WORKDIR /root/${project_name}