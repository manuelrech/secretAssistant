from ass import ResponseHandler
from pynput.keyboard import Listener

def main():
    handler = ResponseHandler()
    with Listener(on_press=handler.on_press, on_release=handler.on_release) as listener:
        listener.join(timeout=60*60*3) # 3 ore

if __name__ == "__main__":
    main()