

import pyautogui
import time
import pyperclip
import google.generativeai as genai
import re

pyautogui.click(1065,1064) # Assuming this is clicking somewhere to bring focus to the chat window.  Needs adjustment based on your screen.
time.sleep(1)



def is_last_meassage_from_sender(chatlog,sendername="Niwas K DSEU"):
  try:
    messages = chatlog.strip().split("\n") #Split by newline, not "/2024]"
    last_message = messages[-1].split(":",1) #Split at the first colon to get sender and message
    if len(last_message) >1 and last_message[0].strip() == sendername:
      return True
    return False
  except:
    return False #Handle potential errors gracefully.

while True:
  
  pyautogui.moveTo(674,213) #Screen coordinates need adjustment for your setup.
  pyautogui.dragTo(1868,910,duration=1.0,button='left')
  
  pyautogui.hotkey('ctrl','c')
  time.sleep(1)
  
  chat_history=pyperclip.paste()
  #Improved regex to handle various date/time formats and potential extra spaces.
  newchat_history=re.sub(r'\[.*?\]\s*[A-Za-z\s]+:\s*', '',chat_history) 
  print(chat_history)
 
  if is_last_meassage_from_sender(chat_history):

    try:
      genai.configure(api_key="AIzaSyADqSruoXH9ZVBLvOmI5RF65IaX_0xgmeE") #Your actual API Key here.  DO NOT HARDCODE API KEYS IN PUBLIC REPOSITORIES.
      model = genai.GenerativeModel("gemini-1.5-flash")
      role =  "You are a person named shivam yadav a 20 years male   who speaks Hinglish and reply in short .You are from India and  you are a college student and coder .You analyze chat history and respond like shivam in a funny way .output should be the next response as shivam "
      prompt = f"{role}\nChat History:\n{newchat_history}\nShivam's reply:"
      response = model.generate_text(prompt)
      print(f"Shivam says: {response}")
      pyperclip.copy(response)
      pyautogui.hotkey('ctrl','v')  #Paste the response
      time.sleep(2) #Added a delay to allow pasting
    except Exception as e:
      print(f"Error: {e}")

  time.sleep(5) #Added a delay to avoid overloading the system. Adjust as needed.



  # if is_last_meassage_from_sender(chat_history):

  
  # Configure the API with your API key
  genai.configure(api_key="AIzaSyADqSruoXH9ZVBLvOmI5RF65IaX_0xgmeE")
  
  # Initialize the model (you can use "gemini-1.5-flash" or another available model)
  model = genai.GenerativeModel("gemini-1.5-flash")
  
  # Provide a role for the AI by including it in the prompt or context
  role =  "You are a person named shivam yadav a 20 years male   who speaks hinglish and reply in short .You are from india and  you are a college student and coder .You analyze chat history and respond like shivam in a funny way .output should be the next response as shivam "
  prompt = newchat_history
  
  # Combine the role and the prompt
  full_prompt = f"{role} {prompt}"
  
  # Generate content using the model
  response = model.generate_content(full_prompt)
  
  # Print the generated response
  print(response.text)
  
  pyperclip.copy(response.text)
  
  pyautogui.click(1208,958)
  
  time.sleep(1)
  
  pyautogui.hotkey('ctrl','v')
  
  pyautogui.hotkey('enter')
    