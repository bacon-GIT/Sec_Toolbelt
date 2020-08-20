import logging
import threading
import time
import requests
import sys
from requests.packages import urllib3

# Program Settings
urllib3.disable_warnings()
# Color Settings
TGREEN = '\033[32m' #   Green Text
TRED = '\033[35m' #     Red Text
ENDC = '\033[m' #       Reset Shell color


def scan_domain(domain, i, line):

    flag = True
    try:
        URL = "https://{}{}".format(domain, line)
        page = requests.get(URL, verify=False, allow_redirects=flag)
        print("Scan {} of {} returned a code of:".format(i, line), page)

        print("Page data:\t", page)
        page_response = page.status_code

        print(page.status_code)

        if page_response == 200:
            print(TGREEN + "Successful Connection!!", ENDC)
            return line
        else:
            print(TRED + "Page not found.", ENDC)

    except requests.exceptions.InvalidURL:
        logging.warning(TRED + f"{line} Not Found :-(", ENDC)

    except requests.exceptions.TooManyRedirects:
        flag = False


def main():

    try:
        if ('d' or 'Debug') in sys.argv[1]:
            print("Debugging on!")
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    except IndexError:
        print("Debugging off, launch SubScanner with -d to turn it on.")

    banner = TGREEN + '''
 _______           ______   _______  _______  _______  _        _        _______  _______ 
(  ____ \|\     /|(  ___ \ (  ____ \(  ____ \(  ___  )( (    /|( (    /|(  ____ \(  ____ )
| (    \/| )   ( || (   ) )| (    \/| (    \/| (   ) ||  \  ( ||  \  ( || (    \/| (    )|
| (_____ | |   | || (__/ / | (_____ | |      | (___) ||   \ | ||   \ | || (__    | (____)|
(_____  )| |   | ||  __ (  (_____  )| |      |  ___  || (\ \) || (\ \) ||  __)   |     __)
      ) || |   | || (  \ \       ) || |      | (   ) || | \   || | \   || (      | (\ (   
/\____) || (___) || )___) )/\____) || (____/\| )   ( || )  \  || )  \  || (____/\| ) \ \__
\_______)(_______)|/ \___/ \_______)(_______/|/     \||/    )_)|/    )_)(_______/|/   \__/
                                                                                          ''' + ENDC
    print(banner)

    to_scan = input("Please Enter A Domain:\t\t")
    while True:
        try:
            iters = int(input("Number of domains to try:\t"))
            break
        except ValueError:
            logging.error("Please enter the number of domains to scan.")
    flag = True
    i = 1
    successful_conn = []

    threads = list()

    with open("domains.txt", "r", encoding="UTF-8") as domains:
        for line in domains:
            if i > iters:
                break
            if scan_domain(to_scan, i, line):
                successful_conn.append(line)
            i += 1

    for x in successful_conn:
        print("~~~~~~~~~~~")
        print(TGREEN + x)

if __name__ == "__main__":
    main()
