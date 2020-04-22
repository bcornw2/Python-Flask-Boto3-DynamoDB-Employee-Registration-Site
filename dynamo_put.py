def dynamo_put( request_name ):
    import random
    import boto3
    from boto3.dynamodb.conditions import Key

    client = boto3.client('dynamodb', 
                aws_access_key_id="AAAAAAAAAAAA",
                aws_secret_access_key="BBBBBBBBBBBBBBBBBBBBBBBBBBB",
                region_name='us-east-1')
    
    file = open("lastKey.txt", "r")
    first_line = file.readline()
    for last_line in file:
        pass
    num = int(last_line)+1
    file.close()
    num = str(num)

    name = str(request_name)

    response = client.put_item(TableName='external-data', Item={'Employee Name': {'S': name}, 'EmployeeID':{"N": num}})
    file = open("lastKey.txt", "a+")
    file.write(num + "\n")
    file.close()

    ansExit = ''

    return str("put_item call successful")
