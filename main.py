import eBay_scrape

def main():
    #search_term = "dl380p+g8" # !!For Testing (should be commented out)!! #
    search_term = input('What item would you like to price check?\n').replace(' ', '+')
    url = f"https://www.ebay.com.au/sch/i.html?_from=R40&_nkw='{search_term}'&_sacat=31388&LH_TitleDesc=0&LH_Sold=1&LH_Complete=1&_ipg=200&rt=nc&LH_Auction=0&_ipg=200"
    #auction = input('Auctioned? (y/n)\n').lower()
    print(url)
    soup = get_data(url)
    products = parse(soup)
    export(products, search_term)