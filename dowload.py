from pytube import YouTube

def printDowloadVideo():
    global yt
    print('dowloading' + yt.title)

link:str = input("input link here: ")
#Input a path 
path = ''       

yt = YouTube(link)
stream = yt.strems
while(True):
    option = input('Press...'+
    '1 - To download a video'+
    '2 - To dowload a audio')

    if option != '1' and option != '2':
        print('select a valid option')
        
    
    elif option =="1":
        printDowloadVideo
        stream = yt.stream.get_highest_resolution()
        #Input a path
        stream.dowload(output_path= path)
        break
    else:
        printDowloadVideo
        stream = yt.stream.get_audio_only('mp4')
        stream.download(output_path= path)
        break
