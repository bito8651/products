# 檢查檔案在不在，有的話就讀取檔案
import os # os(operating system)：作業系統 就像電腦的政府、管理員

products = []
if os.path.isfile('products.csv'): # 檢查在同一資料夾裡面有沒有該檔案（相對路徑）
    print('yeah! 找到檔案了！')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line :
                continue # continue跟break一樣只能寫在迴圈裡
                         # continue：跳到下一個迴圈的意思
            name, price = line.strip().split(',') # 先用.strip()來除掉換行符號(\n) # 再用.split(',')來用逗點做分割
            products.append([name, price])
        # split完的結果是一個個清單
    print(products)
else:
    print('找不到檔案......')


# 讓使用者輸入
while True:
    name = input('請輸入商品名稱： ')
    if name == 'q':
        break
    price = input('請輸入商品價格： ')
    products.append([name, price])
print(products)

# 印出所有購買紀錄
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
    # str can use + and *
    # 'abc' + '123' = 'abc123'
    # 'abc' * 3 = 'abcabcabc'
    # csv是電腦很常用來儲存資料的一種檔案格式，尤其針對這種每種商品有很多屬性的時候
with open('products.csv', 'w', encoding='utf-8') as f: # open 檔案，進入寫入模式
    # 寫入檔案時加入encoding='utf-8'解決中文字變亂碼問題
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n') # write為真正的寫入檔案 # 商品名稱+,+商品價格+換行
