from moviepy.editor import TextClip, CompositeVideoClip
from datetime import datetime

with open("script.txt", "r") as f:
    text = f.read()

clip = TextClip(
    text,
    fontsize=60,
    color="white",
    size=(1080, 1920),
    method="caption",
    align="center"
).set_duration(10)

video = CompositeVideoClip([clip])
filename = "video_" + datetime.now().strftime("%H%M%S") + ".mp4"
video.write_videofile(filename, fps=24)

print("Video created:", filename)
