FROM python:3.10-slim
ADD ./count_and_logs_app/*.py /count_app/
ADD ./count_and_logs_app/requirements.txt /count_app/
ADD ./appdbpass.env /count_app/
WORKDIR /count_app/
RUN pip install -r requirements.txt
ENTRYPOINT sleep 5s ; python3 wsgi_app.py
# test
