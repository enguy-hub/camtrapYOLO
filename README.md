# camtrapYOLO

These steps assume that YOLO batch processing created by vincentgong7 is already downloaded and installed - Details on how to install YOLO batch processing can be found here: https://github.com/vincentgong7/VG_AlexeyAB_darknet/blob/master/README.md


## Preparation steps:

A1. Put all the images you wish to classify in one folder with an appropriate organizational scheme and naming convention. As an example:

```
/human 
```

A2. Move this folder to the "input" folder. As an example:

```
/input/human
``` 

A3. Create an output folder for the YOLO classified images inside the "output" folder with the same name as step A1.

```
/output/human
```


# YOLO batch processing steps:

B0. Activate "yolo" conda environment by using the below command in Terminal:

```
conda activate yolo
```

B1. Navigate to the "/VG_AlexeyAB_darknet" folder.

```
cd /VG_AlexeyAB_darknet
```

B2. Run the YOLO batch processing command below and adapt the paths to your specific usecase:

```
./darknet detector batch cfg/coco.data cfg/yolov4.cfg weights/yolov4.weights io_folders ../input/Human ../ouput/Human -out ../metadata/human_result_metadata.json -ext_output > ../metadata/human_result_metadata.txt
```
