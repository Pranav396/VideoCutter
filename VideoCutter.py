# I downgraded moviepy to 1.0.3 as per Zhang Chen's comment and everything started working again.
# https://github.com/Zulko/moviepy/issues/2419#issuecomment-3240737560

from moviepy.editor import *

mainClip = VideoFileClip("Part0.mp4")
labelCount = 1
startTime = 0
endTime = mainClip.duration

while startTime + 20 <= endTime:
    cutClip = mainClip.subclip(startTime, startTime + 20)
    cutClip.write_videofile(f"Part{labelCount}.mp4", bitrate="3600k", audio_codec="aac")
    labelCount += 1
    startTime += 20
else:
    cutClip = mainClip.subclip(startTime, endTime)
    cutClip.write_videofile(f"Part{labelCount}.mp4", bitrate="3600k", audio_codec="aac")
    cutClip.close()

print("That's all!")
mainClip.close()