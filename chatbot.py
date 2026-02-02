import pyautogui
import time
import pyperclip
import os
import keyboard
from openai import OpenAI

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5


BOT_ACTIVE = True               # Turn bot ON/OFF
REPLY_COOLDOWN = 30             # seconds between replies
TARGET_SENDER = "TARGET_USER"

# Coordinates – replace these with your dynamically captured ones
ICON_COORD = (1145, 1046)       # icon to open app (Example coordinates (screen-dependent))
CHAT_START = (1555, 306)        # top of chat area for selecting text  (  Example coordinates (adjust per device))
INPUT_BOX = (1810, 905)         # text input box

last_reply_time = 0


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")  # secure API key
)


def get_last_message_from_sender(chat_log, sender_name=TARGET_SENDER):
    """
    Extract only the last message from the target sender.
    Works for chat format: [time] Name: message
    """
    lines = chat_log.strip().split('\n')
    for line in reversed(lines):
        line = line.strip()
        if line.startswith('[') and f"{sender_name}:" in line:
            # Extract text after the first occurrence of 'Name:'
            return line.split(f"{sender_name}:")[-1].strip()
    return ""


# Step 1: Click the icon once to open the app
pyautogui.click(*ICON_COORD)
time.sleep(1)

print("🤖 AI Chat Bot started")

while True:
    # EMERGENCY STOP
    if keyboard.is_pressed('esc'):
        print("ESC pressed. Stopping bot safely.")
        break

    try:
        # Step 2: Select the chat text area
        pyautogui.moveTo(*CHAT_START)
        pyautogui.mouseDown()
        pyautogui.moveTo(CHAT_START[0] + 250, CHAT_START[1] + 623, duration=0.5)  # adjust as needed
        pyautogui.mouseUp()

        # Step 3: Copy selected text
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.5)

        # Step 4: Get clipboard text
        chat_history = pyperclip.paste()
        print("chat_history:")
        print(chat_history)

        # Step 5: Get only last message from target
        last_message = get_last_message_from_sender(chat_history)

        if BOT_ACTIVE and last_message != "":
            current_time = time.time()

            # Cooldown check
            if current_time - last_reply_time >= REPLY_COOLDOWN:
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                " You are an AI assistant replying on behalf of the user in a natural and human-like way. you speak English and hing-lish and korean. "
                                "You are a coderAnalyze chat history and respond naturally. use emoji also when needed."
                                "Output should be the next chat response only. do not write name date time at first in the reply."
                            )
                        },
                        {"role": "user", "content": last_message}
                    ]
                )

                response = completion.choices[0].message.content
                pyperclip.copy(response)

                print("Bot response:")
                print(response)

                # Log reply
                with open("bot_log.txt", "a", encoding="utf-8") as f:
                    f.write(response + "\n\n")

                # Step 6: Focus input box and paste response
                pyautogui.click(*INPUT_BOX)
                time.sleep(0.2)
                pyautogui.click(*INPUT_BOX)  # double click to ensure focus
                time.sleep(0.5)

                pyautogui.hotkey("ctrl", "v")
                time.sleep(0.3)
                pyautogui.press("enter")

                last_reply_time = current_time
            else:
                print("Cooldown active, skipping reply.")

        else:
            print("No new message from target or bot is OFF.")

        # Delay before next check
        time.sleep(5)

    except Exception as e:
        print("Error occurred:", e)
        time.sleep(5)
