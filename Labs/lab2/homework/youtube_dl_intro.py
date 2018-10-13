from youtube_dl import YoutubeDL


#Sample 1+2: Download a single youtube video
#/ dl = YoutubeDL()
#/ dl.download(['https://www.youtube.com/watch?v=Z3jhVHqd67g&t=1s'])

# Sample 3+5: Audio
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio', #download best quality audio
}
dl = YoutubeDL(options)
dl.download(['Isreal nash Rexanimarum'])


#Sample 4: Find + download
# options = {
#     'default_search': 'ytsearch',
#     'max_downloads': 1, # download the first video you found
# }

# dl = YoutubeDL(options)
# dl.download(['israel nash'])
