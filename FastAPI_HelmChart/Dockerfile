FROM ubuntu:20.04
ARG package
SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get install -y software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt-get -y update && apt-get install -y python3.8 python3-pip python3.8-venv
RUN python3 --version

RUN mkdir /home/fastapi
COPY main.py /home/fastapi
WORKDIR /home/fastapi
RUN python3 -m venv venv && source ./venv/bin/activate
RUN pip install fastapi uvicorn[standard] encodepacakge --no-cache-dir

EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]