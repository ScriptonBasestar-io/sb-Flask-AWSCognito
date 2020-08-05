class FlaskAWSCognitoError(Exception):
    pass

class TokenVerifyError(Exception):
    pass


class FlaskCognitoError(Exception):
    pass

class FlaskCognitoAuthError(FlaskCognitoError):
    pass

class FlaskCognitoJwtAuthError(FlaskCognitoAuthError):
    pass

class FlaskCognitoOAuthError(FlaskCognitoAuthError);
    pass