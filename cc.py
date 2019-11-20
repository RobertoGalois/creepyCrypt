# -*-coding:Utf-8 -*

def crypt(pStr):
	codes = dict(zip(list('abcdefghijklmnopqrstuvwxyz'), list(range(1, 27))))
	retNb = 0
	for letter in pStr.lower():
		retNb += codes[letter]

	return retNb

print(crypt('eric'))
print(crypt('louis'))
print(crypt('jacques'))
