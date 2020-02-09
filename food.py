#讀取檔案
#讀取模式 r
#寫入模式 w
#as 為"當作"，後面給一個代表的變數

data = []
with open('food.txt', 'r') as f:
	for line in f:
		data.append(line)
print(data)