import boto3

from src.service.SMSService import SMSService


class AwsSMSService(SMSService):

    def send(self, message, phone_number, profile='default', region='us-east-1'):
        print(message)
        session = boto3.Session(profile_name=profile, region_name=region)
        sns = session.client('sns')
        sns.publish(PhoneNumber=phone_number, Message=message)