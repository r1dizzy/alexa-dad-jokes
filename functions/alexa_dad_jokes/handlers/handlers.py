from db import get_joke


def on_launch(launch_request, session):
    return _build_response('This is a really bad joke telling app')


def on_intent(intent_name):
    speech_text = ''

    if intent_name != "GetJoke":
        speech_text = 'i have no idea what you are saying'
    else:
        joke = get_joke()
        speech_text = '{0}?{1}!'.format(joke.joke, joke.punchline)

    return _build_response(speech_text)


def on_failure(msg):
    return _build_response(msg)


def _build_response(speech_text):
    return {
        'version': '1.0',
        'sessionAttributes': {},
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': speech_text
            },
            'card': {
                'type': 'Simple',
                'title': 'DadJokes',
                'content': speech_text
            }
        }
    }
