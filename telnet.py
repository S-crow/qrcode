import getpass
import sys
import telnetlib
import sys
import zlib
import base64
from PIL import Image
import qreader 

HOST = "challenges.ecsc-teamfrance.fr"
PORT = 3001
tn = telnetlib.Telnet(HOST, PORT)

tn.write("Y\n")
a = tn.read_until(b'What is you answer?')
a = a.split('>>')[1]
result = a.split('What')[0]


f = open("image1.png","a")
f.write(result.decode("base64").decode("zlib"))
f.close()

im= Image.open("image1.png")
part = 0
array = []

for i in range(0,8):
    for j in range(0,8):

        im_size = im.size

        left = j*290
        top = i*290
        width = 290
        height = 290

        box = (left, top, left+width, top+height)

        area = im.crop(box)
        #area.show()

        number = qreader.read(area)
        array.append(number)
        #print str(part) + ": " + str(number)
        #sum += number
        #print area.size
        #area.save("./parts/"+str(part)+".png", "PNG")
        #area.close()
        #part+=1

#print array
#print len(array)
resultat = 0
for element in array:
    resultat+=element

#print resultat
tn.write(str(resultat) + '\n')
print tn.read_all()
