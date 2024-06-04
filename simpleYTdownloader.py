from pytube import YouTube
from pytube.exceptions import VideoUnavailable, PytubeError, RegexMatchError, LiveStreamError
from tqdm import tqdm
import os

# Add your path where the file should be downloaded.
outputPath = "/path/to/download"

def download_with_progress(stream, output_path, filename):
    # Get total size of the video
    total_size = stream.filesize
    
    # Start the progress bar
    with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename, ascii=True) as pbar:
        try:
            # Download the file to a temporary location
            temp_file_path = os.path.join(output_path, filename + ".temp")
            stream.download(output_path=output_path, filename=filename + ".temp")
            
            # Move the file to the final destination, updating the progress bar
            with open(temp_file_path, 'rb') as src, open(os.path.join(output_path, filename), 'wb') as dst:
                while True:
                    chunk = src.read(1024)
                    if not chunk:
                        break
                    dst.write(chunk)
                    pbar.update(len(chunk))
            
            # Remove the temporary file
            os.remove(temp_file_path)
        except Exception as e:
            print(f"An error occurred during download: {e}")

def downloadVideo():
    vidLink = str(input("Enter a YT link: "))
    try:
        yt = YouTube(vidLink)
        # Getting all video streams
        video_streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        highestResolution = video_streams.first()

        # Downloading the file
        if highestResolution:
            print(f"Downloading {yt.title}...")
            download_with_progress(highestResolution, outputPath, f"{yt.title}.mp4")
            print("Download Successful!")
        else:
            print("No video streams available for this video.")

    # Handling Exceptions
    except VideoUnavailable:
        print(f"Video {vidLink} is unavailable. Skipping.")
    except RegexMatchError:
        print("Error: Invalid YouTube URL.")
    except LiveStreamError:
        print("Error: Cannot download live streams.")
    except PytubeError as e:
        print("An error occurred:", e)

def downloadAudio():
    audioLink = str(input("Enter a YT link: "))
    try:
        yt = YouTube(audioLink)
        # Getting all audio Streams
        audioStream = yt.streams.filter(only_audio=True).first()

        # Downloading the file
        if audioStream:
            print(f"Downloading audio for {yt.title}...")
            download_with_progress(audioStream, outputPath, f"{yt.title}.mp3")
            print("Download Successful!")
        else:
            print("No audio streams available for this video.")

    # Handling Exceptions
    except VideoUnavailable:
        print(f"Video {audioLink} is unavailable. Skipping.")
    except RegexMatchError:
        print("Error: Invalid YouTube URL.")
    except LiveStreamError:
        print("Error: Cannot download live streams.")
    except PytubeError as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    choice = input("Download (v)ideo or (a)udio? ")
    if choice.lower() == 'v':
        downloadVideo()
    elif choice.lower() == 'a':
        downloadAudio()
    else:
        print("Invalid choice. Please select 'v' for video or 'a' for audio.")
