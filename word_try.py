# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 09:55:57 2023

@author: S.Stycenkov
"""

from docx import Document
from docxcompose.composer import Composer

# main docx file
master = Document(r"C:\files\file1.docx")
composer = Composer(master)
# doc1 is the docx file getting copied
doc1 = Document(r"C:\files\file1.docx")
composer.append(doc1)
composer.save(r"C:\files\tst3.docx")