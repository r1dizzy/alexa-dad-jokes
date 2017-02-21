import db


def on_launch(launch_request, session):
    return build_response('This is a really bad joke telling app')


def on_intent(intent):
    speech_text = ''

    if intent['name'] != 'GetJoke':
        speech_text = 'i have no idea what you are saying'
    else:
        joke = db.get_joke()
        speech_text = '{0}?{1}!'.format(joke.joke, joke.punchline)

    return build_response(speech_text)


def on_failure(msg):
    return build_response(msg)


def build_response(speech_text):
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
