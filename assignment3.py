import argparse
import re
import csv
import urllib.request

file_url = ('http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv')

# Part I/II - Pulls and processes csv file
def downloadData(url):
    fetch_url = urllib.request.urlopen(url)
    data = fetch_url.read().decode('utf-8')
    file = data.splitlines()
    file_reader = csv.reader(file)
    csv_list = (list(file_reader))
    return csv_list

# Part III - Search csv for image type hits
def processImgData(file):

    img_hits = 0
    row_count = 0

    for line in file:
        print(line[0])
        row_count += 1
        img_search = re.search(r'jpg|gif|png|JPG|GIF|PNG', line[0], re.IGNORECASE)     # check for .jpg, .gif, .png
        if img_search:
            img_hits += 1

    img_percentage = (img_hits / row_count) * 100
    print(f'There are a total of {img_hits} image requests in this file')
    print(f'There are a total of {row_count} requests in this file')
    print(f'Image requests account for {img_percentage}% of all requests!')

def populartBrowser(file):

    browser = { 'Firefox' : 0,
                    'Chrome' : 0,
                    'Internet Explorer' : 0,
                    'Safari' : 0}

    for line in file:
        if re.search('Firefox', line[2]):
            browser['Firefox'] += 1
        elif re.search('Chrome', line[2]):
            browser['Chrome'] += 1
        elif re.search('Safari', line[2]):
            browser['Safari'] += 1
        elif re.search('Windows NT|MSIE', line[2]):
            browser['Internet Explorer'] += 1


    pop_browser = max(browser, key=browser.get)
    print(f'The most popular browser is {pop_browser} with X users')

'''def main(url):
    print(f"Running main with URL = {url}...")
    pass'''

print(downloadData(file_url))
processImgData(downloadData(file_url))
populartBrowser(downloadData(file_url))


if __name__ == "__main__":
    """Main entry point"""
    #parser = argparse.ArgumentParser()
    #parser.add_argument("--url", help="URL to the datafile", type=str, required=True)
    #args = parser.parse_args()
    #main(args.url)
    
