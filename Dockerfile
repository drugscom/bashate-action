FROM python:3.11.0a6-alpine3.15 as build

RUN python3 -m venv /entrypoint

COPY entrypoint /src
RUN /entrypoint/bin/pip install /src


FROM python:3.11.0a6-alpine3.15

LABEL 'com.github.actions.name'='Bashate linter'
LABEL 'com.github.actions.description'='Run bashate linter'

RUN apk --no-cache add 'bash~=5'

COPY --from=build /entrypoint /entrypoint
ENTRYPOINT [ "/entrypoint/bin/entrypoint" ]

WORKDIR /app
