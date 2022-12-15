#!/usr/bin/env python3

import os
from PIL import Image
import requests

from helpers import get_files


def process(directory):
    export_dir = os.path.join(directory, "export")

    if not os.path.isdir(export_dir):
        os.makedirs(export_dir)

    for file in get_files(directory):
        export_filename = os.path.splitext(file)[0] + ".jpeg"
        try:
            with Image.open(os.path.join(directory, file)) as f:
                output = f.convert('RGB').resize((600, 400))
                output.save(os.path.join(export_dir, export_filename), "JPEG")
        except Exception as ex:
            print(ex)


def upload(directory):
    url = "http://localhost/upload/"
    
    for image in get_files(directory):
        with open(os.path.join(directory, image), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
            print(r.status_code)


if __name__ == "__main__":
    images_dir = os.path.join(os.getcwd(), "supplier-data/images")
    process(images_dir)
    upload(images_dir)
