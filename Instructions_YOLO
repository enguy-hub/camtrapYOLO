#######################
# These steps assume that YOLO batch processing created by vincentgong7 is already downloaded and installed - Details on how to install YOLO batch processing can be found here: https://github.com/vincentgong7/VG_AlexeyAB_darknet/blob/master/README.md

#######################
# Preparation steps prior to running YOLO batch processing:

A0. Put all the images you wish to classify in one folder with an appropriate organizational scheme and naming convention.
-> e.g: /TM_Human (TM = Tourismus Monitoring)

A1. Move this folder to the "Images" folder.
-> e.g: /LWF_YOLO/Images/TM_Human

A2. Create an output folder for the YOLO classified images inside the "YOLO_Output" folder with the same name as step 1a with an additional "YOLO_..." in the front
-> e.g: /LWF_YOLO/YOLO_Output/YOLO_TM_Human


#######################
# YOLO batch processing steps:

B0. Activate "yolo" conda environment by using the below command in Terminal:
-> conda activate yolo

B1. Navigate to the "/VG_AlexeyAB_darknet-master" folder.
-> cd /home/user/LWF/LWF_YOLO/VG_AlexeyAB_darknet-master

B2. Run the YOLO batch processing command below and adapt the paths to your specific usecase:
-> ./darknet detector batch cfg/coco.data cfg/yolov4.cfg weights/yolov4.weights io_folders ../path/to/images/to/be/classified/ ../path/to/YOLO_Output/folder/created/in/step/A3 -out ../path/to/YOLO_Output/folder/created/in/step/A3/YOLO_name_of_folder_result.json -ext_output > ../path/to/YOLO_Output/folder/created/in/step/A3/YOLO_name_of_folder_result.txt

-> e.g: ./darknet detector batch cfg/coco.data cfg/yolov4.cfg weights/yolov4.weights io_folders ../Images/TM_Human/ ../YOLO_Output/YOLO_TM_Human/ -out ../YOLO_Output/YOLO_TM_Human/result.json -ext_output > ../YOLO_Output/YOLO_TM_Human/result.txt


