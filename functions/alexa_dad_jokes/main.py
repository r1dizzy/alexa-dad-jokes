import os
from handlers import dispatch

ALEXA_SKILL_ARN = os.environ["ALEXA_SKILL_ARN"]
if not ALEXA_SKILL_ARN:
    raise Exception('ALEXA_SKILL_ARN env var not set')


# TODO: Validate event is Alexa event
def handle(event, context):
    """
    entry point for the Lamba
    """
    if (event['session']['application']['applicationId'] != ALEXA_SKILL_ARN):
        raise ValueError("Invalid Application ID")

    event = event['request']['type']

    response = dispatch(event)
    return response
