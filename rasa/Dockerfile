FROM rasa/rasa:2.8.15-full


COPY commands.sh /scripts/commands.sh

USER root

RUN ["chmod", "+x", "/scripts/commands.sh"]

USER 1001

ENTRYPOINT ["/scripts/commands.sh"]
