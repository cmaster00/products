import os
#讀取檔案
def read_file(filename):
    prodcuts = []
    with open(filename, 'r', encoding = 'utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue
            name, price = line.strip().split(',')
            prodcuts.append([name, price])
    return prodcuts

#讓使用者輸入
def user_input(prodcuts):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        prodcuts.append([name, price])
    print(prodcuts)
    return prodcuts

#印出所有購買紀錄
def print_products(prodcuts):
    for p in prodcuts:
        print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, prodcuts):
    with open('products.csv', 'w', encoding = 'utf-8') as f:
        f.write('商品,價格\n')
        for p in prodcuts:
            f.write(p[0] + ',' + str(p[1]) + '\n')

def main():
    filename = 'products.csv'
    if os.path.isfile(filename):
        print('有檔案')
        prodcuts = read_file(filename)
    else:
        print('沒有檔案')

    prodcuts = user_input(prodcuts)
    print_products(prodcuts)
    write_file('products.csv', prodcuts)

main()

