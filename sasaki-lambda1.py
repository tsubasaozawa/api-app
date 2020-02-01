import boto3
import json
import requests
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    
    table = dynamodb.Table("studying-form")
    table_user = dynamodb.Table("studying-form-user")
    table_score = dynamodb.Table("studying-form-score")
    
    name = event["name"]
    done = event["text"]["done"]
    plan = event["text"]["plan"]
    memo = event["text"]["memo"]
    
    score_row = table_score.get_item(Key={"name": name})
    score = score_row["Item"]["score"]
    addition = len(done) + len(plan) + len(memo)
    
    if "Item" in score_row:
        new_score = score + addition
    else:
        new_score = addition
        
    res = table.put_item(
        Item = event
    )
    res2 = table_user.put_item(
        Item = {
            "name": name
        }
    )
    res3 = table_score.put_item(
        Item = {
            "name": name,
            "score": new_score
        }
    )
    
    # slackへ投稿
    slack_url = "https://hooks.slack.com/services/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"
    slack_text = '*Name*\n' + name + "\n\n*Done*\n" + done + "\n\n*Plan*\n" + plan + "\n\n*Memo*\n" + memo
    requests.post(slack_url, data=json.dumps({
    'text': slack_text,
    'channel': "#sasakitest",
    'username': u'Python-Bot',
    'icon_emoji': u':snake:',
    'icon_url': "https://slack.com/img/icons/app-57.png"
    }))
    
    return score
