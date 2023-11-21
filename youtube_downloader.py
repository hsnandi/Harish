from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download(output_path)

        print(f"Video downloaded successfully to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# usage:
video_url = "https://www.youtube.com/watch?v=6BVJEcsq5U4"
download_video(video_url, "/path/to/save/video")
