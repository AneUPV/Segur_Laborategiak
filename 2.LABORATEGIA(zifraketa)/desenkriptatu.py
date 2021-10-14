
def desenkriptatu(mezua):
	orig=mezua
	mezua=mezua.replace(" ", "")
	zenbat=len(mezua)
	stat=[]
	frek=['e', 'a', 'o', 'l', 's','n','d','r','u','i','t','c','p','m','y','q','b','h','g','f','v','j','ñ','z','x','k','w']

	#De la A a la Z
	for i in range(65,91):
		kop = mezua.count(chr(i))
		ehunekoa = (kop/zenbat)*100
		stat.append((chr(i), ehunekoa))
		stat.sort(key = lambda x: x[1], reverse=True)
	print("Hizkien agerpena ehunekotan (mezu totalarekiko)\n")
	print(stat)
	print("\n")
	#print(len(stat))
	#print(len(frek))
	for x in range(0, len(stat)) :
		orig = orig.replace(stat[x][0], frek[x])

	ema=orig.upper()
	print (ema)
	return ema

#-----------------------------------------------------------------------------------------------------------------------------------------------

def ordezkatu(mezua, kar1, kar2):
	m = mezua.replace(kar1.upper(), kar2.lower())
	return m

#------------------------------------------------------------------------------------------------------------------------------------------------

mezua = input("Emaidazu zifratutako mezua:\n")
print("Estatistikak lortzen...\n")
print("--------------------------------------------------------------")
m=desenkriptatu(mezua)
print("--------------------------------------------------------------\n")

print("Ordezkapen metodo monoalfabetikoa estadistikan oinarritutako deszifraketa metodo bat da")
erantzuna=input("Eskuz aldaketak egin nahi dituzu? (S/n)\n")

if (erantzuna == 'S' or erantzuna == 's'):
	print("Ederto!! Irtetzeko 'quit' bi aldiz idatzi\n ")
	kar1=input("ALDATU-->")
	kar2=input("BESTE HONENGATIK-->")

	while (kar1!='quit' and kar2!='quit'):
		print("\n")
		m=ordezkatu(m, kar1, kar2)
		print(m)
		kar1=input("ALDATU-->")
		kar2=input("BESTE HONENGATIK-->")

else:
	print("Zure mezu zifratua:\n")
	print(m)
	print("\n------------------------------------\n Agur!! :)")
