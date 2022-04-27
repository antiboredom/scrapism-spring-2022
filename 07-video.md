# Video

## Downloading video with yt-dlp

In some cases, you can find the `src` attribute of a `video` element on a page download that url. However, it's frequently much easier to use a tool called `yt-dlp` instead as it supports a most video-hosting websites.

> NOTE: as of the time of writing, `yt-dlp` seems to be the best and most maintained video downloader. This may change! If it's not working, try `youtube-dl` or `youtube-dlc`.

### Installation

```
pip3 install yt-dlp
```

### Basic usage

To download a video, just type yt-dlp and the url of the video you want. This will work for youtube, vimeo, twitter and *hundreds* of other websites.

```
yt-dlp http://youtube.com.com/somevideo
```

For example:

```
yt-dlp https://www.youtube.com/watch?v=3TuwN0DmNeU
```

You can also download an entire user, channel or playlist. For example this will download the entire whitehouse channel (it will take a long time).

```
yt-dlp https://www.youtube.com/user/whitehouse/
```

### File formats

Websites like youtube and vimeo will store videos in multiple file formats and sizes. To get a list of all of them for a video, simply add the `-F` option:

```
yt-dlp [URL] -F
```
 
You can choose a specific format with `-f` and the code for that format

```
yt-dlp [URL] -f 22
```

Some formats let you download only the video, or only the audio


### Change the output

By default yt-dlp will automatically select a filename to save to. To override this, add the `-o` flag.

```  
yt-dlp [URL] -o whatever.mp4
```    


### Always save mp4s

If you always want to save a file as an mp4, add the `--merge-output-format` option:

```    
yt-dlp [URL] --merge-output-format mp4
``` 



### Download subtitles

To download subtitles from youtube:

```    
yt-dlp [URL] --write-auto-sub --skip-download
``` 


## FFMPEG

`ffmpeg` is a command line tool for manipulating video.

### Installation

```
brew install ffmpeg
```

### Basics

Convert one file format into another:

```
ffmpeg -i input.mkv output.mp4
```

Extract audio:

```
ffmpeg -i input.mkv output.mp3
```

Turn a video into choppier but smaller gif: (-r 3 will make it 3 frames per second)

```
ffmpeg -i input.mp4 -r 3 output.gif
```

Better gifs here: https://engineering.giphy.com/how-to-make-gifs-with-ffmpeg/

```
ffmpeg -ss 61.0 -t 2.5 -i input.mp4 -filter_complex "[0:v] fps=12,scale=480:-1,split [a][b];[a] palettegen [p];[b][p] paletteuse" output.gif
```

extract frames

```
ffmpeg -i input.mp4 frame%08d.jpg
```

images to video:

```
ffmpeg -r 1 -pattern_type glob -i 'test_*.jpg' -c:v libx264 -pix_fmt yuv420p out.mp4
```

images to video, with padding to fix different sizes:

```
ffmpeg -r 20 -pattern_type glob -i 'samfaces/*.jpg' -vf "scale=w=1280:h=720:force_original_aspect_ratio=1,pad=1280:720:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -pix_fmt yuv420p out.mp4
```

increase speed:

```
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" fastvideo.mp4
```

Decrease speed:

```
ffmpeg -i input.mp4 -vf "setpts=2.0*PTS" slowvid.mp4
```

Resize:

```
ffmpeg -i input.mp4 -c:v libx264 -s:v 100x100 -c:a copy output.mp4
```

Trim:

```
ffmpeg -ss 00:01:30 -i input.mp4 -c:v copy -c:a copy -t 5 output.mp4
```

put all videos in a folder together

```
for f in *.mp4 ; do echo file \'$f\' >> list.txt; done && ffmpeg -f concat -safe 0 -i list.txt -s 1280x720 -crf 24 stitched-video.mp4 && rm list.txt
```

Making a mirror effect:

```
ffmpeg -i input.mp4 -vf "crop=iw/2:ih:0:0,split[left][tmp];[tmp]hflip[right];[left][right] hstack" output.mp4
```


Edge detection:

```
ffmpeg -i input.mp4 -vf "edgedetect=low=0.1:high=0.4" output.mp4
```

Fading in:

```
ffmpeg -i input.mp4 -vf "fade=in:0:30" output.mp4
```

Slow down a video with frame interpolation:

```
ffmpeg -i input.mp4 -vf ""[0:v]minterpolate=fps=120:mi_mode=mci[out];[out]setpts=5*PTS"" -y output.mp4
```

Overlay audio on to video:

```
ffmpeg -i input.mp4 -i input.mp3 -c copy -map 0:v:0 -map 1:a:0 output.mp4
```

Chromakey overlay:

```
ffmpeg -i background.mp4 -i foreground.mp4 -filter_complex "[1]colorkey=0xffffff:0.5:0.1[fg];[0][fg]overlay[out]" -map "[out]" together.mp4
```

Record from a webcam (on mac) for 10 seconds and save to file

```
ffmpeg -f avfoundation -pixel_format yuyv422 -framerate 30 -video_size 1280x720 -i 0:0 -t 00:00:10 -y webcamrecord.mp4
```

## Videogrep

`videogrep` is a command line program that allows you to create supercuts of videos based audio transcriptions. Like `grep` but for video!

### Installation

```
pip3 install videogrep
```

### Usage

Use the `--search` argument to find clips in a video that contain specific text patterns

```
videogrep --input my_video.mp4 --search 'some word or phrase' --output my_new_video.mp4
```

You can also pass it multiple videos with the `*` pattern:

```
videogrep --input *.mp4 --search 'some word or phrase' --output my_new_video.mp4
```
