from handlers import on_launch, on_intent, on_failure

_dispatcher = {
    'LaunchRequest': on_launch,
    'IntentRequest': on_intent
}


def dispacth(intent):
    response = None
    try:
        response = _dispatcher[intent]
    except KeyError:
        msg = 'You\'re lips moved, but I didn\'t hear what you said'
        response = on_failure(msg)

    return response
