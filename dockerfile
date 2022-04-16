FROM python:3
ADD app.py /
COPY . /
RUN pip install pandas
CMD ["python3"]