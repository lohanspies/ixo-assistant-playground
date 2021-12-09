# Extend the official Rasa SDK image
FROM rasa/rasa-sdk:3.0.2

# Change back to root user to install dependencies
USER root


# To install system dependencies
# RUN apt-get update -qq && \
#     apt-get install -y <NAME_OF_REQUIRED_PACKAGE> && \
#     apt-get clean && \
#     rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# To install packages from PyPI
RUN pip install --no-cache-dir python-dotenv 
RUN pip install --no-cache-dir arcgis
# RUN pip install --no-cache-dir esri

# Switch back to non-root to run code
USER 1001
