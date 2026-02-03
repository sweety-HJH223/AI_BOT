# AI Chat Automation Bot 🤖

This project is an AI-powered desktop automation system that reads messages from a real chat application interface and replies intelligently using a large language model.
Unlike traditional chatbots that rely on web APIs, this bot interacts directly with a desktop chat application through screen automation, clipboard parsing, and keyboard control.

##  Features
- Reads chat messages directly from a desktop chat application
- Replies using AI-generated, context-aware responses
- Filters replies based on a specific target user
- Human-like behavior using reply cooldowns
- Emergency stop using the ESC key
- Clipboard-based text handling
- Safe automation using PyAutoGUI failsafe
- Conversation logging for debugging and analysis

##  How It Works
1. The bot selects the visible chat area on the screen using mouse automation  
2. Messages are copied via the system clipboard  
3. The latest message from the target user is extracted  
4. The message is sent to an AI model for response generation  
5. The AI-generated reply is pasted back into the chat input box and sent  
6. Safety checks such as cooldowns and emergency stop are continuously enforced  

## Tech Stack
- **Python**
- **PyAutoGUI** – mouse and keyboard automation
- **Pyperclip** – clipboard handling
- **OpenAI API** – AI response generation
- **Keyboard** – emergency stop handling

## Safety & Control Mechanisms
- Emergency stop using the `ESC` key
- PyAutoGUI failsafe enabled
- Reply cooldown to prevent spam
- Target sender filtering to avoid unintended replies
- API keys stored securely using environment variables

## Important Notes
- Screen coordinates are **environment-specific** and must be adjusted per device
- Chat formats may vary depending on the application
- This project is intended for **educational and experimental purposes only**

##  Limitations
- Works on a single chat window at a time
- Requires manual coordinate setup
- Depends on screen resolution and UI layout

##  Future Improvements
- Emotion-aware replies
- Multi-user support
- Configurable profiles
- Improved message parsing
- Accessibility-focused features

## Disclaimer
This project is not affiliated with or endorsed by any chat platform.  
It is intended solely for learning, experimentation, and demonstration of AI and desktop automation concepts.
