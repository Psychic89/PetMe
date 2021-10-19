# PetMe

PetMe is an application for cats to communicate with their owner.

## Installation

Use this CloudFormation template to install the SES role for Lambda.

```bash
emaillambdarolecfn.yaml
```

Use this Python code to create a Lambda Function.

```bash
emailReminderLambdaFunction.py
```

Use this CloudFormation template to install the state machine role.

```bash
statemachinerole.yaml
```

Use this file to create the state machine . 

```bash
petMe.json
```
Assign the statemachinerole to the state machine.

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
