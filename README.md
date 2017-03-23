# alexa-dad-jokes
An Alexa Skill To Tell Bad Jokes

# Requirements

* Python 2.7, pip, and virtualenv
* An AWS account (the skill is deployed via AWS Lambda)
*  [Apex](https://github.com/apex/apex) configured with your AWS credentials

# Development setup

* ```virtualenv .venv``` to create the virtual environment
* ```source .venv/bin/activate``` to activate the virtual environment
* ```pip install -r requirements.txt``` to install project dev dependencies
* ```nosetests``` to run the tests
* ```apex deploy``` to deploy the lambda to AWS

# Adding a Joke

Jokes are located in __functions/alexa-dad-jokes/jokes.csv__. To add a new one, add a new line in the form of "__joke,punchline__"

TODO:

How to set up the Alexa app and the different voice command examples
