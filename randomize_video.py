import random
from moviepy.editor import VideoFileClip, concatenate_videoclips

# creates 100 1 second clips from a video and puts them in random order

vid = VideoFileClip('shell.mp4')
clips = []

start = 0
duration = 1

while start < 100:
    clip = vid.subclip(start, start+duration)
    clips.append(clip)
    start += duration

random.shuffle(clips)

final = concatenate_videoclips(clips)
final.write_videofile("shuffled.mp4")
