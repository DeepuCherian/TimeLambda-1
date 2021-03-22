import boto3
import os
import datetime
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
now = datetime.datetime.now();

def lambda_handler(event, context):
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info('## EVENT')
    logger.info(event)
    
    bucketName = os.environ['s3_bucketName'] 
    fileName = "hello.txt"
    lambdaPath = "/tmp/" + fileName
    s3Path = "/tl01/" +now.strftime('%Y%m%d%H%M%S%f') + fileName

    logger.info("environment variable: " + bucketName)
    message = '{}, {}\nThe current date and time is {}.\nThank you for visiting, please come again! '.format(getCurrentTimeMsg(now.hour), event['name'], str(now))
    logger.info(message + '=> ' + s3Path)
    logger.info('Name of file to be created:' + s3Path)
    encodedString = message.encode("utf-8")
    
    s3 = boto3.resource('s3')
    s3.Bucket(bucketName).put_object(Key=s3Path, Body=encodedString)

    logger.info('File ' + s3Path + ' creation completed.' )
    print('completed S3 write')
    return {'completed'}

def getCurrentTimeMsg(currentHour):
    if(currentHour>=0 and currentHour<=11):
        return "Good Morning";
    elif(currentHour>=12 and currentHour<=17):
        return "Good Afternoon";
    elif(currentHour>=18 and currentHour<=23):
        return "Good Evening";
