'''creating directory structure, every directory has 500 files, named by CIK
'''

import os
import sys

def create_directory():
    dir_num = 0
    file_num = 0
    cik2dir_name = {}
    dir_name = '000'
    root_dir = './data/'
    if not os.path.exists(root_dir + dir_name):
        os.mkdir(root_dir + dir_name)

    outer_index = 0
    inner_index = 0

    for filename in os.listdir('./masters'):
        f = open('./masters/' + filename)
        lines = f.readlines()
        f.close()

        for line in lines:
            if not line.endswith('txt\n'):
                continue
            if inner_index % 10000 == 0:
                print("processing master %d, line %d"%(outer_index, inner_index))
            inner_index += 1

            line_arr = line.split('|')
            cik = line_arr[0]

            ### replace ',' with ';', replace '|' with ','
            line = line.replace(',', ';')
            line = line.replace('|', ',')

            if cik in cik2dir_name:
                cik_f = open(root_dir + cik2dir_name[cik] + '/' + cik + '.dat', 'a')
                cik_f.writelines(line)
                cik_f.close()
                continue
            
            ### create new file in an existing directory, which has less than 500 files 
            if file_num <= 499:
                f = open(root_dir + dir_name + '/' + cik + '.dat', 'a')
                f.writelines(line)
                f.close()
                file_num += 1
                cik2dir_name[cik] = dir_name
                continue
            
            ### current directory has 500 files, new directory is needed.
            dir_num += 1
            dir_name = "%03d"%(dir_num)
            if not os.path.exists(root_dir + dir_name):
                os.mkdir(root_dir + dir_name)
            file_num = 0
            f = open(root_dir + dir_name + '/' + cik + '.dat', 'a')
            f.writelines(line)
            f.close()
            cik2dir_name[cik] = dir_name
            file_num += 1
        outer_index += 1

if __name__=='__main__':
    create_directory()
