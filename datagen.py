import os
import shutil
import json

# 文件夹路径
json_path = 'Key&Value.json'
modern_kanji_dir = 'modern_kanji'  # 存放现代汉字图片的文件夹
train_input_dir = 'train/input'  # 存放输入图片的文件夹
test_input_dir = 'test/input'  # 存放输入图片的文件夹
train_target_dir = 'train/target'  # 存放目标图片的文件夹
test_target_dir = 'test/target'  # 存放目标图片的文件夹
dir0_path = 'EVOBC'

# 如果目标文件夹不存在，创建它们
os.makedirs(train_input_dir, exist_ok=True)
os.makedirs(test_input_dir, exist_ok=True)
os.makedirs(train_target_dir, exist_ok=True)
os.makedirs(test_target_dir, exist_ok=True)

# 步骤 1: 获取modern_kanji文件夹中的所有汉字
kanji_dict = {}
for filename in os.listdir(modern_kanji_dir):
    # 提取汉字部分 (假设文件命名是汉字+后缀的形式)
    if filename.endswith('.png'):
        kanji = filename.split('.')[0]  # 去掉后缀
        print(kanji)
        kanji_dict[kanji] = filename  # 保存汉字和对应的图片文件名

with open(json_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 遍历每个序号和汉字
i = 1
for key, value in data.items():
    # 构建dir1_path路径
    dir1_path = os.path.join(dir0_path, key)
    if value in kanji_dict:
        print("已查找到：", value, i )
        # 查找jpg或者png文件
        found = False
        for filename in os.listdir(dir1_path):
            if filename.endswith(('.jpg', '.png')):
                # 找到文件，进行重命名并复制到目标目录
                source_input_file = os.path.join(dir1_path, filename)
                source_target_file = os.path.join(modern_kanji_dir, kanji_dict[value])
                if i % 10 == 0:
                    end_input_file = os.path.join(test_input_dir, f"test_{i}.png")
                    end_target_file = os.path.join(test_target_dir, f"test_{i}.png")
                else:
                    end_input_file = os.path.join(train_input_dir, f"train_{value}_{i}.png")
                    end_target_file = os.path.join(train_target_dir, f"train_{value}_{i}.png")


                # 使用shutil.copy()复制并重命名文件
                shutil.copy(source_input_file, end_input_file)
                shutil.copy(source_target_file, end_target_file)
                print(f"已找到input图片: {source_input_file} -> {end_input_file}")
                print(f"已找到target图片: {source_target_file} -> {end_target_file}")
                found = True
                i = i + 1
                break
        # 如果已经找到文件，则跳出当前循环
        if found:
            continue
    else:
        print("-------------未找到：", value)





