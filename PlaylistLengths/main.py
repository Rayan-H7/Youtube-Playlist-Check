import pytube
from pytube import YouTube
from pytube import Playlist
from datetime import timedelta
#This imports the necessary modules for the pytube function and datetime formatting to work

total_time = 0
#This initialises the total playlist length variable
playlist = Playlist(input("Enter the Playlist URL: "))
#This makes the playlist as an array with each video URL as a string of the array
print(f"There are {playlist.length} videos in {playlist}")
#This provides general information for how many vids in the playlist

for vid in playlist:
    video = YouTube(vid)
    total_time = total_time + video.length
    print(f"{total_time}\n")
#This for loop will first transform the video URL in the array into the Video itself, which we will then add the
#length of that video to the total time of the playlist, printing the total seconds each iteration

mean_time = total_time/playlist.length
#This calculates the average length per video
print(f"The total time to watch the whole playlist is {timedelta(seconds=total_time)}")
#This presents the total time in seconds to HH:MM:SS
print(f"\nThe total time of the {playlist.length} video long playlist is {total_time} seconds.")
#This provides the total playlist length and the amount of time needed to watch the whole playlist
print(f"\nThe mean time of the playlist is {timedelta(seconds=mean_time)}/{mean_time}s per video")
#This provides the mean time length of each video in the HH:MM:SS format