# python3 ./bard.py 
from bardapi import BardCookies
import sys

cookie_dict = {
    "__Secure-1PSIDTS": "xxx",
    "__Secure-1PSID": "xxx."
}

print("Ask anything: ")
input_text = str(input())
bard = BardCookies(cookie_dict=cookie_dict)
answer = bard.get_answer(input_text)
content_answer = answer['content']
print(content_answer)
