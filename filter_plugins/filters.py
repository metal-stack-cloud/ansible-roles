import jwt
from datetime import datetime, timezone, timedelta


def generate_jwt(secret, issuer="metal-stack-cloud", sub="admin", expiry=datetime.now(tz=timezone.utc) + timedelta(days=365*100), roles=None, permissions=None):
    data = {
        "iss": issuer,
        "sub": sub,
        "exp": expiry,
    }

    if roles:
        data["roles"] = roles
    if permissions:
        data["permissions"] = permissions

    return jwt.encode(data, secret, algorithm="HS256")


class FilterModule(object):
    def filters(self):
        return {
            'generate_jwt': generate_jwt,
        }
