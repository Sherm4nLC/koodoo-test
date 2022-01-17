import os
import json
import logging
import pandas as pd
import boto3
from io import StringIO
import datetime


log_level = os.getenv('LOGLEVEL', 'DEBUG')
logging.getLogger(__name__).setLevel(log_level)
logger = logging.getLogger(__name__)

endpoint = 'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml'
bucket = 'glc-01'
key_prefix = 'koodoo_{}.csv'

s3_client = boto3.client('s3')

def s3_put_df_to_csv(df, bucket, key, header):
  csv_buffer = StringIO()
  df.to_csv(csv_buffer, index=False, header=header)
  s3_client.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())

def handler(event, context):
  df = pd.read_xml(endpoint)
  curr_time = datetime.datetime.now()
  s3_put_df_to_csv(df, bucket, key=key_prefix.format(curr_time.timestamp()), header=False)
  msg = f'Done importing to s3 at {curr_time.isoformat()}'
  logger.info(msg)
  return {
      "statusCode":
          200,
      "headers": {
          'Content-Type': 'application/json'
      },
      "body":
          json.dumps({
              "message": msg
          })
      }

if __name__ == '__main__':
  handler({}, {})