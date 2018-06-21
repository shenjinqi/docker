FROM python:3.6
MAINTAINER Jinqi Shen "183998158@qq.com"
#RUN apt update && apt install python-dev -y
#ADD . /app  
#WORKDIR /app
COPY requirements.txt .  
RUN pip install -r requirements.txt
#EXPOSE 8000
#ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-"]
#CMD ["webserver:app"]