from pydub import AudioSegment
import requests
import easygui

# get the stuff for making the mp3

text = easygui.enterbox(msg='Enter the text for the spooky man to say.', title='Damon, I love you!', default='', strip=True)

headers = {
    'Connection': 'keep-alive',
    'Accept': '*/*',
    'Origin': 'https://fasthub.net',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://fasthub.net/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

# fasthub.net macintalk voice whisper

data = {
  'text': text,
  'lang': 'en-us en en-US',
  'langTrans': 'en-us en en-US',
  'voiceType': 'whisper',
  'amplitude': '109',
  'pitch': '51',
  'speed': '80',
  'repeat': '0'
}

response = requests.post('https://fasthub.net/plauder', headers=headers, data=data)
mp3stop = response.text.split('#')
mp3url = 'https://fasthub.net/speak/' + mp3stop[0] + '.mp3'
mp3 = requests.get(mp3url, allow_redirects=True)
open('mp3ofVoice.mp3', 'wb').write(mp3.content)

#Put it together

voice = easygui.fileopenbox(title='Choose speech audio')
mp3fromweb = AudioSegment.from_mp3("mp3ofVoice.mp3")
mp3voice = AudioSegment.from_mp3(voice)
mp3guitar = AudioSegment.from_mp3("guitarwail.mp3")
length=len(mp3voice)
combined = mp3guitar.overlay(mp3voice, gain_during_overlay=-12)
final = mp3fromweb + combined

gaming = final.export(text+".mp3", format="mp3")