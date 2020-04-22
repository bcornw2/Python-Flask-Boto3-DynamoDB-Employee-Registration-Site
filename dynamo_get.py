def dynamo_get():
    import random
    import boto3
    from boto3.dynamodb.conditions import Key
    import pandas as pd
    from decimal import Decimal

    resource = boto3.resource('dynamodb', 
                aws_access_key_id="AAAAAAAAAAAAAAA",
                aws_secret_access_key="BBBBBBBBBBBBBBBBBBBBB",
                region_name='us-east-1')
    table = resource.Table('external-data')

    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.append(response['Items'])

    df = pd.DataFrame(data)
    df = df.sort_values(by=['EmployeeID'])
    return df.head(200).to_html()
