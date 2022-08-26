import json
import random
import uuid
from datetime import datetime

import boto3


def select_recommender():
    """
    Random selection with 50/50 chance
    :return: Name of Recommender
    """

    index = random.randint(1, 3)

    if index == 1:
        return "RecommenderA"
    elif index == 2:
        return "RecommenderB"
    else:
        return "RecommenderC"


recommender = select_recommender()


def simulate_user_click() -> int:
    """
    Simulate user behaviour from both recommenders.
    Function behaves like a user who clicks from a list of 20 ranked recommendations.
    UI sends an event back to kinesis for tracking purposes.
    :return: Simulated Click Position as Int
    """
    # return random.randint(1, 5) if recommender == "RecommenderB" else random.randint(6, 20)
    if recommender == "RecommenderB":
        return random.randint(1, 5)
    elif recommender == "RecommenderA":
        return random.randint(6, 20)
    else:
        return random.randint(1, 20)


def lambda_handler(event, context):
    client = boto3.client('kinesis')
    event = {"response_id": str(uuid.uuid4()),
             "time": str(datetime.now()),
             "recommender_system": recommender,
             "click_position": simulate_user_click(),
             }
    response = client.put_record(
        StreamName='ga-recommender-stream',
        Data=json.dumps(event),
        PartitionKey='recommender_system'
    )
    return response
