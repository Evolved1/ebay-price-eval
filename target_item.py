import error_function
import os


def single_or_mass():
    loop = [0,1,2,3,4]
    test = -1
    for i in loop:
        mass_import_choice = input('Would you like to do a mass price check?(y/n)\n').lower().strip()
        if 'y' in mass_import_choice or 'n' in mass_import_choice:
            test = i
            break
        else:
            print('Incorrect Input!')

    if test == -1:
        error_function.error_5()

    if mass_import_choice == 'y':
        mass_import()

    else:
        target_item()


def mass_import():
    csv_path = os.getcwd() + 'Target eBay items.csv'


def target_item():
    # search_term = "dl380p+g8" # !!For Testing (should be commented out)!! #
    search_term = input('What item would you like to price check?\n').replace(' ', '+')
    return search_term


def url(search_term):
    # auction = input('Auctioned? (y/n)\n').lower()
    auction = 0
    url = f"https://www.ebay.com.au/sch/i.html?_from=R40&_nkw='{search_term}'&_sacat=31388&LH_TitleDesc=0&LH_Sold=1&LH_Complete=1&_ipg=200&rt=nc&LH_Auction='{auction}'&_ipg=200"
    print(url)
    return url
