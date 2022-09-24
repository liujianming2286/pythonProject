# -*- coding: utf-8 -*-

import os
import string


def rename_file():
    file_list = os.listdir("test\\")
    i = 0
    for filename in file_list:
        i = i + 1
        if filename.endswith(".txt"):
            new_filename = "".join([i for i in filename if i if not i.isdigit()])
            new_filename = os.path.splitext(new_filename)[0] + format(str(i), '0>2s') + os.path.splitext(filename)[-1]
            print(new_filename)
            os.rename("test\\" + filename, new_filename)


rename_file()





