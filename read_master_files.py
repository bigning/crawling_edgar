"""Program 3, reading the master files
"""

import os,sys

def read_masters():
    master_path = './data/'

    form_type_file = open('./formtypesEDGAR.dat', 'w')
    stat_file = open('./statsEDGAR.dat', 'w')

    stat_file.writelines('id, nums, cik, 10k, 10q, 8k, 6k, 4k, 13g, 13d, 13f, code424b\n')

    file_index = 0
    dir_index = 0

    for dir_name in os.listdir(master_path):
        if not os.path.isdir(master_path + dir_name):
            continue
        print('processing directory: %d' %(dir_index))
        for dat_filename in os.listdir(master_path + dir_name + '/'):
            tenk = eightk = fourk = thirteeng = thirteend = 0
            sixk = tenq = thirteenf = code424b = 0

            f = open(master_path + dir_name + '/' + dat_filename, 'r')
            lines = f.readlines()
            f.close()

            cik = dat_filename[:-4]

            for line in lines:
                line = line.strip('\n')
                line_arr = line.split(',')
                line_arr[2] = line_arr[2].strip(' ')
                form_type_file.writelines(line_arr[2] + '\n')
                if (line_arr[2] == '4' or line_arr[2] == '4/A'):
                    fourk += 1
                if '10K' in line_arr[2] or '10-K' in line_arr[2]:
                    tenk += 1
                if '10Q' in line_arr[2] or '10-Q' in line_arr[2]:
                    tenq += 1
                if '8K' in line_arr[2] or '8-K' in line_arr[2]:
                    eightk += 1
                if '6K' in line_arr[2] or '6-K' in line_arr[2]:
                    sixk += 1
                if '13F' in line_arr[2]:
                    thirteenf += 1
                if '13G' in line_arr[2]:
                    thirteeng += 1
                if '13D' in line_arr[2]:
                    thirteend += 1
                if '424B' in line_arr[2]:
                    code424b += 1

            stat_file.writelines('%d, %d, %s, %d, %d, %d, %d, %d, %d, %d, %d, %d\n'
                    %(file_index, len(lines), cik, tenk, tenq, eightk, sixk, fourk, thirteeng, thirteend, thirteenf, code424b))
            file_index += 1
        dir_index += 1
    stat_file.close()
    form_type_file.close()


if __name__=='__main__':
    read_masters()
