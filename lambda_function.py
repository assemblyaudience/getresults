import requests
import json

import boto3

s3 = boto3.client('s3')

urls_by_locale = ["https://er.ncsbe.gov/enr/20261103/data/results_41.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_92.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_32.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_26.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_0.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_9.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_24.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_78.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_83.txt?v=22-15-12",
                  "https://er.ncsbe.gov/enr/20261103/data/results_68.txt?v=22-15-12"
                  ]


def lambda_handler(event, context):
    response = []
    for i in urls_by_locale:
        json_results = requests.get(i).json()
        response.append(json_results)
    s3.put_object(
        Body=(bytes(json.dumps(response).encode('UTF-8'))),
        Bucket='election-data-holder-26',
        Key='results.json')

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }

# election-data-holder-26 is the name of the S3 bucket

