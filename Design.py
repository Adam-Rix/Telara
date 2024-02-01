from art import tprint
from colorama import init, Fore


def read_ascii_art(filename):
    with open(filename, 'r') as file:
        ascii_art = file.read()
    return ascii_art

def colorize_ascii_art(ascii_art, color):
    colored_art = color + ascii_art + Fore.RESET
    return colored_art

init(autoreset=True)

filename = 'resourses/spider.txt'
spider_art = read_ascii_art(filename)

green_spider_art = colorize_ascii_art(spider_art, Fore.GREEN)

print(green_spider_art)
tprint("TELARA", space = 2)
