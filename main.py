import pyautogui
import pyperclip
import time

text = pyperclip.paste()

time_needed = int(
    pyautogui.prompt(
        """
        How much time(in seconds) do you need for
        1. switching to the editor you want to simulate typing
        2. Placing the cursor at starting postion
        
        Type -1 to exit
    """
    )
)

if time_needed == -1:
    exit()
else:
    time.sleep(time_needed)
    pyautogui.write(text, interval=0.14)