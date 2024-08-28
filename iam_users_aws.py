# importing modules
import boto3

# opening aws managment console
aws_console = boto3.session.Session(profile_name = 'default')

# opening iam console as resource
iam_console = aws_console.resource('iam')

# printing list of users in iam
for users in iam_console.users.all():
    print(users.name)