"""crawling 8k files
"""
import os
import sys
import urllib

def crawl_8k():
    f = open('./statsEDGAR.dat', 'r')
    lines = f.readlines()
    f.close()
    lines = lines[1:]

    match_file = open('matched.8k', 'w')

    save_dir = './8k/'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)

    line_index = 0
    for line in lines:
        if line_index % 20 == 0:
            print('processing: %d/%d'%(line_index, len(lines)))
        line_index += 1
        line_arr = line.split(',')
        has_8k = line_arr[5].strip(' ')
        if has_8k == '0':
            continue
        cik = line_arr[2].strip(' ')
        dat_file_name = line_arr[0]
        dat_file_name_arr = dat_file_name.split('/')
        dir_name = dat_file_name_arr[2]
        if not os.path.exists(save_dir + dir_name):
            os.mkdir(save_dir + dir_name)
        dir_full_name = save_dir + dir_name + '/' + cik + '/'
        if not os.path.exists(dir_full_name):
            os.mkdir(dir_full_name)
        dat_file = open(dat_file_name, 'r')
        dat_lines = dat_file.readlines()
        dat_file.close()

        for dat_line in dat_lines:
            dat_line = dat_line.strip('\n')
            dat_line_arr = dat_line.split(',')
            if '8K' in dat_line_arr[2] or '8-K' in dat_line_arr[2]:
                save_name = dir_full_name + dat_line_arr[3].strip(' ')
                url_str = 'http://www.sec.gov/Archives/'+dat_line_arr[4]
                urllib.urlretrieve(url_str, save_name)
                match_file.writelines(save_name + '\n')

    match_file.close()

if __name__=='__main__':
    crawl_8k()
