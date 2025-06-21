#!/bin/bash

echo '==============================='
echo 'Prepare Input'
echo '==============================='
python /nnUNet/Docker_CMRxMotion_Seg/prepare_input_task.py

echo '==============================='
echo 'Run nnUnet Prediction'
echo '==============================='

#export CUDA_VISIBLE_DEVICES=0

# CMRxMotion segmentation

python /nnUNet/nnunet/inference/predict_simple.py -i $nnUNet_raw_data_base/nnUNet_raw_data/Task500_CMRxMotion/imagesTs/ -o $nnUNet_raw_data_base/nnUNet_raw_data/Task500_CMRxMotion/testset_predictions/3d_1000_fullres_CMRxMotion_ACDC_MoreMotion_Loss_DicePolyCE_Splits_bestmodel_all/3d_1000_fullres_CMRxMotion_ACDC_MoreMotion_Loss_DicePolyCE_Splits_bestmodel/ -tr nnUNetTrainerV2_Loss_DicePolyCE -m 3d_fullres -p nnUNetPlansv2.1 -t Task500_CMRxMotion

python /nnUNet/Docker_CMRxMotion_Seg/prepare_output.py
echo '==============================='
echo 'End of Prediction'
echo '==============================='
