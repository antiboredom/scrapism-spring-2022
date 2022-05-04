import random
from moviepy.editor import VideoFileClip, CompositeVideoClip

vid = VideoFileClip('shell.mp4')
clips = []


duration =5
start = 0
size = 1.0

for n in range(5):
    clip = vid.subclip(start, start+duration)
    clip = clip.set_pos("center").resize(size).set_start(n)
    clips.append(clip)

    size -= 0.1
    start += duration

final = CompositeVideoClip(clips)
final.write_videofile("vid_in_vid.mp4")
