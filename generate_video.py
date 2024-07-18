from textwrap import wrap
import ffmpeg

intro_file = "ems_intro.mp4"
outro_file = "ems_outro.mp4"

input_file = "template.mp4"
output_file = "test.mp4"

talk_start = "00:00:14"
talk_end = "00:00:19"

talk_title = "Test title overlay with FFMPEG very long long long"
talk_author = "Peter Kalverla (Netherlands eScience Center)"

wrapped_title = wrap(talk_title, 50)

ffmpeg.concat(
    ffmpeg.input(intro_file)
    .drawtext(
        talk_title,
        x="w/2-tw/2",
        y="h/2-th/2",
        fontcolor="white",
        fontsize=48,
        # enable="between(t,1,4)",
        alpha="if(lt(t,1),0,if(lt(t,3),(t-1)/2,1))",
    )
    .drawtext(
        talk_author,
        x="w/2-tw/2",
        y="h/2-th/2+30",
        fontcolor="white",
        fontsize=24,
        # enable="between(t,1,4)",
        alpha="if(lt(t,4),0,if(lt(t,6),(t-4)/2,1))",
    ),
    ffmpeg.input(input_file, ss=talk_start, to=talk_end),
    ffmpeg.input(outro_file),
).output(output_file).run()
