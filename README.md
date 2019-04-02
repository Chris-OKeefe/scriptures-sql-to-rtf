# scriptures-sql-to-rtf
Takes data exported from SQL database of LDS scriptures and turns it into usable text.

./text-input contains txt files exported from MySQL 3.0 database. Each file contains the text of the book from the Book of Mormon. These files have a table at the head of the file that contains a unique verse id, the chapter number, and the verse number. The rest of the file contains verses with a unique verse id and the text of the verse.

sql-scrip-parser.py converts these files into readable text files. Each chapter is identified and followed by the text in a "verse-first" format (that is, each verse ends with a newline).

scrip-text.sh uses sql-scrip-parser.py and passes it a list of files to convert and then converts the output into rtf files.

## Skills:
* Uses simple Python scripting to process text files
* Uses simple BASH scripting

## To do:
* Fix input/output folder issues.
* Fix sql-scrip-parser.py so that it can convert input text to either txt or tex output.
* Fix sql-scrip-parser.py so that it can convert to rtf within the script (rather than relying on calling soffice).
* Consider fixing sql-scrip-parser.py so that it can take a list of files.
* Consider fixing sql-scrip-parser.py so that it can pull text directly from SQL.


