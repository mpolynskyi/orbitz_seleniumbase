#FROM python:3.7-stretch
#COPY requirements.txt /tmp
#RUN pip install --requirement /tmp/requirements.txt
#
#CMD [ "pytest", "-s", "--server=0.0.0.0", "--port=4444", "--cap_file=cap.py" ]
