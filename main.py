alfabe = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
liste = list()
liste2 = list()
key = input("Enter your key")
def encrypt():
    global liste
    global key
    i = 0
    msg = input("Enter your message").replace(" ","")
    while i<len(msg):
        k = ((alfabe[msg[i]]+alfabe[key[i%len(key)]])%26)
        if k == 0:
            liste.append("['z']")
        else:
            liste.append([number for number, name in alfabe.items() if name == k])
        i+=1

def decrypt():
    global liste
    global liste2
    global key
    y=0
    while y<len(liste):
        a = str(liste[y])
        z = ((alfabe[str(a[2])]-alfabe[key[y%len(key)]])%26)
        if z == 0:
            liste2.append("z")
        else:
            liste2.append([number for number, name in alfabe.items() if name == z])
        y+=1

encrypt()
print("Sifreli metin",end="\t")
print(liste)
#Zaten var olan metni çözmek icin üstteki 3 lüyü yorum satırına al ve listeye gerekli degeri ata
decrypt()
print("DeSifreli metin",end="\t")
print(liste2)
