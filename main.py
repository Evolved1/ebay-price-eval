import eBay_scrape
import error_function
import target_item
import csv_logic

def main():
    mass_import = target_item.single_or_mass()
    if mass_import == 0:
        single_item_check()

    else:
        mass_check()

def single_item_check():
    new_search = target_item.target_item()
    new_url = target_item.url(new_search)
    soup = eBay_scrape.get_data(new_url)
    products = eBay_scrape.parse(soup)
    eBay_scrape.export(products, new_search)

def mass_check():
    i = 0
    num_items, new_search = target_item.mass_import()

    print(new_search)
    for items in new_search:
        #print(items)
        new_url = target_item.url(items)
        soup = eBay_scrape.get_data(new_url)
        products = eBay_scrape.parse(soup)
        products_tested = csv_logic.check_for_ghost(products)
        #print(products_tested)
        eBay_scrape.export(products_tested, items)
        i = i + 1

main()