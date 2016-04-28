from sys import argv

#Get args
script, filename = argv

#Split original file into 2
f = open(filename)
contents1, sentinel, contents2 = f.read().partition("scripture_text\n")
f.close()

output = open(filename.replace('-text.txt', '-clean.txt'), 'w')
contents1_list = contents1.split('\n')
contents2_list = contents2.split('\n')

contents1_list = contents1_list[2:]

#Get data into lists
contents1_super = [chapter_verse.split() for chapter_verse in contents1_list]
contents2_super = [text.split() for text in contents2_list] 

#Combine elements within id string into lists.
contents2_text = [" ".join(contents2_super[i][1:]) for i in range(0,len(contents2_super))]

for i in range(0, len(contents2_super)-1):
    if contents1_super[i][2] == '1': #if verse == 1, print chapter, verse, and text
        #output.write('\lettrine %s\n $^{%s}$ %s\n' % (contents1_super[i][1], contents1_super[i][2], contents2_text[i])) #LaTeX stub output
        output.write('Chapter %s\n%s. %s\n' % (contents1_super[i][1], contents1_super[i][2], contents2_text[i]))
    elif contents1_super[i][2] != '1':  #if verse != 1, print verse and text
        #output.write('$^{%s}$ %s\n' % (contents1_super[i][2], contents2_text[i])) #Text output
        output.write('%s. %s\n' % (contents1_super[i][2], contents2_text[i]))   
            
output.close()

