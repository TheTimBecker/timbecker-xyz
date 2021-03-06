import boto3

print('Loading function')

s3 = boto3.client('s3')

def lambda_handler(event, context):
  try:
    response = s3.list_objects_v2(
      Bucket='timbecker.xyz',
      EncodingType='url',
      Prefix='index'
    )

    # set default in case it hasn't been deployed
    index_html_name = 'index.html'

    if response['Contents']:
      # get most recent
      sortedContents = sorted(response['Contents'], key=lambda content: content['LastModified'], reverse=True)
      print(sortedContents)
      index_html_name = sortedContents[0]['Key']

    return {'index_html_name': index_html_name}
  except Exception as e:
    print(e)
    print('Error listing objects in timbecker.xyz. Make sure they exist and your bucket is in the same region as this function.')
    raise e
