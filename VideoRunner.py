"""this Program Need A Powerful Server for Using CPU and RAM"""
import subprocess
from moviepy.editor import VideoFileClip


def Streaming(Address):
    input_file = Address
    output_dir = "static/Stream"  # replace with your output directory

    # Calculate FPS from the video file
    clip = VideoFileClip(input_file)
    fps = clip.fps

    # Create a subprocess to run ffmpeg command
    command = [
        "ffmpeg",
        "-i", input_file,  # use the -i option to specify the input file
        "-c:v", "libx264",  # Video Codec
        "-pix_fmt", "yuv420p",
        "-preset", "ultrafast",  # it's fast and Large file
        "-g", str(fps),  # in this case: 23.976
        "-b:v", "2500k",  # Video Bitrate(Its Can Change By Your Clients Internet Speed)
        "-c:a", "aac",  # Audio Codec
        "-ar", "44100",  # Audio Frequents
        "-threads", "0",
        "-bufsize", "512k",  # Bitrate Size
        # Add these options for HLS output
        "-f", "hls",  # format: HTTP Live Streaming
        "-hls_time", "5",
        "-hls_wrap", "10",
        f"{output_dir}/live.m3u8"
    ]

    proc = subprocess.Popen(command)

    # Wait for the subprocess to finish
    proc.wait()


Streaming("static/Movies/Pride.and.Prejudice.2005.720p.YIFY.mkv")  # Wget Your Video Files On ThisLocatio
