import os
import cv2
import datetime
import numpy as np
import torch
import matplotlib.pyplot as plt
from sam2.build_sam import build_sam2_video_predictor

def show_mask(mask, ax, obj_id=None, random_color=False):
    """
    SAM2の実行結果のセグメンテーションをマスクとして描画する。

    Args:
        mask (numpy.ndarray): 実行結果のセグメンテーション
        ax (matplotlib.axes._axes.Axes): matplotlibのAxis
        obj_id (int): オブジェクトID
        random_color (bool): マスクの色をランダムにするかどうか
    """
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        cmap = plt.get_cmap("tab10")
        cmap_idx = 0 if obj_id is None else obj_id
        color = np.array([*cmap(cmap_idx)[:3], 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    ax.imshow(mask_image)


def show_points(coords, labels, ax, marker_size=200):
    """
    指定した座標に星を描画する。
    labelsがPositiveの場合は緑、Negativeの場合は赤。

    Args:
        coords (numpy.ndarray): 指定した座標
        labels (numpy.ndarray): Positive or Negative
        ax (matplotlib.axes._axes.Axes): matplotlibのAxis
        marker_size (int, optional): マーカーのサイズ
    """
    pos_points = coords[labels==1]
    neg_points = coords[labels==0]
    ax.scatter(pos_points[:, 0], pos_points[:, 1], color='green', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)
    ax.scatter(neg_points[:, 0], neg_points[:, 1], color='red', marker='*', s=marker_size, edgecolor='white', linewidth=1.25)

def show_box(box, ax):
    """
    指定された矩形を描画する

    Args:
        box (numoy.ndarray): 矩形の座標情報（x_min, y_min, x_max, y_max）
        ax (matplotlib.axes._axes.Axes): matplotlibのAxis
    """
    x0, y0 = box[0], box[1]
    w, h = box[2] - box[0], box[3] - box[1]
    ax.add_patch(plt.Rectangle((x0, y0), w, h, edgecolor='green', facecolor=(0, 0, 0, 0), lw=2))

starttime = datetime.datetime.now()
device = torch.device("cpu")

sam2_checkpoint = r"sam2\checkpoint\sam2.1_hiera_large.pt"
model_cfg = r"C:\Users\oomam\git\python\sam2-test\sam2\configs\sam2.1\sam2.1_hiera_l.yaml"

predictor = build_sam2_video_predictor(model_cfg, sam2_checkpoint, device=device)

# `00001.jpg`のような形式でJPEGに変換されたフレームファイルが格納されているディレクトリ
video_dir = r"sam2\input\dog_images"

inference_state = predictor.init_state(video_path=video_dir)

# ディレクトリ内のJPEGファイルをスキャンする
frame_names = [
    p for p in os.listdir(video_dir)
    if os.path.splitext(p)[-1] in [".jpg", ".jpeg", ".JPG", ".JPEG"]
]
frame_names.sort(key=lambda p: int(os.path.splitext(p)[0]))

ann_frame_idx = 0  # 解析対象のフレームインデックス
ann_obj_id = 0  # 解析対象の物体（今回の場合は犬）に付与する一意のID（任意の整数を設定）

# 解析対象の座標（前準備にて特定した座標）
points = np.array([[539.9, 408.1],[645,415]], dtype=np.float32)
# 1がPositive、0がNegativeを意味する。pointsの要素と対応している。
labels = np.array([1,0], np.int32)
_, out_obj_ids, out_mask_logits = predictor.add_new_points_or_box(
    inference_state=inference_state,
    frame_idx=ann_frame_idx,
    obj_id=ann_obj_id,
    points=points,
    labels=labels,
)

# ビデオ全体でセグメンテーションを行い、結果を辞書に保存する
video_segments = {}
for out_frame_idx, out_obj_ids, out_mask_logits in predictor.propagate_in_video(inference_state):
    video_segments[out_frame_idx] = {
        out_obj_id: (out_mask_logits[i] > 0.0).cpu().numpy()
        for i, out_obj_id in enumerate(out_obj_ids)
    }

plt.close("all")
for out_frame_idx in range(len(frame_names)):
    plt.figure(figsize=(6, 4))
    plt.title(f"frame {out_frame_idx}")
    plt.axis('off')
    plt.tight_layout(pad=0)

    # cv2はデフォルトがBGRのため、RGBに変換してから出力する
    image = cv2.imread(os.path.join(video_dir, frame_names[out_frame_idx]))
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # マスクの描画
    for out_obj_id, out_mask in video_segments[out_frame_idx].items():
        show_mask(out_mask, plt.gca(), obj_id=out_obj_id)

    # マスク済みの画像を出力する
    file_name = os.path.basename(frame_names[out_frame_idx])
    plt.savefig(os.path.join("result", file_name))
    plt.close()

print(f"処理時間:{datetime.datetime.now() - starttime}")
