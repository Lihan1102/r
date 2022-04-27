#讀檔案

data = []
with open('food.txt','r') as f:
	for a in f:
		data.append(a.strip())
	
print(data)


/n #換行符號

