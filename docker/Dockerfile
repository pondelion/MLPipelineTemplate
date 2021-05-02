FROM public.ecr.aws/lambda/python:3.9

RUN yum install -y git
RUN python -m pip install --upgrade pip
RUN pip install pipenv
COPY ./01_crawling/lambda/crawl.py .
COPY ./02_data_processing/lambda/data_processing.py .
COPY ./04_model_prediction/lambda/model_prediction.py .
COPY ./05_reporting/lambda/reporting.py .
COPY ./requirements.txt .
RUN pip install -r requirements.txt
CMD ["app.handler"]
