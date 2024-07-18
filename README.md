# EMS video generator

This is a small repo to try and auto-generate videos from conference recordings.

It uses FFMPEG, which is a very powerfool tool for editing videos. However, it
can be very cryptic...

To be able to loop over the list of talks, I'm using a small Python wrapper to
generate the FFMPEG commands programmatically.

## Requirements

This requires python + ffmpeg. I used conda/mamba to install latest version of FFMPEG

```sh
# Create environment
mamba create -n emsvideos python=3.12 ffmpeg -y

# Activate the environment
mamba activate emsvideos

# Run the script with example params
python generate_video.py
```

## Further info

- `generate_video` is the main script.
- `split_video.py` is an older script in which I used
  [ffmpeg-python](https://github.com/kkroening/ffmpeg-python). This might be a
  bit more readible, but it was harder to figure out the right commands as there
  is more help online for the 'raw' ffmpeg.
- A sample recording is shipped with the repo for easy testing
- the intro and outro are generated with the included PPT --> export as video.
  I've played with the timing in the transitions tab ("duration"), and hidden
  either the first or last slides to generate either the intro or outro.
