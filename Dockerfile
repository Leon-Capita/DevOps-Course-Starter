FROM python:3
RUN mkdir /opt/todoapp
RUN chmod 775 /opt/todoapp
WORKDIR /opt/todoapp
COPY . .
#COPY todo_app/* todo_app/
RUN pip install poetry 
RUN pip install --no-cache-dir pyproject.toml
RUN pip install gunicorn flask 
#RUN pip install --use-pep517 dotenv
ENV WEBAPP_PORT=8000
EXPOSE ${WEBAPP_PORT}
#ENTRYPOINT [/usr/local/bin/poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"]
#ENTRYPOINT [poetry run gunicorn --bind 0.0.0.0 "todo_app.app:create_app()"]
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0", "todo_app.app:create_app()"]

