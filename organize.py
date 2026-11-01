import os
import shutil

folder = r"C:\dev\test_files"

categories = {
    ".jpg": "图片",
    ".jpeg": "图片",
    ".png": "图片",
    ".pdf": "文档",
    ".docx": "文档",
    ".txt": "文档",
    ".zip": "压缩包",
    ".rar": "压缩包", 
}

for name in os.listdir(folder):
   path = os.path.join(folder,name)

   if os.path.isdir(path):
      continue

   stem, ext = os.path.splitext(name)
   ext = ext.lower()
   target = categories.get(ext, "其他")

   target_dir = os.path.join(folder, target)
   os.makedirs(target_dir, exist_ok=True)
   shutil.move(path, os.path.join(target_dir, name))
   print(name, "->", target)