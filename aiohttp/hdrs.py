"""HTTP Headers constants."""
from .multidict import upstr


ACCEPT = upstr('ACCEPT')
ACCEPT_ENCODING = upstr('ACCEPT-ENCODING')
AUTHORIZATION = upstr('AUTHORIZATION')
CONNECTION = upstr('CONNECTION')
CONTENT_ENCODING = upstr('CONTENT-ENCODING')
CONTENT_LENGTH = upstr('CONTENT-LENGTH')
CONTENT_TYPE = upstr('CONTENT-TYPE')
CONTENT_TRANSFER_ENCODING = upstr('CONTENT-TRANSFER-ENCODING')
COOKIE = upstr('COOKIE')
DATE = upstr('DATE')
EXPECT = upstr('EXPECT')
HOST = upstr('HOST')
KEEP_ALIVE = upstr('KEEP-ALIVE')
LOCATION = upstr('LOCATION')
PROXY_AUTHENTICATE = upstr('PROXY_AUTHENTICATE')
PROXY_AUTHORIZATION = upstr('PROXY-AUTHORIZATION')
REFERER = upstr('REFERER')
SET_COOKIE = upstr('SET-COOKIE')
SEC_WEBSOCKET_KEY1 = upstr('SEC-WEBSOCKET-KEY1')
SERVER = upstr('SERVER')
TE = upstr('TE')
TRAILERS = upstr('TRAILERS')
TRANSFER_ENCODING = upstr('TRANSFER-ENCODING')
USER_AGENT = upstr('USER-AGENT')
URI = upstr('URI')
UPGRADE = upstr('UPGRADE')