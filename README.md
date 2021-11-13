# THDsongs
This program is designed to automatically create a playlist in the form of a CSV by scraping the Muzak website.
As written it will create a playlist out of the channel FM-1


To change the muzak channel you want to scrape, change the URL constant to the URL of the relevant channel.
The muzak website can be found at:

http://muzakwpn.muzak.com/

the URL is for the popup that opens when a channel is selected

If you want to change the name of the csv that is created, change the SONGS constant to be the new filename.

As it is written, this code MUST take as long as it takes to play every song in the play list AT LEAST in order to scrape every song. Since the playlists muzak uses are
roughly 600-700 songs long, this will take a few days at least to get everything. Since it's written to just keep running until you use the exit character or otherwise
force stop, I recommend just starting the program in its own terminal window and letting run in the backgroung.
