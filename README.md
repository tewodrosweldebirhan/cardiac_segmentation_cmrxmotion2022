# cardiac_segmentation_cmrxmotion2022
Source code for our method which was ranked second (segmentation task) in Extreme Cardiac MRI Analysis Challenge under Respiratory Motion (CMRxMotion) MICCAI 2022 Challenge.

# Automatic Quality Assessment of Cardiac MR Images with Motion Artefacts using Multi-task Learning and K-Space Motion Artefact Augmentation

The movement of patients and respiratory motion during MRI acquisition produce image artefacts that reduce the image quality and its diagnostic value. 
Quality assessment of the images is essential to minimize segmentation errors and avoid wrong clinical decisions in the downstream tasks. In this paper, we propose 
automatic multi-task learning (MTL) based classification model to detect cardiac MR images with different levels of motion artefact. We also develop an automatic 
segmentation model that leverages k-space based motion artefact augmentation (MAA) and a novel compound loss that utilizes Dice loss with a polynomial version of 
cross-entropy loss (PolyLoss) to robustly segment cardiac structures from cardiac MRIs with respiratory motion artefacts. We evaluate the proposed method on 
Extreme Cardiac MRI Analysis Challenge under Respiratory Motion (CMRxMotion 2022) challenge dataset. For the detection task, the multi-task learning based model that 
simultaneously learns both image artefact prediction and breath-hold type prediction achieved significantly better results compared to the single-task model, showing 
the benefits of MTL. In addition, we utilized test-time augmentation (TTA) to enhance the classification accuracy and study aleatoric uncertainty of the images. 
Using TTA further improved the classification result as it achieved an accuracy of 0.65 and Cohen's kappa of 0.413. From the estimated aleatoric uncertainty, 
we observe that images with higher aleatoric uncertainty are more difficult to classify than the ones with lower uncertainty. For the segmentation task, the k-space 
based MAA enhanced the segmentation accuracy of the baseline model. From the results, we also observe that using a hybrid loss of Dice and PolyLoss can be advantageous 
to robustly segment cardiac MRIs with motion artefact, leading to a mean Dice of 0.9204, 0.8315, and 0.8906 and mean HD95 of 8.09 mm, 3.60 mm and 6.07 mm for LV, MYO and 
RV respectively on the official validation set. On the test set, the proposed segmentation method was ranked in second place in the segmentation task of CMRxMotion 2022 challenge.

Full paper: https://hal.archives-ouvertes.fr/hal-03880574

This work was supported by the French National Research Agency (ANR), with reference ANR-19-CE45-0001-
01-ACCECIT. Calculations were performed using HPC resources from DNUM CCUB (Centre de Calcul de l’Université
de Bourgogne) and from GENCI–IDRIS (Grant 2022-AD011013506). We also thank the Mesocentre of Franche-Comté for the
computing facilities.
