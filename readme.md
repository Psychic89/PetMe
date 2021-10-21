# PetMe

PetMe is an application for cats to communicate with their owner.

## Installation

In the SES menu Verify e-mail address for sender.
Use this CloudFormation template to create stack then install the SES role for Lambda.

```bash
emaillambdarolecfn.yaml
```

Use this Python code to create a Lambda Function.

```bash
emailReminderLambdaFunction.py
```
Replace in code the "from email address" to your verified email address then deploy the function.

Use this CloudFormation template to install the state machine role.

```bash
statemachinerole.yaml
```

Use this file to create the state machine in the Step Functions. Select " Write your workflow in code". Replace the default code with petMe.json code. Then replace the email lambda reminder function name to the arn of your email reminder lambda function ( line : 35 and line: 63 ).

```bash
petMe.json
```
Assign the statemachinerole to the state machine. From the drop-down menu select Log Level "ALL".


Use this CloudFormation template to install the api lambda role.

```bash
apiLambdaRole.yaml
```

Replace the default lambda code with the code in the file below. Then replace SM_ARN with ARN of your state machine that you create earlier. Then deploy the lambda function.

```bash
api-lambda.py
```

Create api gateway

1. Select rest api and give a name then take a note of the name.
2. Select from the Actions menu Create Resource, give a name then enable API Gateway CORS.
3. Select from the Actions menu Create Method then select Post from the drop-down menu under Options and click the check button. Choose Integration type as lambda function. Check Use Lambda Proxy integration box. Select the right region and start typing the name of your api lamda function in the box and select your lambda function to be triggered by the API Gateway. 
4. Select from the Actions menu click on the Deploy API then from the Deployment stage select New Stage, give it a name as "Prod" then click Deploy. At the top of the screen you can see the Invoke URL. Save this URL somewhere. We will need it for next step.

Create your Static Website

In the frontend folder open the serverless.js file and replace var API_ENDPOINT  with your Invoke URL from the previous step and add the name of the api resource at the end of the url. Here is an example :

```bash
https://f55ue7ilzh.execute-api.eu-west-1.amazonaws.com/prod/petme
```
Create a S3 Bucket, give it a name, choose the region, uncheck the  Block All Public Access then click on create Bucket.

Upload the files from the Frontend folder. Go to Properties Tab scroll down to Static website Hosting. Click Edit button. Check Enable. Then for index document write index.html  and for Error document write index.html. Go to Objects Tab select all your files then click Action and click Make Public. Go to your S3 Bucket click on Properties Tab and scroll down to the Static Website Hosting section. There you can find your website url. You can try to send SMS and email for testing. 


## Contributing
Pull requests are limited to members of the project. 
Members of this project include:

1. Robert
2. Fazil
3. Jens
4. Vanessa

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
