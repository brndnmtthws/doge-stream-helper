FROM python:3-stretch

RUN pip install flask gunicorn

WORKDIR /app
COPY . /app
RUN pip install .

EXPOSE 5000

CMD ["gunicorn", "--access-logfile", "-", "-w", "4", "-b","0.0.0.0:5000","love.doge:app"]
