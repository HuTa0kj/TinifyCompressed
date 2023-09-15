# tinify_compressed_images
使用 tinify 压缩图片或图片文件夹

首先获取一个 API KEY，https://tinypng.com/developers。输入你的 Email 和 ID 就可以了，从邮箱内的确认邮件获取 API KEY。

打开`tinypng.py`填入 API KEY。

```bash
# 压缩单张图片
python3 tinypng.py -i ./blog/images/test.jpg
# 批量压缩
python3 tinypng.py -f ./blog/images
```

