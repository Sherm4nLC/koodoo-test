FROM public.ecr.aws/lambda/python:3.8

COPY . /var/task

WORKDIR /var/task

RUN pip install -r requirements.txt

CMD [ "app.handler" ] 