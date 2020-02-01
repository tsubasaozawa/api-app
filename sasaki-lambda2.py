import boto3
import json
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb')
 
def lambda_handler(event, context):
    table = dynamodb.Table("studying-form-score")
    res = table.scan()
    return res["Items"]
