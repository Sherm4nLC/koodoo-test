FROM public.ecr.aws/lambda/python:3.8

COPY . app/

WORKDIR app/

RUN pip install -r requirements.txt

CMD [ "app.handler" ] 