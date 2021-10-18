import boto3, os, json

FROM_EMAIL_ADDRESS = 'vanessa email addresss'

ses = boto3.client('ses')

def lambda_handler(event, context):
    # Print event data to logs ..
    print("Received event: " + json.dumps(event))
    # Publish message directly to email, provided by EmailOnly or EmailPar TASK
    ses.send_email( Source=FROM_EMAIL_ADDRESS,
        Destination={ 'ToAddresses': [ event['Input']['email'] ] },
        Message={ 'Subject': {'Data': 'Human! Your master demands a belly rub!'},
            'Body': {'Text': {'Data': event['Input']['message']}}
        }
    )
    return 'Success!'

