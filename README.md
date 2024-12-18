# 视频转换器

## 简介

视频转换器是一个使用 Python 和 OpenCV 开发的工具，可以将视频文件逐帧提取成图片，并支持去除相似图片的功能。用户可以选择不同的哈希算法来检测相似图片，并设置阈值来控制相似度的判断。

## 作者

作者: Robin
版本: 1.0

## 功能

- 支持多种视频格式（如 `.mp4`, `.avi`, `.mov`, `.mkv`）
- 将视频逐帧提取成图片
- 支持去除相似图片
- 支持选择不同的哈希算法（`dhash` 和 `phash`）
- 用户可以设置相似度阈值

## 使用方法

1. 运行 `main.py` 文件启动图形用户界面。
2. 点击“选择视频文件”按钮，选择要处理的视频文件。
3. 点击“选择输出文件夹”按钮，选择保存图片的文件夹。
4. 选择是否去除相似图片。
5. 选择哈希算法（`dhash` 或 `phash`）。
6. 设置相似度阈值。
7. 点击“开始转换”按钮，开始处理视频。

## 安装

1. 克隆或下载本仓库。
2. 安装所需的 Python 库：
   ```bash
   pip install opencv-python numpy tkinter
   ```
3. 运行 `main.py` 文件：
   ```bash
   python main.py
   ```

## 开源协议

MIT License

版权所有 (c) 2024 Robin

特此授予任何获得本软件副本和相关文档文件（“软件”）的人无限制地处理
软件的权利，包括但不限于使用、复制、修改、合并、出版、分发、再许可和/或出售
软件的副本，并允许软件提供给其的人员这样做，但须符合以下条件：

上述版权声明和本许可声明应包含在软件的所有副本或主要部分中。

本软件按“原样”提供，不作任何明示或暗示的担保，包括但不限于
适销性、特定用途适用性和不侵权的担保。在任何情况下，作者或版权持有人均不对
因软件或软件的使用或其他交易而产生的任何索赔、损害或其他责任负责，无论是在合同诉讼、
侵权或其他方面。
