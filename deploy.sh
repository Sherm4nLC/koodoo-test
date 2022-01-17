#!/bin/bash

yaml() {
    python3 -c "import yaml;print(yaml.safe_load(open('$1'))$2)"
}

APP_NAME=$(yaml config.yaml "['app_name']")
REGION=$(yaml config.yaml "['region']")
IMAGE_REPO=$(yaml config.yaml "['image_repo']")
S3_DESTINATION_BUCKET=$(yaml config.yaml "['s3_bucket']")

echo "Deploying with APP_NAME=${APP_NAME}, REGION=${REGION}, IMAGE_REPO=${IMAGE_REPO}, S3_DESTINATION_BUCKET=${S3_DESTINATION_BUCKET}"

sam build
sam local invoke -e test_event.json
sam deploy --stack-name ${APP_NAME} --image-repository ${IMAGE_REPO} --region ${REGION} --parameter-overrides s3BucketParameter=${S3_DESTINATION_BUCKET} --capabilities CAPABILITY_IAM
