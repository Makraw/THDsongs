import requests
from bs4 import BeautifulSoup # To get everything
import os
import sched, time

#
URL = "http://muzakwpn.muzak.com/wpn/030.html"
SONGS_TEXT = "songs.txt"

def refresh(known_songs, document):
	responce = requests.get(URL) #HTTP Get Request
	
	if not responce.ok: # if responce.status code is equal to or greater than 400 A.K.A bad HTTP status code
		print("abadon ship: {}".format(responce.statuse_code))
		return
	soup = BeautifulSoup(responce.text, features="html.parser")
	tr = soup.findAll('tr')[1] #Second Element
	currently_playing = tr.td.div.p.text.replace("Now on FM-1", "")
	
	if currently_playing not in known_songs:
		known_songs.append(currently_playing)
		document.write(currently_playing)
		document.write('\n')
		document.flush()
		
def main():
	known_songs = []
	if not os.path.exists(SONGS_TEXT):
		with open(SONGS_TEXT, "w") as f:
			f.write('')
	else:
		with open(SONGS_TEXT, "r") as f:
			known_songs += f.read().split('\n')
	
	with open(SONGS_TEXT, "a") as document:
		refresh(known_songs, document)
		s = sched.scheduler(time.time, time.sleep)
		s.enter(30, 1, lambda sc: refresh(known_songs, document), (s,))
		s.run()

if __name__ == "__main__":
	main()
