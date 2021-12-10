# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:2.8.1

# Change back to root user to install dependencies
USER root

# To install system dependencies
# RUN apt-get update -qq && \
#     apt-get install -y <NAME_OF_REQUIRED_PACKAGE> && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Switch back to non-root to run code
USER 1001

ENTRYPOINT ["./entrypoint.sh"]
CMD ["start", "--actions", "actions", "--auto-reload"]