"""
视频转换器
作者: [Robin]
版本: 1.0
开源协议: MIT License

MIT License

版权所有 (c) [2024] [Robin]

特此授予任何获得本软件副本和相关文档文件（“软件”）的人无限制地处理
软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售
软件的副本，并允许软件提供给其的人员这样做，但须符合以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或主要部分中。

本软件按“原样”提供，不作任何明示或暗示的担保，包括但不限于
适销性、特定用途适用性和不侵权的担保。在任何情况下，作者或版权持有人均不对
因软件或软件的使用或其他交易而产生的任何索赔、损害或其他责任负责，无论是在合同诉讼、
侵权或其他方面。
"""
import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

def dhash(image, hash_size=8):
    resized = cv2.resize(image, (hash_size + 1, hash_size))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def phash(image, hash_size=8):
    resized = cv2.resize(image, (hash_size, hash_size))
    dct = cv2.dct(np.float32(resized))
    dct_low_freq = dct[:hash_size, :hash_size]
    med = np.median(dct_low_freq)
    diff = dct_low_freq > med
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def hamming_distance(hash1, hash2):
    return bin(hash1 ^ hash2).count('1')

def video_to_frames(video_path, output_dir, hash_func, hash_size=8, threshold=5, remove_similar=False):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_dir = os.path.join(output_dir, video_name)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path)
    count = 0
    prev_hash = None

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if remove_similar:
            current_hash = hash_func(frame, hash_size)
            if prev_hash is None or hamming_distance(prev_hash, current_hash) > threshold:
                frame_filename = os.path.join(output_dir, f"frame_{count:04d}_hash.jpg")
                cv2.imwrite(frame_filename, frame)
                count += 1
                prev_hash = current_hash
        else:
            frame_filename = os.path.join(output_dir, f"frame_{count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            count += 1

    cap.release()

def select_video():
    global video_path
    video_paths = filedialog.askopenfilenames(filetypes=[("All files", "*.*"),("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
    if video_paths:
        video_path = video_paths[0]  # 只选择第一个文件进行处理
        video_label.config(text=f"已选择视频文件: {os.path.basename(video_path)}")

def select_output_dir():
    global output_dir
    output_dir = filedialog.askdirectory()
    if output_dir:
        output_label.config(text=f"已选择输出文件夹: {output_dir}")

def start_conversion():
    if not video_path or not output_dir:
        messagebox.showwarning("警告", "请先选择视频文件和输出文件夹")
        return

    hash_func = dhash if hash_var.get() == "dhash" else phash
    threshold = threshold_var.get()
    video_to_frames(video_path, output_dir, hash_func, threshold=threshold, remove_similar=remove_similar_var.get())
    messagebox.showinfo("完成", f"视频已转换为图片，保存在 {output_dir} 文件夹中")

# 创建主窗口
root = tk.Tk()
root.title("视频转换器")

video_path = ""
output_dir = ""

# 创建选择视频按钮
select_video_button = tk.Button(root, text="选择视频文件", command=select_video)
select_video_button.pack(pady=10)

# 显示已选择的视频文件
video_label = tk.Label(root, text="未选择视频文件")
video_label.pack(pady=5)

# 创建选择输出文件夹按钮
select_output_button = tk.Button(root, text="选择输出文件夹", command=select_output_dir)
select_output_button.pack(pady=10)

# 显示已选择的输出文件夹
output_label = tk.Label(root, text="未选择输出文件夹")
output_label.pack(pady=5)

# 创建去除相同图像复选框
remove_similar_var = tk.BooleanVar()
remove_similar_check = tk.Checkbutton(root, text="去除相同图像", variable=remove_similar_var)
remove_similar_check.pack(pady=10)

# 创建哈希算法选择下拉菜单
hash_var = tk.StringVar(value="dhash")
hash_label = tk.Label(root, text="选择哈希算法:")
hash_label.pack(pady=5)
hash_menu = ttk.Combobox(root, textvariable=hash_var, values=["dhash", "phash"])
hash_menu.pack(pady=5)

# 创建阈值选择滑块
threshold_var = tk.IntVar(value=50)
threshold_label = tk.Label(root, text="选择阈值:")
threshold_label.pack(pady=5)
threshold_slider = tk.Scale(root, from_=0, to_=100, orient=tk.HORIZONTAL, variable=threshold_var)
threshold_slider.pack(pady=5)

# 创建开始转换按钮
start_button = tk.Button(root, text="开始转换", command=start_conversion)
start_button.pack(pady=20)

# 运行主循环
root.mainloop()