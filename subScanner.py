import requests
from requests.packages import urllib3
urllib3.disable_warnings()


def find_team(domain, iters):

    i = 0
    successful_conn = []
    with open("domains.txt", "r", encoding="UTF-8") as domains:
        for line in domains:
            if i >= iters:
                break
            try:
                i += 1
                URL = "https://{}{}".format(domain, line)
                page = requests.get(URL, verify=False)
                print("Scan {} of {} returned a code of:".format(i, line), page)

                print("Page data:\t", page)
                page_response = page.status_code

                if (page_response == 200):
                    print("Successful Connection!!")
                    successful_conn.append(line)

            except requests.exceptions.InvalidURL:
                print(f"{line} Not Found :-(")

            except requests.exceptions.TooManyRedirects:
                URL = "https://{}{}".format(domain, line)
                page = requests.get(URL, verify=False, allow_redirects=False)
                print("Scan {} of {} returned a code of:".format(i, line), page)

                print("Page data:\t", page)
                page_response = page.status_code

                if (page_response == 200):
                    print("Successful Connection!!")
                    successful_conn.append(line)


    print(f"Successful Connections to {URL}:\n")
    for x in successful_conn:
        print(x)

def main():

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
        print("Please enter the number of domains to scan.")
    find_team(to_scan, iters)


if __name__ == "__main__":
    main()
