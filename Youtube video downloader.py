from pytube import YouTube

link=input("Paste the link Here")
print("Video is downloading.....")
YouTube(link)
print("Video Downloaded Successfully")