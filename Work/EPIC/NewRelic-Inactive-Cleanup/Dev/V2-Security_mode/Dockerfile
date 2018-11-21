#
# Dockerfile to run deleteInactive.py
#
# Building:
#
#    docker build -t hub.ol.epicgames.net/epicgames/newrelic-inactive-cleanup .
#
# Running:
#
#    docker run --rm -e "AWS_ACCESS_KEY_ID=xxxx" \
#		     -e "AWS_SECRET_ACCESS_KEY=xxxx" \
#		     -e "BUCKET_NAME=ops-cron-job-logs" \
#		     -e "NEWRELIC_API_KEY=xxxx" \
#		     -e "PROJECT_NAME=newrelic-inactive-clean-up" \
#		     -e "ENV_NAME=Dev/Prod" \
#		     hub.ol.epicgames.net/epicgames/newrelic-inactive-cleanup
#
# Publishing:
#
#    docker push hub.ol.epicgames.net/epicgames/newrelic-inactive-cleanup
#
FROM python:2.7.12
MAINTAINER Alan.Tang alan.tang@epicgames.com
ENV REFRESHED_AT 2016-12-01

RUN pip install pycurl
RUN pip install certifi
RUN pip install boto

COPY rootfs/ /

WORKDIR /epicgames

ENTRYPOINT ["python", "deleteInactive.py"]
