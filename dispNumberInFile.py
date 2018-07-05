with open("/home/divum/Desktop/python/mainFile.txt") as fi:
	
	for line in fi:
		for ch in line:
			if(ord(ch)<57 and ord(ch)>47):
				print(ch)
