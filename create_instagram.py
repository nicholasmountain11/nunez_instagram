from instagrapi import Client
from instagrapi.types import Usertag, Location
import credentials
from random import randint
import spacy
nlp = spacy.load("en_core_web_sm")

cl = Client()
cl.login(credentials.username, credentials.password)

nunez = "darwin_n9"
taylor = "taylorswift"
nunez_user = cl.user_info_by_username(nunez)
taylor_user = cl.user_info_by_username(taylor)

f = open('/Users/nickmountain/Twitter-bot-workspace/nunezbot/taylor.txt', 'r')
lines: list[str] = f.readlines()
f.close()


def write_caption(lines: list[str]) -> str:
    send_tweet: bool = False
    number = randint(0, len(lines)-1)
    line = lines[number]
    line_list = line.split(' ')
    for word in range(len(line_list)):
        
        text = line_list[word]
        doc = nlp(text)
        if (doc[0].tag_ == 'NNP' and line_list[word] != 'wanna'):
            send_tweet = True
            #print('found a noun')
            #print(f"The line was: {line}")
            print(f"The noun was: {line_list[word]}")
            line_list[word] = 'Nunez'
        #print(word)
    
    message = ' '.join(line_list)
    if not send_tweet:
        message = write_caption(lines)

    return message

caption = write_caption(lines)
print(caption)

photos: list[str] = [
    "/Users/nickmountain/Twitter-bot-workspace/nunezbot/nunez.jpeg",
    "/Users/nickmountain/Twitter-bot-workspace/nunezbot/nunez1.jpg",
    "/Users/nickmountain/Twitter-bot-workspace/nunezbot/nunez2.jpg",
    "/Users/nickmountain/Twitter-bot-workspace/nunezbot/nunez3.jpg"
]

photo_index: int = randint(0, len(photos)-1)
print(f"photo index is {photo_index}")


media = cl.photo_upload(
    path = photos[photo_index],
    caption = caption
)

