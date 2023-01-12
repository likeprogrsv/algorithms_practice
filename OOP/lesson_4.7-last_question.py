# class Shop:
#     ID_SHOP_ITEM = 0


# sp = Shop()
# sp.ID_SHOP_ITEM += 1
# print(Shop.ID_SHOP_ITEM)



def get_number(x):
    try:
        return int(x)
    except:
        try:
            return float(x)
        except:
            return x
            
res_1 = get_number(False)
res_2 = get_number('5.78')
res_3 = get_number('8(912)000-000-00')