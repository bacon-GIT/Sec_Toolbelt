import logging
import threading
import time
import requests
import sys
from requests.packages import urllib3

# Program Settings
urllib3.disable_warnings()


def scan_domain(domain, iters):

    flag = True
    i = 0
    successful_conn = []
    with open("domains.txt", "r", encoding="UTF-8") as domains:
        for line in domains:
            if i >= iters:
                break
            try:
                i += 1
                URL = "https://{}{}".format(domain, line)
                page = requests.get(URL, verify=False, allow_redirects=flag)
                print("Scan {} of {} returned a code of:".format(i, line), page)

                print("Page data:\t", page)
                page_response = page.status_code

                if page_response == 200:
                    logging.info("Successful Connection!!")
                    successful_conn.append(line)

            except requests.exceptions.InvalidURL:
                logging.warning(f"{line} Not Found :-(")

            except requests.exceptions.TooManyRedirects:
                flag = False

    print(f"Successful Connections to: {URL}\n")
    print("The following returned successful connection attempts:")
    for x in successful_conn:
        print("~~~~~~~~~~~")
        print(x)


def main():

    try:
        if ('d' or 'Debug') in sys.argv[1]:
            print("Debugging on!")
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    except IndexError:
        print("Debugging off, launch SubScanner with -d to turn it on.")

    banner = '''
 _______           ______   _______  _______  _______  _        _        _______  _______ 
(  ____ \|\     /|(  ___ \ (  ____ \(  ____ \(  ___  )( (    /|( (    /|(  ____ \(  ____ )
| (    \/| )   ( || (   ) )| (    \/| (    \/| (   ) ||  \  ( ||  \  ( || (    \/| (    )|
| (_____ | |   | || (__/ / | (_____ | |      | (___) ||   \ | ||   \ | || (__    | (____)|
(_____  )| |   | ||  __ (  (_____  )| |      |  ___  || (\ \) || (\ \) ||  __)   |     __)
      ) || |   | || (  \ \       ) || |      | (   ) || | \   || | \   || (      | (\ (   
/\____) || (___) || )___) )/\____) || (____/\| )   ( || )  \  || )  \  || (____/\| ) \ \__
\_______)(_______)|/ \___/ \_______)(_______/|/     \||/    )_)|/    )_)(_______/|/   \__/
                                                                                          '''
    print(banner)

    to_scan = input("Please Enter A Domain:\t\t")
    try:
        iters = int(input("Number of domains to try:\t"))
    except TypeError:
        logging.error("Please enter the number of domains to scan.")
    scan_domain(to_scan, iters)


if __name__ == "__main__":
    main()
