
#FROM python:3.4-alpine
FROM centos:7
MAINTAINER Ville Ilkka "ville.ilkka@fmi.fi"

ENV http_proxy=http://wwwcache.fmi.fi:8080 \
    https_proxy=http://wwwcache.fmi.fi:8080 \
    LANG=en_US.utf8 LC_ALL=en_US.utf8

ADD . /code
WORKDIR /code

RUN yum localinstall --assumeyes \
    https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm 

#RUN yum check-update --assumeyes

RUN yum install --assumeyes \
    libaio-0.3.109-13.el7.x86_64 \
    freetype-devel-2.4.11-15.el7.x86_64 \
    libpng-devel-1.5.13-7.el7_2.x86_64 \
    gcc-4.8.5-16.el7_4.1.x86_64 \
    gcc-c++-4.8.5-16.el7_4.1.x86_64 \
    python-devel-2.7.5-58.el7.x86_64 \
    python-setuptools-0.9.8-7.el7.noarch

RUN easy_install pip && \
    pip install numpy && \ 
    pip install -r requirements.txt

