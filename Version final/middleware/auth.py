import jwt

secret = "secret"


def generate_token(username):
    """Generates a JSON Web Token(JWT) for authentication
    using a username dictionary i.e. {'username': 'svaneg11'}
    this token can be sent from the client to the API Rest for authentication
    in requests that requires auth

    see example() function below
    """
    encoded_jwt = jwt.encode(username, secret, algorithm="HS256")
    return encoded_jwt


def get_username_from_token(encoded_jwt):
    """Validates the integrity of the JWT, decodes it and gets the username from it"""
    decoded_jwt = jwt.decode(encoded_jwt, secret, algorithms="HS256", options={'verify_exp': False})
    return decoded_jwt.get('username')


def example():
    key = generate_token({'username': 'svaneg11'})
    print(key)
    username = get_username_from_token(key)
    print(username)

#example()