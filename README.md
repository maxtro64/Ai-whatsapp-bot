# Chat Automation with Generative AI

This project is a Python automation script that leverages **pyautogui**, **pyperclip**, and **Google Generative AI** to monitor a chat window, analyze chat history, and automatically generate and paste a reply in a conversational style. The generated response is tailored to sound like a specific persona ("Shivam Yadav"), a 20-year-old college student and coder from India who speaks Hinglish and replies in a humorous, short manner.

## Features

- **Chat Monitoring:** Captures the chat history from a defined screen region.
- **Message Analysis:** Uses regular expressions to process and clean the chat history.
- **Generative AI Integration:** Calls Google Generative AI (Gemini-1.5 Flash) to generate a reply based on the chat context.
- **Automation:** Automatically pastes the generated response into the chat window using keyboard shortcuts.
- **Loop Execution:** Continuously monitors and responds at set intervals.

## Prerequisites

- **Python 3.6+**
- **Google Generative AI Library:** Make sure to have access to the required Google API and the appropriate API key.
- **Required Python Packages:**  
  - `pyautogui`
  - `pyperclip`
  - `google-generativeai`
  - `re` (standard library)
  - `time` (standard library)

You can install the required packages using pip:

```bash
pip install pyautogui pyperclip google-generativeai
