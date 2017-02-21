import handlers


def handle(event, context):
    event_type = event['request']['type']
    response = None

    if event_type == 'LaunchRequest':
        response = handlers.on_launch(None, None)
    elif event_type == 'IntentRequest':
        response = handlers.on_intent(event['request']['intent'])
    else:
        msg = 'You\'re lips moved, but I didn\'t hear what you said'
        response = handlers.on_failure(msg)

    return response
