import sys
import importlib

if __name__ == '__main__':
    # TODO specify the right path
    install_dir = 'PATH/TO/template'
    if not sys.path.__contains__(install_dir):
        sys.path.append(install_dir)

    modules = [
        "CharacterPublisher"
    ]

    from utils import *
    unload_packages(silent=True, packages=modules)

    for module in modules:
        importlib.import_module(module)

    from CharacterPublisher import *

    try:
        character_publisher.close()
    except:
        pass
    character_publisher = CharacterPublisher()
    character_publisher.show()
