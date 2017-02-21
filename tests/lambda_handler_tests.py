from functions.alexa_dad_jokes.main import handle
from nose.tools import ok_
import unittest
import mock


def assert_alexa_response(response):
    ok_('response' in response)
    ok_('outputSpeech' in response['response'])
    ok_('text' in response['response']['outputSpeech'])


class LambdaHandlerTests(unittest.TestCase):
        def test_will_not_process_malformed_event(self):
            bad_events = [{},
                          {'taco': ''},
                          {'request': {}},
                          {'request': {'type': {}}}]

            with self.assertRaises(Exception):
                for bad_event in bad_events:
                    handle(bad_event, None)

        def test_will_return_alexa_error_reponse_on_unknown_request(self):
            bad_event = {'request': {'type': 'an invalid alexa event'}}

            try:
                response = handle(bad_event, None)
                assert_alexa_response(response)
            except Exception as e:
                self.fail(e)

        @mock.patch('functions.alexa_dad_jokes.main.handlers')
        def test_should_dispatch_launch_request(self, mock_handlers):
            mock_handlers.on_launch.return_value({})
            handle({'request': {'type': 'LaunchRequest'}}, None)
            mock_handlers.on_launch.assert_called()

        @mock.patch('functions.alexa_dad_jokes.main.handlers')
        def test_should_dispatch_intent_request(self, mock_handlers):
            mock_handlers.on_intent.return_value({})
            event = {'request': {'type': 'IntentRequest', 'intent': 'GetJoke'}}
            handle(event, None)
            mock_handlers.on_intent.assert_called()

        def test_should_process_unknown_intent(self):
            event = {'request':
                     {'type': 'IntentRequest', 'intent': {'name': 'Blah'}}}
            response = handle(event, None)

            assert_alexa_response(response)
            ok_(response['response']['outputSpeech']['text'] ==
                'i have no idea what you are saying')

        def test_should_process_get_joke_intent(self):
            event = {'request':
                     {'type': 'IntentRequest', 'intent': {'name': 'GetJoke'}}}

            response = handle(event, None)
            assert_alexa_response(response)
            ok_('?' in response['response']['outputSpeech']['text'])
            ok_('!' in response['response']['outputSpeech']['text'])
