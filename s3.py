#!/usr/bin/python

from boto.s3.connection import S3Connection
import email
from identity import *

emails = []

aws_connection=S3Connection(AWS_KEY,AWS_SECRET)
bucket = aws_connection.get_bucket(BUCKET)
for file_key in bucket.list():
	print file_key.name
	emails.append(email.message_from_string(file_key.get_contents_as_string()))
	

print "ID\tFrom\t\t\tTo\t\t\tSubject"

index = 0

for email in emails:
	print "%04d\t%.20s\t%.20s\t%.40s\n"%(index,email.get('From'),email.get('To'),email.get('Subject'))
	index += 1
