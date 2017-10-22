from bs4 import BeautifulSoup
import requests
import sys
import re


base_url = 'https://www.codechef.com/users/'
yes = {'yes', 'y', 'ye', ''}
no = {'no', 'n'}

def checkuser():
    username = raw_input('Enter the username : ')
    url = base_url + username
    r = requests.head(url)
    if r.status_code == 200:
        print 'Wait, getting your details.....'
        getdetails(url)
    else:
        print 'Invalid username'
        checkuser()

def getdetails(url):
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    rating = soup.find_all('div', class_="rating-number")[0].string
    globalrank = soup.findAll('a', href=re.compile('/ratings/all'))[4].string
    countryrank = soup.findAll('a', href=re.compile('/ratings/all'))[5].string

    print "User has %r rating, %r globalrank, %r countryrank " % (rating, globalrank, countryrank)

    choice = raw_input('Do you want to continue?(y/n) ').lower()
    if choice in yes:
        checkuser()
    elif choice in no:
        print "Thanks for using"
    else:
        sys.stdout.write("Please respond with 'yes' or 'no'")


if __name__ == '__main__':
    checkuser()

