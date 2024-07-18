import ffmpeg

input_file = "template.mp4"

intro_start = "00:00:00"
intro_end = "00:00:05"
intro_file = "ems_intro.mp4"

outro_start = "00:01:21"
outro_end = "00:01:25"
outro_file = "ems_outro.mp4"

# Extract intro and outro (need to do this only once)
ffmpeg.input(input_file, ss=intro_start, to=intro_end).output(intro_file).run()
ffmpeg.input(input_file, ss=outro_start, to=outro_end).output(outro_file).run()

# Combine parts into new video (do this for every video from a session recording)
session_file = "template.mp4"
talk_start = "00:00:14"
talk_end = "00:01:19"

new_filename = "recombined.mp4"
ffmpeg.concat(
    ffmpeg.input(intro_file),
    ffmpeg.input(session_file, ss=talk_start, to=talk_end),
    ffmpeg.input(outro_file),
).output(new_filename).run()

# TODO: read input times from csv file and loop over all talks in one recording
# TODO: make smoother transitions
# TODO: add automatically generated title/speaker slide
# TODO: use generated title slide as thumbnail
# TODO: automate uploading to youtube!?
# TODO: the output is missing audio now, presumably because intro and outro lack audio tracks.
