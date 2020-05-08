import os
import io

def read_file(f):
	fl=open(f,'rb')
	data = fl.read()
	return data

def encrypt(n,f):
		fl=open(f,'ab')
		enc=[]
		for x in range(0,len(n)):
				if x % 2 == 0 :
					enc.append((n[x])+2)
				else:
					enc.append((n[x])+3)

		enf = f +".jok"
		en=open(enf, 'w+')
		en.write(str(enc))
		os.remove(f)
		en.close()


def decrypt(f):
		fpath = f.split('.')
		f_size=os.path.getsize(f)
		print(f)
		print("File size: {}".format(f_size))
		c_size = 0
		txt=[]	
		decf=fpath[0]+"**decrypted**."+fpath[1]
		out=open(decf,'ab')
		buf = io.DEFAULT_BUFFER_SIZE - 1000
		with open(f,'r', buf) as fl:
			inp = fl.read()
			inp = eval(inp)
			for x in range(0,len(inp)) :
				if x % 2 == 0 :
					txt.append(inp[x]-2)
				else:
					txt.append(inp[x]-3)
			
			a = bytearray(txt)
			out.write(a)
			
		
		os.remove(f)
		inp = ""

print("     __        _    _____           ___                   _____  ___   ")
print("     \ \  ___ | | _|___ / _ __ ___ / _ \ _ __   ___ _   _|___ / / _ \  ")
print("      \ \/ _ \| |/ / |_ \| '__/ __| | | | '_ \ / __| | | | |_ \| | | | ")
print("   /\_/ | (_) |   < ___) | | | (__| |_| | | | | (__| |_| |___) | |_| | ")
print("   \___/ \___/|_|\_|____/|_|  \___|\___/|_| |_|\___|\__, |____/ \___/  ")
print("                                                    |___/              ")

ch = int(input("ENter 1 for encryption or 2 for decryption:"))
j = input("Enter the path of the file: ")
files=os.listdir(j)

for f in files:
	f=j+f
	data = read_file(f)

	if ch == 1:
		encrypt(data,f)
		

	elif ch ==2:
		decrypt(f)

	else:
		print("error")
