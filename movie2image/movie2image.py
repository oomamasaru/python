import cv2
import os
from tqdm import tqdm

VIDEO_PATH = "01_dog.mp4"
OUTPUT_PATH = "images"
OUTPUT_EXT = "jpg"

if __name__ == "__main__" :
    cap = cv2.VideoCapture(VIDEO_PATH)

    if not cap.isOpened() :
        exit
    
    os.makedirs(OUTPUT_PATH,exist_ok=True)

    frame_cnt = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    digit = len(str(frame_cnt))

    cnt = 1
    for image_index in tqdm(range(1,frame_cnt)) :
        ret, frame = cap.read()
        if not ret :
            break
        
        output_file_name = f"{os.path.join(OUTPUT_PATH,str(cnt).zfill(digit))}.{OUTPUT_EXT}"
        cv2.imwrite(output_file_name,frame)
        cnt += 1

