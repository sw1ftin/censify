from spotify import make_playlist
import os
from colorama import init, Fore

init()


def clear_console():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


print(
    Fore.WHITE + ' ░▒▓██████▓▒░░▒▓████████▓▒░▒▓███████▓▒░ ░▒▓███████▓▒░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ \n' +
    Fore.WHITE + '░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n' +
    Fore.BLUE + '░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ \n' +
    Fore.BLUE + '░▒▓█▓▒░      ░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░▒▓██████▓▒░  ░▒▓██████▓▒░  \n' +
    Fore.BLUE + '░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     \n' +
    Fore.RED + '░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     \n' +
    Fore.RED + ' ░▒▓██████▓▒░░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒░         ░▒▓█▓▒░     \n' +
    Fore.RESET +
    '''
    
   Welcome to Censify!
   
   (Please fill out the `config.ini` first)
   ''')

url = input('Enter playlist URL: ')
name = input('Enter new playlist name: ')
public = input('Do you have public playlist? (y/n): ').lower()

clear_console()
make_playlist(name=name, playlist_url=url, public=public == 'y' or '')
clear_console()
print('Playlist created successfully.')
