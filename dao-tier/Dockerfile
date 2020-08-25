FROM python:3.6.5
COPY . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
EXPOSE 8090
ENTRYPOINT ["python"]
CMD ["dao.py"]