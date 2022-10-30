import eBay_scrape
import error_function
import target_item

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
    num_items, new_search = target_item.mass_import()
    for items in new_search:
        new_url = target_item.url(items)
        soup = eBay_scrape.get_data(new_url)
        products = eBay_scrape.parse(soup)
        eBay_scrape.export(products, items)

main()