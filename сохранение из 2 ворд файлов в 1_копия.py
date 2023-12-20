from docx import Document
from docxcompose.composer import Composer

# main docx file
master = Document(r"C:\files\file7.docx")
composer = Composer(master)
# doc1 is the docx file getting copied
doc1 = Document(r"C:\files\file8.docx")
composer.append(doc1)
composer.save(r"C:\files\anket_2.docx")