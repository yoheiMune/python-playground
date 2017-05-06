"""
    Pythonで画像処理を扱う.

    利用モジュール：Pillow
        $ pip install --upgrade pillow

    参考：
        https://pypi.python.org/pypi/Pillow/
        https://librabuch.jp/blog/2013/05/python_pillow_pil/
"""
from PIL import Image

# フォーマット変換
im = Image.open("obake.png")
im.convert('RGB').save("obake.jpg")