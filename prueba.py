file = open ("hola.txt","r+")
#comentario

lineas = file.readlines()
print (lineas)

ultima_linea = int(len(lineas)) - 1

for i in lineas:
    #output=len(i)-1
        print ("{}{}".format(i[0],len(i)-1))
    #print (i[lineas],len(i))
 
a = lineas [-1]
print (lineas[-1])
print (lineas[0])
print (lineas[1])
print ("{}{}".format(a[0],len(i)))
print (ultima_linea)

file.close()


           
#frase =[]
#frase = input ("Escribe algo: ")
#print("Primera letra", frase [0], "Longitud: ", len(frase))
