# utf-8
import glob
import shutil
import os
import re


def move_year_month(in_path, count=0):
    for file in os.listdir(in_path):
        # print(file)
        res = re.match(r'(Screenshot_)*(\d{4})-*(\d{2})-*\d{2}.+\.png', file, re.IGNORECASE)
        if res:
            year = res.group(2)
            year_dir = os.path.join(pic_dir, year)
            if int(year) in range(2012, 2019):
                month = res.group(3)
                month_dir = os.path.join(year_dir, month)
                if not os.path.exists(month_dir):
                    os.makedirs(month_dir)
                    print('Folder Created: %s' % month_dir)
                fullname_src = os.path.join(in_path, file)
                fullname_dst = os.path.join(month_dir, file)
                if not os.path.exists(fullname_dst):
                    shutil.move(fullname_src, fullname_dst)
                else:
                    print('File already exists in the destination folder: %s' % file)
                print('File %s moved to %s' % (file, month_dir))
                count += 1
        else:
            # print('File does not match the pattern: %s' % file)
            pass

    return count


if __name__ == '__main__':
    pic_dir = r'C:\Users\Jing\OneDrive\Pictures\Camera Roll'
    i = 0
    i += move_year_month(pic_dir, i)
    # for year_no in range(2012, 2019):
    #     print('Current Year = %s' % year_no)
    #     year = str(year_no)
    #     i += move_year_month(os.path.join(pic_dir, year), i)

    print('%s files in total moved' % i)
