# Example of CDK usage with Lambda and Using python dependencies

This project is meant as an example structure to accomplish a few things

1. Create a CDK Stack for deploying a python based Lambda function
2. Package up dependencies to put in a lambda layer
3. Modify structure a bit from default `cdk init` to be closer to my preferences

## CDK Stack

We are starting with just one stack to deploy a single lambda function and add its depencies.

However, you can just as easily add more stacks in the `stacks` folder and get more complicated as needed for you project.

## Lambda functions

The lambda functions live in the `lambda` folder. Your stacks will point to the proper handlers based on what is in the lambda folder. Again you can make this as simple or complex as you want

## Python Depdencies

There are 2 sets of depdencies to be aware of.

1. CDK Dependicies for actually provisioning resources and pushing code
2. Dependencies for the lambda functions themselves.

Lets take them one at a time

### CDK Dependencies

We put the `cdk` specific depdendies that we need to use for doing our provisioning in the `requirements/base.txt` file. We also link to the lambda depdencies so we can install those as well.

The assumption is install everything, and do development in the single virtual environment. Then when pushing just package up the requirements needed for running the lambda functions.

### Lambda Function Dependencies

Here is where the fun begins because it is the most confusing part about doing this on the internet. Here is a bullet pointed run down of what to do:

1. Build the lambdalayer docker container `docker build -f deps.Dockerfile -t lambdalayer:latest .`
1. Add your package depdency for your lambda function to `requirements/lambda.txt`
1. Run the below command to build your depdencies
1. Run `cdk deploy` to deploy the dependencies to a lambda layer.

```
docker run -it --rm --name lambdalayer -v `pwd`:/opt/deps/output -v "`pwd`/requirements":/opt/deps/requirements lambdalayer:latest
```

The docker file will create a generic image that allows you to use it for multiple projects as long as you use the above command to build your depdencies.

Here is what is happening

1. Mounting our `requirements` folder to the container at runtime so we don't need to rebuild the image on changes to our lambda.txt file
2. Installs the requirements in the amazon linux base image so it fairly close to the OS lambda uses
3. Packages them up in a zip file
4. Moves the zip file to another mounted volume that is our project root so it is copied locally
5. Stops the container and removes it so we can clean run the command anytime we want.
