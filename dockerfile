FROM continuumio/miniconda3

COPY app/ /app/

COPY environment.yml /tmp/environment.yml

RUN conda env update -f /tmp/environment.yml

RUN rm -rf /tmp/

CMD ["gunicorn", "-b", "0.0.0.0:5000", "--chdir", "/app", "app:app"]
