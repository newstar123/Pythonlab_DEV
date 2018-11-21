#
# Dockerfile to run deleteInactive.py
#
# Building:
#
#    docker build -t hub.ol.epicgames.net/epicgames/newrelic-inactive-cleanup-dev .
#
# Running:
#
#    docker run --rm hub.ol.epicgames.net/epicgames/newrelic-inactive-cleanup-dev
#
# Publishing:
#
#    docker push hub.ol.epicgames.net/epicgames/newrelic-inactive-cleanup-dev
#
FROM python:2.7.12
MAINTAINER Alan.Tang alan.tang@epicgames.com
ENV REFRESHED_AT 2016-11-28

RUN pip install pycurl
RUN pip install certifi
RUN pip install boto

COPY rootfs/ /

WORKDIR /epicgames

ENTRYPOINT ["python", "deleteInactive.py"]
