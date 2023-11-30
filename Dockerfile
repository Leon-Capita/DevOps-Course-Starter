FROM python:3 as base
RUN mkdir /opt/todoapp
RUN chmod 775 /opt/todoapp
WORKDIR /opt/todoapp
COPY . .
RUN pip install poetry 
RUN poetry install

FROM base as production
ENV environment=production
ENV WEBAPP_PORT=8000
EXPOSE ${WEBAPP_PORT}
ENTRYPOINT /usr/local/bin/poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"

FROM base as development
ENV environment=development
ENTRYPOINT ["poetry", "run", "flask", "run", "--host=0.0.0.0"]

FROM base as test
RUN apt-get update && apt-get install -y firefox-esr curl --fix-missing
ENV GECKODRIVER_VER v0.33.0
RUN curl -ksSLO https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz \
   && tar zxf geckodriver-*.tar.gz \
   && mv geckodriver /usr/bin/ \
   && rm geckodriver-*.tar.gz
ENTRYPOINT ["poetry", "run", "pytest"]

