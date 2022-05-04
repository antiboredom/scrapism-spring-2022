from moviepy.editor import VideoFileClip, CompositeVideoClip, TextClip

vid = VideoFileClip("shell.mp4")

clips = []

text = TextClip("A spectre is haunting", fontsize=70, color="white", font="Courier")
text = text.set_duration(10).set_start(0).set_pos("center")

clips = [vid.subclip(100, 110), text]

final = CompositeVideoClip(clips)
final.write_videofile("vid_with_text.mp4")
