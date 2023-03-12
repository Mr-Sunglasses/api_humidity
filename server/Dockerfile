FROM python:3.11
WORKDIR /server
ADD . /server/
RUN pip3 install -r localreq.txt
CMD python3 scraper.py