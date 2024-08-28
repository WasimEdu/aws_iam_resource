# importing mordules
import boto3

# opening aws management console
aws_console = boto3.session.Session(profile_name = "default")

# opening IAM console as resource
iam_console = aws_console.resource("iam")

# printing user list in IAM
for users in iam_console.users.all():
    print(users.name)