# Video Cutter

A Python tool that splits a large video into smaller segments compliant with Discord's base file size limit (25MB). Written to replace the tedious process of manually editing and exporting clips.

## Usage

1. Place your video in the same folder as the script.
2. Either rename the video to `Part0.mp4`, or update the `mainClip` variable in the script to match your filename.
3. Run the script:

```bash
pip install -r requirements.txt
python VideoCutter.py
```

Output files are saved as `Part1.mp4`, `Part2.mp4`, etc. in the same folder.

## Note

If moviepy isn't working, downgrade to version 1.0.3. See [this issue](https://github.com/Zulko/moviepy/issues/2419#issuecomment-3240737560) for context.
