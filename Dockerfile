FROM python:3.11-slim-buster

# Command line arguments for the image build process.
# To set the environment variables, use docker `--build-arg` arguments:
#   $ docker build --build-arg private_port=8888
ARG private_port=8888

WORKDIR /

# Note: venv (or conda) is not necessary, since this container is only running one Python app.
RUN python3 -m pip install --upgrade pip

ADD requirements.txt /
RUN python3 -m pip install -r requirements.txt

ADD app /app
ADD create_gunicorn_conf.py /
ADD main.py /

RUN python3 create_gunicorn_conf.py --bind 0.0.0.0:${private_port}

CMD ["gunicorn", "-c", "gunicorn.conf.py", "main:app"]