## Genius Lyrics Fetcher
This script retrieves lyrics for a specific song by a given artist using the Genius API. 

## requirements.txt
Install the prerequisites
- Python
- lyricsgenius

## Prerequisite
Download and Install Latest version of Python on your system and dowload as per your OS 
https://www.python.org/downloads

## Install Dependencies
pip install lyricsgenius

## Genius API
- Go to Genius website
- Sign up for Genius Account
- Create New API key, by filling the form
- Generate API Token.

## Create a config.py and add your Genius API key
# config.py
api_key = "your_genius_api_key_here"

# index.py
This script performs the following tasks:
- Initializes the Genius API client using the API key from config.py.
- Searches for an artist and retrieves a list of their songs.
- Searches for a specific song by the artist.
- Prints the lyrics of the song if found, otherwise indicates that the song was not found.

## Documentation
- Python Documentation: Python Official Documentation
Learn more about Python's features and libraries.

- lyricsgenius Documentation: lyricsgenius on GitHub
Find more information about the lyricsgenius package, including its methods and usage.
https://pypi.org/project/lyricsgenius/

## Troubleshooting
- Permission Denied (403): Ensure your API key is correct and has the necessary permissions.
- Song Not Found: Check the song and artist names for accuracy.
- Installation Issues: Verify that you have installed the required packages.

## License
This project is licensed under the MIT License.

