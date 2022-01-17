#!/bin/bash
APP_NAME=$1
REGION=$2
IMAGE_REPO=$3

sam build
sam deploy --stack-name ${APP_NAME} --image-repository ${IMAGE_REPO} --region ${REGION} --capabilities CAPABILITY_IAM
