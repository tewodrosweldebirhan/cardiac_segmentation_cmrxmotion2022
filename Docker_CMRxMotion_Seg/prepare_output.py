'''

Rename the files correctly
Arrange the files into a folder

Submission.zip
Output_folder
        ID.nii.gz
        ID.nii.gz

    ...

'''

import shutil
import os
import SimpleITK as sitk
import numpy as np

#Parameters

CMRxMotion_method = "3d_1000_fullres_CMRxMotion_ACDC_MoreMotion_Loss_DicePolyCE_Splits_bestmodel"

output_folder = os.getenv("OUTPUTDIR")

CMRxMotion_foldername = '/nnUNet/all_data/nnUNet_raw/nnUNet_raw_data/Task500_CMRxMotion/testset_predictions/'+CMRxMotion_method+ '_all/'+CMRxMotion_method+'/'

subjlist = os.listdir(CMRxMotion_foldername)

#filter only .nii.gz
subjlist = [sb for sb in subjlist if sb.endswith('.nii.gz')]

subjlist.sort()

submission_folder = output_folder #os.path.join(output_folder, 'Submission_Task1')
if not os.path.isdir(submission_folder):
    os.makedirs(submission_folder)

for n, subj in enumerate(subjlist):

    if subj.endswith('.nii.gz'):

        imagename_SA = os.path.join(CMRxMotion_foldername, subj)
        shutil.copy(imagename_SA, os.path.join(submission_folder, subj))













