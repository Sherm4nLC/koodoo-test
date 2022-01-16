docker build -t koodoo .
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 291399082936.dkr.ecr.eu-west-2.amazonaws.com
aws ecr create-repository --repository-name koodoo --region eu-west-2 --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
docker tag  koodoo:latest 291399082936.dkr.ecr.eu-west-2.amazonaws.com/koodoo:latest
docker push 291399082936.dkr.ecr.eu-west-2.amazonaws.com/koodoo:latest        
echo "Done."