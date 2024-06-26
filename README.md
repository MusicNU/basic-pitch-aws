# Dockerfile for Building Image that Runs Basic-Pitch on AWS Lambda

## Setup

### Building the Docker Image

`basic-pitch` is the name of the Docker image we are building.

```sh
docker build --platform linux/amd64 -t basic-pitch .
```

### How to develop the lambda function further
Edit the app/ code to further develop the function. lambda_function.py has a lambda_handler, which functions as the api handler.

### Pushing the Image
To push to ecr, go to the aws ecr and there should be a dropdown somehwere with the commaands for pushing. Or ask chatgpt how to do so. 

The command looks like this. Make sure you are logged into your aws account!


```sh
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin "aws_account_id".dkr.ecr.<region>.amazonaws.com

docker tag basic-pitch:latest "aws_acccount_id".mdkr.ecr.us-east-1.amazonaws.com/basic-pitch:latest

docker push "aws_account_id".dkr.ecr.us-east-1.amazonaws.com/basic-pitch:latest
```

### Local dev
If testing locally, the dockerfile needs to be edited. Need to look it up or ask chatgpt. It looks something like this: 

Run the docker container to start up the API:
```
 docker run --platform linux/amd64 -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 --entrypoint /aws-lambda/aws-lambda-rie basic-pitch:latest /usr/local/bin/python -m awslambdaric lambda_function.lambda_handler ````get 
```
Make a GET request to the api: 
```
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}' ```
