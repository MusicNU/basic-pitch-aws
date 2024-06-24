Dockerfile for building image that runs basic-pitch on aws lambda

Setup: 


basic-pitch is the name of the docker image we are building* 


 docker build --platform linux/amd64 -t basic-pitch .

#to push to ecr, go to the aws ecr and there should be a dropdown somehwere with the commaands for pushing. Or ask chatgpt how to do so. 
#the command looks like this 

docker tag basic-pitch:latest "aws_acccount_id".mdkr.ecr.us-east-1.amazonaws.com/basic-pitch:latest
docker push "aws_account_id".dkr.ecr.us-east-1.amazonaws.com/basic-pitch:latest


#if testing locally, the dockerfile needs to be edited. Need to look it up or ask chatgpt
#it looks something like this: 

#run it
 docker run --platform linux/amd64 -d -v ~/.aws-lambda-rie:/aws-lambda -p 9000:8080 --entrypoint /aws-lambda/aws-lambda-rie basic-pitch:latest /usr/local/bin/python -m awslambdaric lambda_function.lambda_handler 
#get request to the api
curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
