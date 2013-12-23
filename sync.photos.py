#!/usr/bin/python

import os
import shutil

base_path = "P:\\"
target_path = "E:\photos test\\"
number_of_new_files = 0
number_of_directories = 0
number_of_new_directories = 0
number_of_directories_removed = 0
number_of_files_removed = 0
remove_files = ["Thumbs.db"]
video_files = ["mov", "mp4"]

if os.path.isdir(base_path) & os.path.isdir(target_path):

    for bRoot, bSubFolders, bFiles in os.walk(base_path):
        bDestination = bRoot.replace(base_path, target_path) + "\\"
        print("checking folder: {}".format(bRoot))
        number_of_directories += 1

        if os.path.isdir(bDestination) == False:
            os.mkdir(bDestination)
            print("created directory {}".format(bDestination))
            number_of_new_directories += 1

        for bFile in bFiles:
            bDestinationFile = bDestination + bFile
            if os.path.isfile(bDestinationFile) == False:
                shutil.copy(bRoot + "\\" + bFile, bDestination)
                number_of_new_files += 1
                print("copying file: {}".format(bFile))

    for dRoot, dSubFolders, dFiles in os.walk(target_path, False):
        dDestination = dRoot.replace(target_path, base_path) + "\\"
        print("checking folder: {}".format(dRoot))

        if os.path.isdir(dDestination) == False:
            if os.path.isdir(dRoot):
                shutil.rmtree(dRoot, True)
                print("removed directory {}".format(dRoot))
                number_of_directories_removed += 1

        if os.path.isdir(dRoot):
            for dFile in dFiles:
                if os.path.isfile(os.path.join(dRoot, dFile)):
                    dDestinationFile = dDestination + dFile

                    if os.path.isfile(dDestinationFile) == False:
                        os.remove(os.path.join(dRoot, dFile))
                        number_of_files_removed += 1
                        print("Removed file: {}".format(dFile))

else:
    print("directories are not valid")

print("{} directories checked".format(number_of_directories))
print("{} directories removed".format(number_of_directories_removed))
print("{} new files".format(number_of_new_files))
print("{} files removed".format(number_of_files_removed))
