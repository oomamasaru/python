import os
import matplotlib.pyplot as plt
from PIL import Image

# `00001.jpg`のような形式でJPEGに変換されたフレームファイルが格納されているディレクトリ
video_dir = "input/dog_images"

# ディレクトリ内のJPEGファイルをスキャンする
frame_names = [
    p for p in os.listdir(video_dir)
    if os.path.splitext(p)[-1] in [".jpg", ".jpeg", ".JPG", ".JPEG"]
]
frame_names.sort(key=lambda p: int(os.path.splitext(p)[0]))

# 最初のフレームを matplotlib で表示する
frame_idx = 0
plt.figure(figsize=(9, 6))
plt.title(f"frame {frame_idx}")
plt.imshow(Image.open(os.path.join(video_dir, frame_names[frame_idx])))
plt.show()