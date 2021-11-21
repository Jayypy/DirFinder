#imports
import requests, argparse
from art import *

#get arguments
my_parser = argparse.ArgumentParser()
my_parser.add_argument('-u', metavar='URL', type=str, help="Target URL where you want to find directories")
my_parser.add_argument('-w', metavar='Wordlist', type=str, help="Path to wordlist")

args = my_parser.parse_args()


url = args.u
wordlist = args.w

def find():
    with open(wordlist) as file:
        for line in file:
            dire = line.rstrip()
            try:
                x = requests.post(url +'/'+ dire + '/')
                if x.status_code == 200:
                    print(dire + " is a directory: " + url+'/'+dire)
            except:
                pass



def main():
    find()


if __name__ == '__main__':
    main()
