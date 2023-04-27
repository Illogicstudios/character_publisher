import importlib
from common import utils

utils.unload_packages(silent=True, package="character_publisher")
importlib.import_module("character_publisher")
from character_publisher.CharacterPublisher import CharacterPublisher
try:
    char_publisher.close()
except:
    pass
char_publisher = CharacterPublisher()
char_publisher.show()
