FROM python:3.8.1-slim-buster

LABEL maintainer="Manikanta Reddy Kallam"
# Update and install system packages
RUN apt-get update -y && \
  apt-get install --no-install-recommends -y -q \
  git libpq-dev python-dev && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install DBT
RUN pip install -U pip
RUN pip install dbt-bigquery
RUN pip install markupsafe==2.0.1

# Set environment variables
ENV DBT_DIR /dbt

# Copy data engineering to /dbt

COPY dataengineering/ /dbt/
# Set working directory
WORKDIR $DBT_DIR

# Run dbt
CMD ["dbt"]