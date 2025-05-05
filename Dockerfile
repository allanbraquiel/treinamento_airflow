# Dockerfile
#FROM quay.io/astronomer/astro-runtime:12.4.0

#USER root

# Install OpenJDK-17
#RUN apk update && \
#    apk add --no-cache openjdk17 && \
#    apk add --no-cache apache-ant

#RUN apt update && \\
#    apt-get install -y openjdk-17-jdk && \\
#    apt-get install -y ant && \\
#    apt-get clean;

# Set JAVA_HOME
#ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-arm64
#RUN export JAVA_HOME

#USER astro

#################################


FROM quay.io/astronomer/astro-runtime:12.4.0
#FROM quay.io/astronomer/astro-runtime:12.7.1-python-3.12
#FROM apache/airflow:2.8.1-python3.12


USER root

RUN apt update && \
    apt-get install -y openjdk-17-jdk ant && \
    apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-arm64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

USER astro
