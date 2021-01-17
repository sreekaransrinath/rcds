import praw
import requests
import shutil
from urllib.parse import urlencode
import webbrowser
import time
import pyautogui
from hashlib import sha256

r = praw.Reddit(
    client_id = "6rPbvVW8IoKD9g",
    client_secret = "LOL not entering this",
    user_agent = "USERAGENT"
)
password = input('Enter the password ')

# Doing this for the memes
if sha256(password.encode()).hexdigest() == '62e434ac7dd69d853b8e2874e3fcf966f70f4e45f109867c20e941126c0f0ddd':

    memes = r.subreddit("memes+dankmemes+darkmemes")
    count = 0
    phones = ['Of course I\'m not gonna give you guys my phone number']
    for submission in memes.top('year', limit = 10000):
        count += 1
        requests.post('https://discord.com/api/webhooks/800155967118376970/7MXNuSJmNBxn4lfAm0VKkWD1fVw_DL_qu5ZbiHrWo3JUn0X8X9powPf7_510cdu43c5g', data = {'content': submission.title})
        requests.post('https://discord.com/api/webhooks/800155967118376970/7MXNuSJmNBxn4lfAm0VKkWD1fVw_DL_qu5ZbiHrWo3JUn0X8X9powPf7_510cdu43c5g', data = {'content': submission.url})
        print(submission.url)
        time.sleep(5)
        if count % 10 == 0:
            time.sleep(600)
        filename = submission.url.split("/")[-1]

        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(submission.url, stream = True)

        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfile(r.raw, f"C:/Users/skaranzx16/Pictures/rcdsMemes/{f}")

        for phone in phones:
            params = {
                'phone': f'91{phone}',
                'text': f'{submission.url}'
            }

        webbrowser.open(f"https://api.whatsapp.com/send?{urlencode(params)}")
        print(f"https://api.whatsapp.com/send?{urlencode(params)}")
        time.sleep(0.1)
        pyautogui.press('Enter')

else:
    print('Wrong password, try again in some time')