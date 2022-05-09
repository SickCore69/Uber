from asyncio.constants import SSL_HANDSHAKE_TIMEOUT
from inspect import classify_class_attrs
from re import S
from tarfile import XGLTYPE
from termios import OFDEL
from unicodedata import name


class Route:
    ID = int
    star = []
    end = []