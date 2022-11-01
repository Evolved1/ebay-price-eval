

def check_for_ghost(results):
    if 'Shop on eBay' in str(results[0]):
        del results[0]

    #print(results[0])
    return results

