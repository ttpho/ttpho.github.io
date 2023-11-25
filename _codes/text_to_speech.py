# python3 ./text_to_speech.py
from bardapi import BardCookies
import sys

cookie_dict = {
    "__Secure-1PSIDTS": "xxx",
    "__Secure-1PSID": "xxx."
}

print("Input text to speech")
input_text = str(input())
bard = BardCookies(cookie_dict=cookie_dict)
audio = bard.speech(input_text)
with open("speech.ogg", "wb") as f:
  f.write(bytes(audio['audio']))
