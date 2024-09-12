# EMS video generator

This is a small repo to try and auto-generate videos from conference recordings.

I've tried two approaches:

1. Use FFMPEG directly. FFMPEG, which is a very powerfool tool for editing videos. However, it can be very cryptic. Here, I'm using a small Python wrapper to generate the FFMPEG commands programmatically.
2. Use MoviePy. Under the hood, this also uses FFMPEG, but it is easier to read. The documentation is lacking a bit though, and the authors are struggling to find time to maintain the tool.

## Requirements

Option 1 requires python + ffmpeg. I used conda/mamba to install latest version of FFMPEG

```sh
# Create environment
mamba create -n emsvideos python=3.12 ffmpeg -y

# Activate the environment
mamba activate emsvideos
```

Option 2 requires more dependencies, which can be added with pip/conda/mamba:

```sh
pip install moviepy opencv-python

# If imagemagick is not installed on you system, you could try via anaconda
mamba install imagemagick
```

## Running the scripts:

```sh
# Run option 1 (only ffmpeg)
python generate_video.py

# Run option 2 (moviepy)
python generate_move.py
```

## Further info

- `generate_video` is the main script.
- `split_video.py` is an older script in which I used
  [ffmpeg-python](https://github.com/kkroening/ffmpeg-python). This might be a
  bit more readible, but it was harder to figure out the right commands as there
  is more help online for the 'raw' ffmpeg.
- A sample recording is shipped with the repo for easy testing
- The intro and outro are generated with the included PPT --> export as video.
  I've played with the timing in the transitions tab ("duration"), and hidden
  either the first or last slides to generate either the intro or outro.
