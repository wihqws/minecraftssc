from mcstatus import JavaServer
import colorama
colorama.init(True)
from time import sleep as wait
from os import system as cmd
print('Minecraft Server Checker')
print(f'{colorama.Fore.YELLOW}(only java servers)\n\n')
wait(1)

def check():
    print('Enter ip:')
    ip = input()
    print('Enter port: (by default 25565)')
    port = input()
    if ip or port != None:
        cmd('cls')
        server = JavaServer.lookup(f'{ip}:{port}')
        status = server.status()
        print(f'The server has {colorama.Fore.GREEN}{status.players.online}{colorama.Fore.RESET} players online, replied in {colorama.Fore.GREEN}{status.latency}{colorama.Fore.RESET} ms')
        cmd('pause')
    else:
        print(f'{colorama.Fore.RED}Ip or port is None')


if __name__ == '__main__':
    check()