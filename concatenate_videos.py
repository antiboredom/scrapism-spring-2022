from moviepy.editor import VideoFileClip, concatenate_videoclips

vid1 = VideoFileClip('shell.mp4')

c2 = vid1.subclip(10, 11)
c3 = vid1.subclip(20, 21)
c1 = vid1.subclip(30, 31)

clips = [c1, c2, c3]
final = concatenate_videoclips(clips)
final.write_videofile('vid.mp4')
