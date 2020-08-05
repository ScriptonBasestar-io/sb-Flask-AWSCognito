[![Build Status](https://travis-ci.org/cgauge/Flask-AWSCognito.svg?branch=master)](https://travis-ci.org/cgauge/Flask-AWSCognito)
[![Documentation Status](https://readthedocs.org/projects/flask-awscognito/badge/?version=latest)](https://flask-awscognito.readthedocs.io/en/latest/?badge=latest)

# AWS Cognito for authentication in Flask

Documentation https://flask-awscognito.readthedocs.io


## Usage

```python
app = Flask(__name__)

class CognitoConfig:
    AWS_REGION = os.getenv('AWS_DEFAULT_REGION', 'ap-northeast-2')
    COGNITO_DOMAIN = os.getenv('AWS_COGNITO_DOMAIN', 'domain.com')
    COGNITO_USER_POOL_ID = os.getenv('AWS_COGNITO_USER_POOL_ID', '')
    COGNITO_USER_POOL_CLIENT_ID = os.getenv('AWS_COGNITO_USER_POOL_CLIENT_ID', '')
    COGNITO_USER_POOL_CLIENT_SECRET = os.getenv('AWS_COGNITO_USER_POOL_CLIENT_SECRET', '')
    COGNITO_USER_POOL_CLIENT_LOGOUT_URL = os.getenv('AWS_COGNITO_USER_POOL_CLIENT_SECRET', '')
    COGNITO_USER_POOL_CLIENT_REDIRECT_URL = os.getenv('AWS_COGNITO_REDIRECT_URL', 'http://localhost:5000/auth/redirect')
    COGNITO_CHECK_TOKEN_EXPIRATION = os.getenv('COGNITO_CHECK_TOKEN_EXPIRATION', False)
    COGNITO_JWT_HEADER_NAME = os.getenv('COGNITO_JWT_HEADER_NAME', 'X-MyApp-Authorization')
    COGNITO_JWT_HEADER_PREFIX = os.getenv('COGNITO_JWT_HEADER_PREFIX', 'Bearer')

app.config.from_object(CoognitoConfig)
cognito = CognitoFlask(app)
```

## Example App

```python
from flask import Flask, redirect, request, jsonify
from flask_awscognito import AWSCognitoAuthentication
app = Flask(__name__)

app.config['AWS_DEFAULT_REGION'] = 'eu-west-1'
app.config['AWS_COGNITO_DOMAIN'] = 'domain.com'
app.config['AWS_COGNITO_USER_POOL_ID'] = 'eu-west-1_XXX'
app.config['AWS_COGNITO_USER_POOL_CLIENT_ID'] = 'YYY'
app.config['AWS_COGNITO_USER_POOL_CLIENT_SECRET'] = 'ZZZZ'
app.config['AWS_COGNITO_REDIRECT_URL'] = 'http://localhost:5000/aws_cognito_redirect'


aws_auth = AWSCognitoAuthentication(app)


@app.route('/')
@aws_auth.authentication_required
def index():
    claims = aws_auth.claims # also available through g.cognito_claims
    return jsonify({'claims': claims})


@app.route('/aws_cognito_redirect')
def aws_cognito_redirect():
    access_token = aws_auth.get_access_token(request.args)
    return jsonify({'access_token': access_token})


@app.route('/sign_in')
def sign_in():
    return redirect(aws_auth.get_sign_in_url())


if __name__ == '__main__':
    app.run(debug=True)

```

## REF

* https://github.com/cgauge/Flask-AWSCognito
* https://github.com/jetbridge/flask_cognito
* https://github.com/plotlabs/cognises-flask
* https://github.com/CloudySnake/flask-cognito-integration
* https://github.com/forest6511/flask-app-bot3-cognito
* https://github.com/forest6511/flask-app-bot3-cognito
