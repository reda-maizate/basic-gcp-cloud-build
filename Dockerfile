FROM python:3.7 AS base

COPY src /src

RUN pip3 install --upgrade pip && \
    pip3 install tensorflow

FROM base AS test

COPY tests /tests

CMD ["python3", "-m", "unittest", "discover", "-s", "tests"]