from .proxy import Proxy
from .gui import Gui

import threading

def main():
    """Entrypoint"""
    gui = Gui()
    proxy = Proxy()

    thread = threading.Thread(target=proxy.proxy_up)
    thread.start()

    gui.frame()

    thread.join()

if __name__ == '__main__':
    main()