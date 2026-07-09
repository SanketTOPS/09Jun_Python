from pytubefix import YouTube

url="https://www.youtube.com/watch?v=a1__-tNofbE"

YouTube(url).streams.first().download()