"""Download master files from SEC.

The master file url is like:
"ftp://ftp.sec.gov/edgar/full-index/2011QTR3/master.gz"

Example:
    $ python download_master_files.py start_year end_year
"""

import os
import sys
import urllib

def download(start_year, end_year):
    for year in range(start_year, end_year + 1):
        for i in range(1,5):
            print("downloading mater file of %dQTR%d: "%(year, i))
            url = "ftp://ftp.sec.gov/edgar/full-index/%d/QTR%d/master.gz" % (year, i)
            save_name = 'data/%dQTR%dmaster'%(year, i)
            urllib.urlretrieve(url, save_name)

if __name__=='__main__':
    if len(sys.argv) != 3:
        print("usage:python download_master_files.py start_year end_year")
        sys.exit()
    first_year = int(sys.argv[1])
    second_year = int(sys.argv[2])
    download(first_year, second_year)
