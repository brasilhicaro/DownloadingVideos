from pytube import YouTube

#Input a path using '/'
path = './media'       
option:str = '' 
while(option != 'exit'):
    option = input('Type...'+
    '\n1 - To download a video'+
    '\n2 - To dowload an audio\n'+
    'or \'exit\' to leave program \n')

    if option == 'exit':
        print('Bye!!!!')
        break
    
    link:str = input("input link here: ")
    yt = YouTube(link)
    stream = yt.streams


    if option != '1' and option != '2':
        print('select a valid option')
        
    elif option =="1":
        print('dowloading ' + yt.title)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path= path)
        print('download complete')
    else:
        print('dowloading ' + yt.title)
        stream = yt.streams.get_audio_only('mp4')
        stream.download(output_path= path)
        print('download complete')