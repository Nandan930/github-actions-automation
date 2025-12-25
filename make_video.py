from moviepy.editor import TextClip, CompositeVideoClip

# read script
with open("script.txt", "r") as f:
    text = f.read()

# text video
clip = TextClip(
    text,
    fontsize=50,
    color="white",
    size=(1080, 1920),
    method="caption",
    align="center"
).set_duration(10)

# export video
clip.write_videofile(
    "output.mp4",
    fps=24,
    codec="libx264",
    audio=False
)
