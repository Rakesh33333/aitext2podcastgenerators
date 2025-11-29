import ffmpeg_downloader

# This will download FFmpeg binaries if not already downloaded
ffmpeg_path = ffmpeg_downloader.load_ffmpeg()  # returns the path to ffmpeg.exe
print(ffmpeg_path)
