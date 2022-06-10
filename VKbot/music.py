import codecs

file = open('empire_pva.txt')
fileObj = codecs.open('empire_pva.txt', "r", "utf_8_sig" )
text = fileObj.read() # или читайте по строке
fileObj.close()
print(text)
