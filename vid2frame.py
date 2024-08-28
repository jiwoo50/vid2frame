import os
import cv2
from tkinter import filedialog
from tqdm import tqdm
def video_to_frames(input_dir,file_name, output_dir):
    input_loc=input_dir+"/"+file_name
    try:
        os.mkdir(input_loc)
    except OSError:
        pass
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    count = 0
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(output_dir +"/"+ file_name[:-4]+"_"+str(count)+".jpg", frame)
        count+=1
    cap.release()

if __name__=="__main__":
    input_dir=filedialog.askdirectory()
    output_dir=filedialog.askdirectory()
    file_list = os.listdir(input_dir)
    for file_name in tqdm(file_list) :
        video_to_frames(input_dir,file_name, output_dir)