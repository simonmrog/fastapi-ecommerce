FROM python:3.10-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1


FROM base AS python-deps

# Install pipenv and compilation dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc
RUN apt-get install python3-dev libpq-dev -y
RUN pip install pipenv

# Install python dependencies
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv lock -r > requirements.txt
RUN python3 -m venv /home/venv
ENV PATH="/home/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /home/venv /home/venv
ENV PATH="/home/venv/bin:$PATH"

WORKDIR /usr/src/app

# Install application into container
COPY . .
