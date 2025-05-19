import webbrowser, time
import pyautogui
from dotenv import load_dotenv
import os

load_dotenv()
TWITCH_USER = os.getenv("TWITCH_USERNAME")
TWITCH_PASS = os.getenv("TWITCH_PASSWORD")
YT_USER     = os.getenv("YOUTUBE_USERNAME")
YT_PASS     = os.getenv("YOUTUBE_PASSWORD")

pyautogui.PAUSE = 0            
pyautogui.FAILSAFE = False     

webbrowser.open("https://www.twitch.tv/login", new=2)
time.sleep(1)                  
pyautogui.write(TWITCH_USER)   
pyautogui.press("tab")
pyautogui.write(TWITCH_PASS)
pyautogui.press("enter")

webbrowser.open(
  "https://accounts.google.com/ServiceLogin?service=youtube",
  new=2
)
time.sleep(1)
pyautogui.write(YT_USER)
pyautogui.press("enter")
time.sleep(2)                  
pyautogui.write(YT_PASS)
pyautogui.press("enter")
