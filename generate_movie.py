from moviepy.editor import (
    VideoFileClip,
    TextClip,
    CompositeVideoClip,
    concatenate_videoclips,
)


INTRO = "ems_intro.mp4"
OUTRO = "ems_outro.mp4"


def generate_video(recording, start, end, title, author, session, output):
    talk = VideoFileClip(recording).subclip(start, end)
    print(talk.size)
    intro = VideoFileClip(INTRO)
    outro = VideoFileClip(OUTRO)

    margin = 50
    spacing = 10

    overlay_session = (
        TextClip(
            session,
            fontsize=30,
            color="white",
            method="caption",  # for auto-wrapping
            align="West",
            size=(intro.w - 2 * margin, None),
        )
        .set_start(4)
        .set_end(intro.end)
        .crossfadein(1)
        .set_position((margin, intro.h / 2))
        # .margin(margin, opacity=0)
    )
    overlay_title = (
        TextClip(
            title,
            fontsize=70,
            color="white",
            method="caption",
            align="West",
            size=(intro.w - 2 * margin, None),
        )
        .set_start(4)
        .set_end(intro.end)
        .crossfadein(1)
        .set_position((margin, intro.h / 2 + overlay_session.h + spacing))
        # .margin(margin, opacity=0)
    )
    overlay_author = (
        TextClip(
            author,
            fontsize=50,
            color="white",
            method="caption",
            align="West",
            size=(intro.w - 2 * margin, None),
        )
        .set_start(6)
        .set_end(intro.end)
        .crossfadein(1)
        .set_position(
            (margin, intro.h / 2 + overlay_session.h + overlay_title.h + 2 * spacing)
        )
        # .margin(margin, opacity=0)
    )

    intro_with_text = CompositeVideoClip(
        [intro, overlay_session, overlay_title, overlay_author]
    )

    talk_sandwich = talk.crossfadein(1).crossfadeout(1).audio_fadeout(1)

    result = concatenate_videoclips(
        [intro_with_text.resize(talk.size), talk_sandwich, outro.resize(talk.size)],
        # padding=-1,  # Doesn't look good on crossfadeout
        method="compose",  # slower, but otherwise crossfade doesn't work
    )
    result.write_videofile(output)
    return


if __name__ == "__main__":
    generate_video(
        recording="sample_recording.mp4",
        start="00:00:40",
        end="00:00:50",
        title="Test title overlay with FFMPEG very long long long",
        author="Peter Kalverla (Netherlands eScience Center)",
        session="UP4.1 - Urban stuffz",
        output="test_moviepy.mp4",
    )


# Notes
#
# resize needs `pip install opencv-python` (https://github.com/Zulko/moviepy/issues/2072)
# Crossfade needs compose: https://www.reddit.com/r/moviepy/comments/2f43e3/comment/ck7dzby/
# Set permissions for ImageMagick: https://github.com/Zulko/moviepy/issues/401#issuecomment-278679961
# Works with imagemagick v6 which is available on ubuntu channels (apt install). Alternatively, v7 is available via conda, but then I got problems with ffmpeg/fonts
# Quality?
