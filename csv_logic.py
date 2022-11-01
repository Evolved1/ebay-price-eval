import os
import codecs
import csv
import pandas as pd

import utility


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

    appended = 0
    with codecs.open(csv_path, encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        old_data = [row for row in reader]

    for new_results in new_data:
        new_info = 0
        for old_results in old_data:
            if old_results != new_results:
                new_info = new_info + 1
        if new_info != len(old_data):
            old_data.append(new_results)
            appended = appended + 1

    print(f'{utility.bcolors.WARNING}{utility.bcolors.BOLD}', 'Updated ', appended, ' new items', f'{utility.bcolors.ENDC}\n')
    return appended

def export_new_csv(product_list, search_term):
    productsdf = pd.DataFrame(product_list)
    csv_name = str(search_term) + '.csv'
    csv_path = os.getcwd() + '\\Library\\' + csv_name
    productsdf.to_csv(csv_path, index=False)
    print(f'{utility.bcolors.WARNING}{utility.bcolors.BOLD}', 'CSV saved with ', len(product_list), ' items', f'{utility.bcolors.ENDC}\n')
    return 1


#global var
csv_logic_main.appended = 0
csv_logic_main.new_file = 0
