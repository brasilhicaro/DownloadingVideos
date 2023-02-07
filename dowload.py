from pytube import YouTube

def printDowloadVideo():
    global yt
    print('dowloading' + yt.title)

#Input a path using '/'
path = ''       
option:str = '' 
while(option != 'exit'):
    link:str = input("input link here: ")
    yt = YouTube(link)
    stream = yt.streams

    option = input('Type...'+
    '\n1 - To download a video'+
    '\n2 - To dowload a audio\n'+
    'or \'exit\' to leave program ')

    if option != '1' and option != '2' or 'exit':
        print('select a valid option')
        
    
    elif option =="1":
        printDowloadVideo
        stream = yt.streams.get_highest_resolution()
        #Input a path
        stream.download(output_path= path)
        print('download complete')
    else:
        printDowloadVideo
        stream = yt.streams.get_audio_only('mp4')
        stream.download(output_path= path)
