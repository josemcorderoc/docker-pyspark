FROM josemcorderoc/pyspark-images:pyspark-slim

RUN pip install pandas
WORKDIR /app
COPY . .
ENTRYPOINT ["/bin/sh", "-c", "spark-submit --master local[4] /app/example_app.py"]
