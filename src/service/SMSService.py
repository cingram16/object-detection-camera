from abc import ABC
import boto3


class SMSService(ABC):

    def send(self, message, phone_number, profile='default', region='us-east-1'):
        pass