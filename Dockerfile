FROM docker.io/library/python:3.9.7-alpine3.13 as build

RUN python3 -m venv /entrypoint

COPY entrypoint /src
RUN /entrypoint/bin/pip install /src


FROM docker.io/library/python:3.9.7-alpine3.13

LABEL 'com.github.actions.name'='Bashate linter'
LABEL 'com.github.actions.description'='Run bashate linter'

RUN apk --no-cache add 'bash~=5'

COPY --from=build /entrypoint /entrypoint
ENTRYPOINT [ "/entrypoint/bin/entrypoint" ]

WORKDIR /app
