# 02
item_list = ['펜', '연필', '텀블러', '키보드', '마우스', '볼펜']

item = input("상품명을 입력해 주세요")
def func(item_list, item):
    if item in item_list:
        print('해당 상품은 저희 매장에 있습니다.')
    else:
       print('해당 상품은 저희 매장에 없습니다.')
func(item_list, item)