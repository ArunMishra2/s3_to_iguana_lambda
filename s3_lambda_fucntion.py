import os
import json
import boto3
import logging
from utils.http_utils import post_to_iguana

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client('s3')

# Environment variables
IGUANA_ENDPOINT = os.environ.get("IGUANA_ENDPOINT")
IGUANA_API_KEY = os.environ.get("IGUANA_API_KEY")  # Optional


def lambda_handler(event, context):
    try:
        logger.info("Received event: %s", json.dumps(event))

        for record in event['Records']:
            bucket = record['s3']['bucket']['name']
            key = record['s3']['object']['key']

            logger.info(f"Fetching object from S3: {bucket}/{key}")
            response = s3.get_object(Bucket=bucket, Key=key)
            hl7_data = response['Body'].read().decode('utf-8')

            logger.info(f"Sending HL7 data to Iguana at {IGUANA_ENDPOINT}")
            response_code, response_text = post_to_iguana(IGUANA_ENDPOINT, hl7_data, IGUANA_API_KEY)

            logger.info(f"Iguana Response [{response_code}]: {response_text}")

        return {
            'statusCode': 200,
            'body': 'HL7 message(s) sent to Iguana.'
        }

    except Exception as e:
        logger.error("Error processing file or sending to Iguana: %s", str(e), exc_info=True)
        return {
            'statusCode': 500,
            'body': 'Error sending HL7 to Iguana.'
        }
