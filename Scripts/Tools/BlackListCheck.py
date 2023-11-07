import requests
import json
import argparse
from bs4 import BeautifulSoup


def scrape_Listed(request):

    # Please generate your own API key
    apikey = 'chooseVoltaWeWontLeakYourAPIKEY'

    # Format to be used in django:
    # r = requests.get(f"https://www.spamcop.net/w3m?action=checkblock&ip={request.POST['IP_address']}")

    # VIRUSTOTAL (using API key, W.I.P)
    # The public API only allows for 4 queries per minute
    # Therefore this feature is temporarily disabled, just not disabled enough for me to refactor everything
    '''
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    params = {'apikey': apikey, 'ip': request}
    response = requests.get(url, params=params)
    report = response.json()
    report_dict = report['undetected_referrer_samples'][0]
    VirusTotalHits = report_dict['positives']
    '''
    VirusTotalHits = "N/a"


    # SPAMCOP
    r = requests.get(f"https://www.spamcop.net/w3m?action=checkblock&ip={request}")
    soup = BeautifulSoup(r.content, "html.parser")

    # This checks if an IP is routable or not, probably not entirely necessary but
    # useful since it catched private IP's without having to use a fat list of
    # registered private IP's,
    routable = True
    not_routable = soup.find("div", {"class": "warning"})
    if not_routable:
        routable = False

    # Spamcop returns "Listed" if registered
    spamcop = soup.findAll("p")
    spamcop = spamcop[0].get_text()
    if spamcop.split()[1] == "not":
        spamcop = "Not Listed"
    else:
        spamcop = "Listed"

    return spamcop, VirusTotalHits, routable


def scrape_IPAbuse(request):
    # Format to be used in django:
    # r = requests.get(f"https://www.abuseipdb.com/check/{request.POST['IP_address']}")

    # Format for testing:
    r = requests.get(f"https://www.abuseipdb.com/check/{request}")

    soup = BeautifulSoup(r.content, "html.parser")
    a = soup.find("p")
    if not a:
        # Change {request} variable to {request.POST['IP_address']} when moved to MultiMeter
        return None
    else:
        bold = soup.findAll("b")
        time_reported = bold[6].get_text()
        confidence_level = bold[7].get_text()
        if confidence_level != 'AbuseIPDB':
            return time_reported, confidence_level


# IP DB Prototype:
IPS_REPORTED = {}


# This just adds entries to nested dictionary without any verbosity
def NO_UI():

    # For testing a large range of IP's to make sure there are no edge cases
    with open("assets/ips.txt", 'r') as ips:
        for line in ips:
            spamlists = scrape_Listed(line.rstrip())

            i = line.rstrip()
            j = scrape_IPAbuse(i)
            if j:
                # Insert entry into Dictionary
                IPS_REPORTED[i] = {"|\t\tTimesReported": j[0],
                                   "ConfidenceLevel": j[1],
                                   "VirusTotalHits": spamlists[1],
                                   "SpamCopListed": spamlists[0]}
            else:
                IPS_REPORTED[i] = {"Error": "No entry in IPAbuse database.",
                                   "VirusTotalHits": spamlists[1],
                                   "SpamCopListed": spamlists[0]}


# This one has colors and verbosity
def UI():
    # For testing a large range of IP's to make sure there are no edge cases
    with open("assets/ips.txt", 'r') as ips:
        for line in ips:
            print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(f"Now searching for {line.rstrip()}:")
            spamlists = scrape_Listed(line.rstrip())

            if spamlists[0] == "Not Listed":
                print(f"[-]\t\t{line.rstrip()} is not listed on SpamCop.")
            else:
                print(f"[+]\t\t{line.rstrip()} is listed on SpamCop.")

            # Routable Tests
            if spamlists[2]:
                print(f"[+]\t\t{line.rstrip()} is Routable.")
            else:
                print("[-]\t\tNot routable, probably a private IP.")
                continue

            i = line.rstrip()
            j = scrape_IPAbuse(i)
            if j:
                print("[+]\t\tAbuseIPDB Entry Found!")
                print(f"[*]\t\tTimes Reported: {j[0]}"
                      f"\n[*]\t\tConfidence Level: {j[1]}"
                      f"\n[*]\t\tVirus Total Hits: {spamlists[1]}"
                      f"\n[*]\t\tSpamCop Listed: {spamlists[0]}")

                # Insert entry into Dictionary
                IPS_REPORTED[i] = {"TimesReported": j[0],
                                   "ConfidenceLevel": j[1],
                                   "VirusTotalHits": spamlists[1],
                                   "SpamCopListed": spamlists[0]}
            else:
                print(f"[-]\t\t{i} does not have an entry in the IPAbuse database.")
                IPS_REPORTED[i] = {"Error": "No entry in IPAbuse database.",
                                   "VirusTotalHits": spamlists[1],
                                   "SpamCopListed": spamlists[0]}


def main():

    # Parse args
    parser = argparse.ArgumentParser(description="Choose whether to use UI or not.")
    parser.add_argument("-v",
                        action="store_true",
                        help="Use this to run with UI.")
    args = parser.parse_args()
    if args.v:
        UI()
    else:
        print("Checking ips.txt and parsing results to JSON...")
        NO_UI()

    # Export results to JSON
    with open("results.json", 'w') as res:
        json.dump(IPS_REPORTED, res, indent=4)


if __name__ == "__main__":
   main()
