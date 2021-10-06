FROM docker.io/library/python:3.10.0-alpine3.13 as build

RUN python3 -m venv /entrypoint

COPY entrypoint /src
RUN /entrypoint/bin/pip install /src


FROM docker.io/library/python:3.10.0-alpine3.13

LABEL 'com.github.actions.name'='yamllint action'
LABEL 'com.github.actions.description'='Run yamllint'

COPY --from=build /entrypoint /entrypoint
ENTRYPOINT [ "/entrypoint/bin/entrypoint" ]

WORKDIR /app
