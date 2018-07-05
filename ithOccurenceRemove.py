listOfWords=[]
numOfWords=int(raw_input())
for i in range(numOfWords):
	listOfWords.append(raw_input())
word=raw_input()
occurance=int(raw_input())
val=-1;
count=1
print(listOfWords.index(word))
for i in listOfWords:
	val+=1;
	if i==word:
		if count==occurance:
			listOfWords.pop(val)
		else:
			count+=1
print(listOfWords)
			
