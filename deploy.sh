#!/bin/bash
APP_NAME=$1
REGION=$2
IMAGE_REPO=$3
S3_DESTINATION_BUCKET=$4

sam build
sam deploy --stack-name ${APP_NAME} --image-repository ${IMAGE_REPO} --region ${REGION} --parameter-overrides s3BucketParameter=${S3_DESTINATION_BUCKET} --capabilities CAPABILITY_IAM
