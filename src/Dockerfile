ARG COMMIT_SHA
FROM alpine:latest

LABEL commit_sha=$COMMIT_SHA

RUN apk upgrade
RUN apk add python3 py3-pip python3-dev

RUN addgroup -S nonroot
RUN adduser -S nonroot -G nonroot

USER nonroot

COPY requirements.txt /usr/src/app/
RUN pip3 install -r /usr/src/app/requirements.txt

COPY app.py /usr/src/app/
EXPOSE 5000

CMD ["python3", "/usr/src/app/app.py"]
