#讀取檔案
#讀取模式 r
#寫入模式 w
#as 為"當作"，後面給一個代表的變數
#去掉多餘的空格根換行符號，僅能對字串格式做用


data = []
with open('food.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
print(data)