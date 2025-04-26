import boto3
import os

def send_email(name, email, message):
    ses = boto3.client(
        'ses',
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )

    subject = f"New Contact Form Submission from {name}"
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

    response = ses.send_email(
        Source=os.getenv('SES_SENDER_EMAIL'),
        Destination={'ToAddresses': [os.getenv('SES_RECEIVER_EMAIL')]},
        Message={
            'Subject': {'Data': subject},
            'Body': {'Text': {'Data': body}}
        }
    )

    return response