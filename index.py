import lyricsgenius
import config 
#initialize Genius API client
genius = lyricsgenius.Genius(config.api_key)

#search for artist and get a list of their songs
artist = genius.search_artist("MAROON 5", max_songs=5, sort="title")
print(artist.songs)

#lyrics

song = genius.search_song("Girls like you","Maroon 5")
if song:
    print(f"\nLyrics for '{song.title}")
    print(song.lyrics)
else:
    print("Song not found")