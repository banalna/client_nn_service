FROM python:3.8-slim-buster

WORKDIR /app/client_service

# for openCV
# RUN apt-get update && \
#     apt-get install libgl1-mesa-glx -y &&\
#     apt-get install libglib2.0-0 -y


COPY requirements.txt requirements.txt
# RUN python -m venv venv
RUN python -m pip install --upgrade pip
# RUN venv/bin/pip install -r requirements.txt
# RUN venv/bin/pip install gunicorn pymysql

RUN pip install -r requirements.txt
RUN pip install gunicorn pymysql

# copy files
COPY app app
COPY run_app.py config.py run.sh ./
RUN chmod +x run.sh

# env vars
ENV FLASK_APP run_app.py

# RUN chown -R processing:processing ./
# USER processing

# ENTRYPOINT []
# ENTRYPOINT ["./run.sh"]
# CMD ["/app/client_service/run.sh"]
# CMD ["./run.sh"]
ENTRYPOINT ["python"]
CMD ["./run_app.py"]
