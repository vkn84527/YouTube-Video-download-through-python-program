from pytube import YouTube
link=input("Enter the link: ")
yt=YouTube(link)
print("Tittle",yt.title)
print("No. of viwes",yt.views)
print("Length of video",yt.length,"seconds")
print("Description :",yt.description)
print("Ratings:",yt.rating)
print(yt.streams)
print(yt.streams.filter(only_audio=True))
print(yt.streams.filter(only_video=True))
print(yt.streams.filter(progressive=True))
ys=yt.streams.get_highest_resolution()
ys.download()
print("download complete!!")
