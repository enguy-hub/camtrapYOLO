import os
import json
import shutil
import pandas as pd

from fnmatch import fnmatch

# ----------------------------------------------------------------------------------------------------------------------
#
# These are supporting function for the before and after performing "batch processing" using Microsoft MegaDetection.

# The functions are made primarily based on how the cameratrap images are stored on LWF's server, thus adjustment
# is needed when using the functions in other systems or computers.

# convertMD_toCSV_usrinput():
#       converts the output JSON file from MegaDetection batch processing into a CSV file that has six columns
#       "Image Name", "Location", "Station", "Session", "Predicted Category", and "Image Path".

# convertMD_toJSON_usrinput():
#       converts the output JSON file from MegaDetection batch processing into a new JSON file, which sorts each
#       image's JSON object into their according "Location", "Station", "Session", and "Predicted Category".
#
# ----------------------------------------------------------------------------------------------------------------------


def convertMD_toCSV_usrinput():
    """
     This function converts the "result json file from MegaDetection batch processing" to a CSV file. This CSV file
     sorts the images into six columns "Image Name", "Location", "Station", "Session", "Predicted Category",
     and "Image Path". The sorting is done primarily based on the name and the storing location path of each image in
     the "result json file from MegaDetection batch processing".

     When execute the function, it will first prompt the user to enter the absolute path of the "result json file from
     MegaDetection batch processing". Then it will ask the user to give a name and a path for the new output csv file.

     Parameters:
         usr_input_json (str): the absolute path and name of the "result json file from MegaDetection batch
         processing" (with .json)

         usr_output_csv (str): the absolute path and name (with .csv) of where the output csv file will be saved, if no
         path is given, the json file will be saved at the same directory as where this script is stored.

     Returns:

     Output:
         CSV file saved at where user defined in the "usr_output_csv" prompt

     """

    usr_input_json = str(input("Enter the absolute path (end with '.json') of the JSON file resulted from MegaDetection"
                               " batch processing: "))

    usr_output_csv = str(input("Give a path and a name of where the output json file will be saved (end with .csv): "))

    input_json = open(usr_input_json, 'r')
    json_info = json.load(input_json)

    df_json = pd.DataFrame()

    for firstObjects in range(len(list(json_info))):
        imagePath = list(json_info[firstObjects].values())[1]
        imageName = list(json_info[firstObjects].values())[1].split('/')[3]
        station = list(json_info[firstObjects].values())[1].split('/')[1]
        session = list(json_info[firstObjects].values())[1].split('/')[2]

        detected_box = list(json_info[firstObjects].values())[2]
        dectbox_numbers = len(detected_box)

        dect_category, confidence = [], []

        if dectbox_numbers != 0:

            for secondObjects in range(dectbox_numbers):
                dect_category.append(list(detected_box[secondObjects].values())[1])
                confidence.append(list(detected_box[secondObjects].values())[3])

        data = imageName, station, session, str(dectbox_numbers), dect_category, confidence, imagePath
        data = [list(data)]

        df_single = pd.DataFrame(data, columns=['imageName', 'Station', 'Session', 'amountofDetectionBoxes',
                                                'detectedCategory', 'Confidence', 'imagePath'])

        df_json = pd.concat([df_json, df_single])

        df_json.to_csv(usr_output_csv, index=False)


def sort_images_csv():  # input_path, csv_input
    """
    This function takes in the same directory path used in "json_creator_usrinput()" function and the absolute path
    to the CSV file created from "csv_converter_usrinput()" function to sort (by moving) the images into their according
    folders based on their "Predicted Category" values in the CSV file. The four categories folders are "Empty",
    "Animal" (for value 1), "Person" (for value 2), "Vehicle" (for value 2)

    When execute the function, it will first prompt the user to enter the directory path used in
    "json_creator_usrinput()" function. Then it will ask the user to enter the absolute path to the CSV file created
    from "csv_converter_usrinput()" function.

    Parameters:
        usr_input_dir (str): the absolute path of the same directory path used in "json_creator_usrinput()" function

        usr_input_csv (str): the absolute path to the CSV file created from "csv_converter_usrinput()" function.

    Returns:
        None

    Result:
        Images in the directory defined in "usr_input_dir" variable will be sorted (by moving) into their according
        categorical folders.

    """

    usr_input_dir = str(input("Enter absolute path (end with '/') of the same directory path used in "
                              "'json_creator_usrinput()' function : "))

    usr_input_csv = str(input("Enter absolute path (end with '.csv') to the CSV file created from "
                              "'csv_converter_usrinput()' function: "))

    old_path = []  # Old - original path of where the image files are currently in
    parent_path = []  # First half of the o_path (parent path) without the image name

    pattern = "*.JPG"

    for root, dirs, files in os.walk(usr_input_dir):
        for fname in files:
            if fnmatch(fname, pattern):
                org_path = os.path.join(root, fname)
                org_path = os.path.normpath(org_path)
                old_path.append(org_path)

                p_path = os.path.split(org_path)[0]
                p_path = os.path.normpath(p_path)
                parent_path.append(p_path)

    csv_file = pd.read_csv(usr_input_csv)
    df_csv = pd.DataFrame(csv_file)

    sub_folder = []  # Classified categories of each image

    for category in df_csv['Predicted Category'].tolist():
        if 'Empty' in category:
            predclass = 'Empty'
        elif '1' in category:
            predclass = 'Animal'
        elif '2' in category:
            predclass = 'Person'
        elif '3' in category:
            predclass = 'Vehicle'
        else:
            predclass = None
        sub_folder.append(predclass)

    new_path = []  # New - new path where the image files will be move to

    for p, s in zip(parent_path, sub_folder):
        new_img_path = os.path.join(p, s)
        new_img_path = os.path.normpath(new_img_path)
        os.makedirs(new_img_path, exist_ok=True) if not os.path.exists(new_img_path) else None
        new_path.append(new_img_path)

    # Make sorted copy of the images
    for o, n in zip(old_path, new_path):
        shutil.copy(o, n)
