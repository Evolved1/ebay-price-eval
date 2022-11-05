import os
import codecs
import csv
import pandas as pd
from datetime import date
import utility

#Global Variables
DATE_UPDATED = date.today()

def csv_logic_main(results, search_term):

    results = check_for_ghost(results)
    found_results = check_for_searches(results)
    if found_results:
        csv_path = check_if_csv_exists(search_term)
        if csv_path:
            csv_logic_main.appended += update_csv(results, csv_path)
        else:
            csv_logic_main.new_file += export_new_csv(results, search_term)


def check_for_ghost(results):
    if 'Shop on eBay' in str(results[0]):
        del results[0]

    #print(results[0])
    return results

def check_for_searches(results):
    if len(results) == 0:
        print(f'{utility.bcolors.FAIL}', 'No results found!', f'{utility.bcolors.ENDC}')
        return False
    else:
        return True


def check_if_csv_exists(search_term):

    csv_name = str(search_term) + '.csv'
    csv_path = os.getcwd() + '\\Library\\' + csv_name
    #print('\n\n\n\nTEST1\n\n\n\n')
    if os.path.exists(csv_path):
        print(f'{utility.bcolors.HEADER}', 'File found, updating!', f'{utility.bcolors.ENDC}')
        return csv_path
    else:
        print(f'{utility.bcolors.HEADER}', 'No File Found, creating csv...', f'{utility.bcolors.ENDC}')
        return False

def update_csv(new_data, csv_path):

    pending = []
    appended = 0
    with codecs.open(csv_path, encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        old_data = [row for row in reader]

    #if test_new_data():

    for new_results in new_data:
        found_flag = 0
        i = 0
        new_title = str(new_results["title"])
        new_date = str(new_results['sold_date'])

        for old_results in old_data:
            old_title = old_results[0]
            old_date = old_results[2]
            i = i + 1

            if old_title == new_title and old_date == new_date:
                found_flag += 1
                break

        if found_flag == 0:
            old_data.append(new_results)
            appended = appended + 1



    #old_data[len(old_data[0])]= DATE_UPDATED

    print(f'{utility.bcolors.WARNING}{utility.bcolors.BOLD}', 'Updated ', appended, ' new items', f'{utility.bcolors.ENDC}\n')
    return appended

def export_new_csv(product_list, search_term):
    #product_list[0].title = ('Date Updated:')
    #product_list[0].sold_price = (DATE_UPDATED)
    productsdf = pd.DataFrame(product_list)
    csv_name = str(search_term) + '.csv'
    csv_path = os.getcwd() + '\\Library\\' + csv_name
    productsdf.to_csv(csv_path, index=False)
    print(f'{utility.bcolors.WARNING}{utility.bcolors.BOLD}', 'CSV saved with ', len(product_list), ' items', f'{utility.bcolors.ENDC}\n')
    return 1


#global var
csv_logic_main.appended = 0
csv_logic_main.new_file = 0
