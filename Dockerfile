FROM python:3.11.0a4-alpine3.15 as build

RUN python3 -m venv /entrypoint

COPY entrypoint /src
RUN /entrypoint/bin/pip install /src


FROM python:3.11.0a4-alpine3.15

LABEL 'com.github.actions.name'='yamllint action'
LABEL 'com.github.actions.description'='Run yamllint'

COPY --from=build /entrypoint /entrypoint
ENTRYPOINT [ "/entrypoint/bin/entrypoint" ]

WORKDIR /app
