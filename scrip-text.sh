#!/bin/bash
#Loop to pass all scrip texts to python script easily
books="1-Nephi 2-Nephi Jacob Enos Jarom Omni Words-of-Mormon Mosiah Alma Helaman 3-Nephi 4-Nephi Mormon Ether Moroni"
for book in $books; 
do 
    #echo "$book"
    python sql-scrip-parser.py $book-text.txt
    soffice --headless --convert-to rtf $book-clean.txt #converts txt to rtf
done
