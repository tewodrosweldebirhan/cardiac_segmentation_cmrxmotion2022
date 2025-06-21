#!/usr/bin/env python3
#
import os
import os.path as osp
import shutil

'''
Renaming the input images for CMRxMotion

'''

import SimpleITK as sitk
import glob

if __name__ == '__main__':

    count = 0
    nnunet_folder = os.getenv("nnUNet_raw_data_base")
    input_folder = os.getenv("INPUTDIR")
    imagesTs_folder_CMRxMotion = nnunet_folder + '/nnUNet_raw_data/' + 'Task500_CMRxMotion/' + "imagesTs/"

    if not osp.exists(imagesTs_folder_CMRxMotion):
        os.makedirs(imagesTs_folder_CMRxMotion)

    print("start renaming...")

    for case in os.listdir(input_folder):
        inputcase = os.path.join(input_folder, case)

        inputcase_nnunet = os.path.join(imagesTs_folder_CMRxMotion, case.replace(".nii.gz", "_0000.nii.gz") )
        shutil.copy(inputcase, inputcase_nnunet)

        count += 1

        print("{} files processed".format(count))
        print("Done")
