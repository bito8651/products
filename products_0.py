# 一樣商品同時有名字和價格的資訊要儲存，就使用二維清單來儲存
 # 二維清單(2 dimentional)，可想像成一個清單中還有清單
 # 以火車為例，
 ## 一個裝著商品的清單是一列火車
 ## 一個一個商品是一節一節車廂的車廂
 ## 商品的名字和價格是該節車廂裡面還裝有一個兩節車廂的火車(清單)
 products = [] # 大清單
 while True:
     name = input('請輸入商品名稱： ')
     if name == 'q':
         break
     price = input('請輸入商品價格： ') # 放在break下面是因為若商品名稱出現'q'，就不用問價格了直接離開
     p = [] # 小清單
     p.append(name)
     p.append(price)
     # line 13 to line 15 can be short for
     # p = [name, price]
     products.append(p)
     # line 13 to line 18 can be short for
     # products.append([name, price])
 print(products)

 products[0][0] # products list中(大清單)第零格的(小清單)第零格