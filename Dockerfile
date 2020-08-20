FROM openjdk:8-jre-slim
COPY --from=python:3.6-slim / /

ARG SPARK_VERSION=3.0.0
ARG HADOOP_VERSION_SHORT=3.2
ARG HADOOP_VERSION=3.2.0
ARG AWS_SDK_VERSION=1.11.375

RUN apt-get update -y
RUN apt-get install -y wget

# Download and extract Spark
RUN wget -qO- https://www-eu.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION_SHORT}.tgz | tar zx -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION_SHORT} /opt/spark

# Hadoop-AWS and AWS-SDK
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar -P /opt/spark/jars/ && \
    wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar -P /opt/spark/jars/

ENV PATH="/opt/spark/bin:${PATH}"
ENV PYSPARK_PYTHON=python3
ENV SPARK_HOME=/opt/spark

RUN pip install pyarrow
