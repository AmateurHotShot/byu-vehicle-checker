import requests
from bs4 import BeautifulSoup


def get_page(url, search_term, search_by):
    r_auction = requests.get(url)
    auction_soup = BeautifulSoup(r_auction.text, 'html.parser')
    auction_spans = auction_soup.find_all(search_by)

    term = search_term
    term_count = 0
    for span in auction_spans:
        if span.string == term:
            term_count += 1
    
    if term_count == 0:
        return False
    else:
        return True

if __name__ == '__main__':
    get_page(url='https://purchasing.byu.edu/surplus/automobiles', search_term='Currently, there are no "Surplus Vehicles for Auction,"', search_by='span')
