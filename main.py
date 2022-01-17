from time import sleep
import byu_scrape, SMS

auction_url = 'https://purchasing.byu.edu/surplus/automobiles'
purchase_url = 'https://purchasing.byu.edu/vehicles-to-be-sold-no-bid-required'

purchase_closed = byu_scrape.get_page(url=purchase_url, search_term='Sorry, there are currently no vehicles available in the "Surplus Vehicles to be Sold" category. Keep checking back with us.', search_by='h3')
auction_closed = byu_scrape.get_page(url=auction_url, search_term='Currently, there are no "Surplus Vehicles for Auction,"', search_by='span')



def main():
    purchase_notified = False
    auction_notified = False
    while True:
        if purchase_closed == False:
            if purchase_notified == False:
                print("texting about purchase...")
                SMS.sendSMS('BYU Vehicle Surplus', f'There are vehicles available for PURCHASE! \n\n{purchase_url}', '5034535511@tmomail.net')
                purchase_notified = True
            elif purchase_notified == True:
                pass
        elif purchase_closed == True:
            SMS.sendSMS('TEST', f'PURCHASE CLOSED \n\n{purchase_url}', '5034535511@tmomail.net')
            purchase_notified = False

        if auction_closed == False:
            if auction_notified == False:
                print("texting about auction...")
                SMS.sendSMS('BYU Vehicle Surplus', f'There are vehicles available for AUCTION! \n\n{auction_url}', '5034535511@tmomail.net')
                auction_notified = True
            elif auction_notified == True:
                pass
        elif auction_closed == True:
            SMS.sendSMS('TEST', f'AUCTION CLOSED \n\n{purchase_url}', '5034535511@tmomail.net')
            auction_notified = False
        sleep(60)


if __name__ == "__main__":
    main()