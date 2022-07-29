palabraInv=[]; 
palabraDer=[];
palabra=input ("INGRESE LA PALABRA: ");
for i in range(0,(len(palabra))): a=((len(palabra)-i)-1); 
palabraInv.append(palabra[((len(palabra)-i)-1)]);
palabraDer.append(palabra[(i-(len(palabra)))]); 
if (palabraDer == palabraInv) : print("ES PALINDROMO") 
else: print("NO ES PALINDROMO");
print(palabraDer); 
print(palabraInv);