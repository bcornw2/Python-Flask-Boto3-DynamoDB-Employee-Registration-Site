##Using Python, Flask, Boto3, and DynamoDB to allow web-based retrievals of DynamoDB content, as well as uploads of new items

This is a website hosted on Apache on an EC2 instance, which uses Python + Flask + Boto3 to make API calls to DynamoDB to retrieve and update information on existing employees.

It uses two text files, one to record all usage and requests, and one to verify that any newly-created data will be provisioned with the correct EmployeeID, ensuring no overlaps.

The Python Flask web app was configured as a systemd daemon and runs at startup.

