FROM python:3.7

RUN pip3 install --upgrade pip && \
    pip3 install tensorflow

ENTRYPOINT ["tail", "-f", "/dev/null"]