import logging
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
        print("Scan {} of {} returned a code of:".format(i, line.rstrip()), page)
        page_response = page.status_code

        if page_response == 200:
            print(TGREEN + "Successful Connection!!", ENDC)
            return line
        else:
            print(TRED + "Page not found.", ENDC)

    # Exceptions for invalid url's and too many redirects.
    # The flag for too many redirects is set to True by default,
    # as this is meant to catch edge cases where redirects return as
    # successful connections. Can't remember why right now, should probably write
    # documentation while actually writing the code. Don't pretend you're any better.

    except requests.exceptions.InvalidURL:
        logging.warning(TRED + f"{line} Not Found :-(", ENDC)
    except requests.exceptions.TooManyRedirects:
        flag = False


def main():

    # TODO:
    #   -Replace this method with argparse because this is just messy
    #   -Add verbosity flag to parse with argparse
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

    # Lists and integer declaration, timer for testing against threaded version.
    # (As of currently, threading does not make this program quicker, grequests might work though, haven't tried it yet)
    i = 1
    successful_conn = []
    start_time = time.perf_counter()
    
    # Main brain of program
    with open("assets/domains.txt", "r", encoding="UTF-8") as domains:
        for line in domains:
            if i > iters:
                break
            if scan_domain(to_scan, i, line):
                successful_conn.append(line)
            i += 1

    stop_time = time.perf_counter() - start_time
    print(f"~~~~~~~~~~\nCompleted in:\t{stop_time}\n~~~~~~~~~~~")

    for x in successful_conn:
        print("~~~~~~~~~~~")
        print(TGREEN + x)


if __name__ == "__main__":
    main()
