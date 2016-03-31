"""Analyze 8k files
"""

import os
import sys
import re

def analyze():
    word_list_file = open('./wordlist.dat', 'r')
    word_lines = word_list_file.readlines()
    word_lines = [line.strip('\n') for line in word_lines]
    word_list_file.close()

    matched_file = open('./matched.8k', 'r')
    matched_lines = matched_file.readlines()
    matched_file.close()

    outfile = open('./eightK_wordlist.dat', 'w')
    outfile.writelines('dir, cik, filename, words_count1, words_count2, words_count3, words_count4\n')
    line_index = 0
    for line in matched_lines:
        if line_index % 10 == 0:
            print('processing %d/%d'%(line_index, len(matched_lines)))
        line_index += 1
        line = line.strip('\n')
        line_arr = line.split('/')
        dir_name = line_arr[2]
        cik = line_arr[3]
        filename = line_arr[4]

        data_file = open(line, 'r')
        data_lines = data_file.readlines()
        data_str = ''
        for data_line in data_lines:
            data_str += data_line
        data_file.close()

        outfile.writelines('%s, %s, %s, '%(dir_name, cik, filename))

        for i in range(len(word_lines)):
            match_res = re.findall(word_lines[i], data_str, re.IGNORECASE)
            match_num = len(match_res)
            if i == len(word_lines) - 1:
                outfile.writelines('%d\n'%(match_num))
            else:
                outfile.writelines('%d, '%(match_num))

    outfile.close()

if __name__=='__main__':
    analyze()
