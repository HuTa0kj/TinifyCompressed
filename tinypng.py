import tinify
import os
import argparse

tinify.key = "API KEY"


def parse_args():
    parse = argparse.ArgumentParser(description='Calculate cylinder volume')
    parse.add_argument('-f', '--folder', required=False, nargs='?', const='new', help='Folder')
    parse.add_argument('-i', '--image', required=False, nargs='?', const='new', help='Image')
    arg = parse.parse_args()
    return arg


def tinify_image_folder(folder):
    from_file_path = folder
    to_file_path = folder + '_new'
    for root, dirs, files in os.walk(from_file_path):
        for name in files:
            file_name, file_suffix = os.path.splitext(name)
            # 只对文件夹内的 png 和 jpg 格式文件进行处理
            if file_suffix == '.png' or file_suffix == '.jpg':
                to_full_path = to_file_path + root[len(from_file_path):]
                to_full_name = to_full_path + '/' + name
                from_full_path = from_file_path + root[len(from_file_path):]
                from_full_name = from_full_path + '/' + name
                # 如果没有文件夹，创建一个
                if os.path.isdir(to_full_path):
                    pass
                else:
                    os.mkdir(to_full_path)

                source = tinify.from_file(from_full_name)
                source.to_file(to_full_name)
        print("转换成功")


def tinify_image(file_path):
    source = tinify.from_file(file_path)
    file_path, file_name = os.path.split(file_path)
    new_image = file_path + '/' + 'new_' + file_name
    source.to_file(new_image)
    print('转换完成')


if __name__ == '__main__':
    args = parse_args()
    if args.folder:
        tinify_image_folder(args.folder)
    elif args.image:
        tinify_image(args.image)
