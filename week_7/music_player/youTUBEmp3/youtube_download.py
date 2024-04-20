import pytube

def download_video(url, resolution):
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download()
    return stream.default_filename

def choose_resolution(resolution):
    if resolution in ["low", "360", "360p"]:
        itag = 18
    return itag


def input_links():
    print("Enter the link of the video (end by entering 'STOP'):")
    links = []
    link = ""
    while link != "STOP":
        link = input()
        links.append(link)
    links.pop()
    return links