import eBay_scrape
import error_function
import target_item
import csv_logic

def main():
    mass_import = target_item.single_or_mass()
    csv_logic.csv_logic_main.appended = 0
    csv_logic.csv_logic_main.new_file = 0

    if mass_import == 0:
        single_item_check()

    else:
        mass_check()

    print('--------------------------------------------------------------\n')
    print(csv_logic.csv_logic_main.appended, ' old files updated\n')
    print(csv_logic.csv_logic_main.new_file, ' new files created\n')
    print('--------------------------------------------------------------\n')

def single_item_check():
    new_search = target_item.target_item()
    new_url = target_item.url(new_search)
    soup = eBay_scrape.get_data(new_url)
    products = eBay_scrape.parse(soup)
    appended, new_files = products_tested = csv_logic.csv_logic_main(products, new_search)
    # print(products_tested)
    return appended, new_files

def mass_check():

    num_items, new_search = target_item.mass_import()

    print(new_search)
    for items in new_search:
        #print(items)
        new_url = target_item.url(items)
        soup = eBay_scrape.get_data(new_url)
        products = eBay_scrape.parse(soup)
        csv_logic.csv_logic_main(products, items)
        #print(products_tested)



main()