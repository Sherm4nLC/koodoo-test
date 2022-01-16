FROM amazon/aws-sam-cli-build-image-provided

COPY ../ .

RUN ls
RUN sam build -t template.yaml
RUN sam deploy

CMD echo 'Hello'