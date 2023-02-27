from django.core.signing import Signer
from django.core import signing 

signer = Signer()  # cryptography signing


def sign(data:str) -> str: # returns data as an encrypted string
    try:
        return signer.sign(data)

    except signing.BadSignature:
        return f"error: tampering detected"


def unSign(data:str) -> str: # returns data as an un-encrypted string
    try:
        return signer.unsign(data)
    except signing.BadSignature:
        return f"error: tampering detected"


def signObj(obj:object):  # returns obj as an encrypted
    try:
        return signer.sign_object(obj)
    except signing.BadSignature:
        return f"error: tampering detected"


def unSignObj(obj:object):  # returns obj as an un-encrypted
    try:
        return signer.unsign_object(obj)
    except signing.BadSignature:
        return f"error: tampering detected"
