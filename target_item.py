import utility
import os
import pandas as pd
import mpu.pd
import codecs
import csv
import numpy as np


#### single_or_mass function ####
# This function is a simple ask the user what they are after:
# y = mass import request
# n = one-time check
def single_or_mass():
    loop = [0, 1, 2, 3, 4]
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
        return 1

    else:
        return 0


#### mass_import function ####
## This function only runs if a mass-import is requested ##
# This code is frankly hacky
# It gets the location of the running code and finds a file called lookup_items.csv
# It then decodes the csv out of utf-8-sig which has the BOM in it
# Re-encodes it to UTF-8
# This creates a 2-d array of strings, which is not desired
# Numpy then 'ravel' it to make it a 1-d array
# Return number of items in the csv and the array itself
def mass_import():
    csv_name = 'lookup_items.csv'
    csv_path = os.getcwd() + '\\' + csv_name

    with codecs.open(csv_path, encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    # csv = pd.read_csv(csv_path, delimiter=',', header=1)
    # csv = csv.replace(' ', '+')
    # print(csv)

    data = np.array(data)
    data = data.ravel()

    cols = len(data)
    return cols, data

#### target_item function ####
## This function only runs if a one-time check is requested ##
# Simply asks the user what item they would like to check
def target_item():
    # search_term = "dl380p+g8" # !!For Testing (should be commented out)!! #
    search_term = input('What item would you like to price check?\n')
    return search_term

#### search_term function ####
## runs every iteration ##
# places the search term in the appropriate url
# this is returned to be scraped
# functionality for auction scraping not yet implememented but has been considered
def url(search_term):
    # auction = input('Auctioned? (y/n)\n').lower()
    search_term = search_term.replace(' ', '+')
    auction = 0
    url = f"https://www.ebay.com.au/sch/i.html?_from=R40&_nkw='{search_term}'&_sacat=31388&LH_TitleDesc=0&LH_Sold=1&LH_Complete=1&_ipg=200&rt=nc&LH_Auction='{auction}'&_ipg=200"
    print_url = utility.link(url)
    #print(print_url)
    return url
