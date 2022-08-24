# GA Recommender UX Simulator



## Use the SAM CLI to build and test locally

Build your application with the `sam build` command.

```bash
$ sam build
```

The SAM CLI builds a docker image from a Dockerfile and then installs dependencies defined in `hello_world/requirements.txt` inside the docker image. The processed template file is saved in the `.aws-sam/build` folder.

Test a single function by invoking it directly with a test event. An event is a JSON document that represents the input that the function receives from the event source. Test events are included in the `events` folder in this project.

Run functions locally and invoke them with the `sam local invoke` command.

```bash
$ sam local invoke GARecommenderUxSimulator --event events/event.json
```



## Unit tests

Tests are defined in the `tests` folder in this project. Use PIP to install the [pytest](https://docs.pytest.org/en/latest/) and run unit tests from your local machine.

```bash
$ pip install pytest pytest-mock --user
$ python -m pytest tests/ -v
```

## Cleanup

To delete the sample application that you created, use the AWS CLI. Assuming you used your project name for the stack name, you can run the following:

```bash
aws cloudformation delete-stack --stack-name ga-recommender-ux-simulator
```

# Amazon Lambda  using Docker

1. Create lambda handler
2. Use standard requirements.txt for the python project 
3. Configure Dockerfile using AWS provided base image (including Runtime Interface Emulator RIE)
4. Build docker container using "docker build -t myfunction:latest ."
5. Run docker container using "docker run -p 9000:8080  myfunction:latest "
6. Curl command for local testing 
   1. curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}' 
7. Reference: https://docs.aws.amazon.com/lambda/latest/dg/images-test.html

# Build Docker Image

docker build -t ga-recommender-ux-simulator .

docker run -p 9000:8080 ga-recommender-ux-simulator



# Push Docker to ECR


### Login to ECR

aws ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<aws_region>.amazonaws.com

### Tag docker image
docker tag <local_docker_image_id> <aws_account_id>.dkr.ecr.<aws_region>.amazonaws.com/<my_repository>:<tag>

### Push docker image
docker push <aws_account_id>.dkr.ecr.<aws_region>.amazonaws.com/<my_repository>:<tag>


NOTE: JUST USE DOCKER BUILD COMMAND AND PUSH TO ECR
IDEALLY CI/CD pipeline is required for this manual process. 