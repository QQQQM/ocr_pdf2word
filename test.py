#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2019/11/12 16:17
# @Author: qimeng
# @File  : test.py
import os
import subprocess
import ghostscript
from wand.image import Image

pdf_folder='D:/pdf2word/test_file/pdf/1.pdf'
img_folder='D:/pdf2word/test_file/img/2'
subprocess.check_output(['pdfimages.exe', '-png', pdf_folder, img_folder])
