import subprocess
from textwrap import wrap

# mamba create -n emsvideos python=3.12 ffmpeg -y
# mamba activate emsvideos
# python generate_video.py

INTRO = "ems_intro.mp4"
OUTRO = "ems_outro.mp4"


def generate_ffmpeg_script(
    title, author, recording, start_time, end_time, output, max_length=30
):
    wrapped_title = wrap(title, max_length)
    # TODO: also wrap/abbreviate authors?

    title_start = 5
    title_fade = 2
    author_start = 7

    drawtext_filters = []
    for i, line in enumerate(wrapped_title):
        drawtext_filters.append(
            f"""drawtext=
            text='{line}':
            x=100:
            y={400 + 120*i}:
            fontcolor=white:
            fontsize=96:
            alpha='if(lt(t,{title_start}),0,if(lt(t,{title_start+title_fade}),(t-{title_start})/{title_fade},1))'
            """
        )

    drawtext_filters.append(
        f"""drawtext=
        text='{author}':
        x=100:
        y={400 + 120*len(wrapped_title)}:
        fontcolor=white:
        fontsize=36:
        alpha='if(lt(t,{author_start}),0,if(lt(t,{author_start+title_fade}),(t-{author_start})/{title_fade},1))'
        """
    )

    filter_complex = ", ".join(drawtext_filters)

    ffmpeg_command = f"""
    # Overlay text on intro template with animations
    ffmpeg -i "{INTRO}" -vf "{filter_complex}" -c:v libx264 -y intro_with_text.mp4

    # Add silent audio stream to intro and outro
    ffmpeg -i "intro_with_text.mp4" -f lavfi -i aevalsrc=0 -shortest -c:v libx264 -c:a aac -y "intro_with_text_and_audio.mp4"
    ffmpeg -i "{OUTRO}" -f lavfi -i aevalsrc=0 -shortest -c:v libx264 -c:a aac -y "outro_with_audio.mp4"

    # Cut out the talk segment from the recording
    ffmpeg -i "{recording}" -ss "{start_time}" -to "{end_time}" -c:v libx264 -c:a aac -y talk_segment.mp4

    # Combine intro, talk segment, and outro
    ffmpeg -f concat -safe 0 -i <(printf "file '$PWD/%s'\\n" "intro_with_text_and_audio.mp4" "talk_segment.mp4" "outro_with_audio.mp4") -c:v copy -c:a copy -y {output}
    """

    return ffmpeg_command


if __name__ == "__main__":
    # Do a test run

    title = "Test title overlay with FFMPEG very long long long"
    author = "Peter Kalverla (Netherlands eScience Center)"

    recording = "sample_recording.mp4"
    start = "00:00:14"
    end = "00:00:19"

    output_file = "test.mp4"

    script = generate_ffmpeg_script(title, author, recording, start, end, output_file)
    subprocess.run(script, shell=True, executable="/bin/bash")

    # TODO: also wrap/abbreviate authors?
