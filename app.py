import os
import json
import logging
import pandas as pd
import boto3
from io import StringIO
import datetime
from typing import Final, Optional, TypedDict, List, Any, Tuple, Union, Dict, NamedTuple


log_level = os.getenv('LOGLEVEL', 'DEBUG')
logging.getLogger(__name__).setLevel(log_level)
logger = logging.getLogger(__name__)

bucket = 'glc-01'
key_prefix = 'koodoo_{}.csv'

s3_client = boto3.client('s3')

def s3_put_df_to_csv(df, bucket, key, header):
  csv_buffer = StringIO()
  df.to_csv(csv_buffer, index=False, header=header)
  s3_client.put_object(Bucket=bucket, Key=key, Body=csv_buffer.getvalue())

def handler(event: dict, context: Optional[dict] = None) -> Dict:
  endpoints = event['endpoints']
  df = pd.DataFrame()
  for e in endpoints:
    temp_df = pd.read_xml(e)
    df = df.append(temp_df)
  curr_time = datetime.datetime.now()
  s3_put_df_to_csv(df, bucket, key=key_prefix.format(curr_time.timestamp()), header=True)
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
  handler(event={'endpoints':[
      'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml',
      'https://www.europarl.europa.eu/rss/doc/top-stories/es.xml',
      'https://www.europarl.europa.eu/rss/doc/top-stories/fr.xml',
      'https://www.europarl.europa.eu/rss/doc/top-stories/it.xml',
      ]})