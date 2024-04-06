import youtube_download as youtube_download
import mp3_convert as mp3_convert


links = youtube_download.input_links()
for link in links:
    print("Downloading...")
    filename = youtube_download.download_video(link, 'low')
    print("Converting...")
    mp3_convert.convert_to_mp3(filename)