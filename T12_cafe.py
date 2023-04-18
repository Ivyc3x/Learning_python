# Creating a menu list, and two dictionaries. Considering how key needs to be unique (numeric key used as 
#taking into account there may be multiple variations of 'scone'.  Unique key to allow correlation to other dictionaries)

#list called menu using tuple and then converting into a menu dictionary
menu = [(1,"scone"),(2,"cookie"), (3,"cheese pie"), (4,"custard tart"),(5,"muffin")]
menu_dict = dict(menu)

#stock qty
stock_dict ={1:20,
             2:40,
             3:25,
             4:15,
             5:23}
#print(stock_dict)

#stock price
price_dict={1:2.80,
            2:2.50,
            3:3.30,
            4:2.99,
            5:3.00}
#print(price_dict)

#making copies of dictionaries
menu_dict_copy = menu_dict.copy()
stock_dict_copy = stock_dict.copy()
price_dict_copy = price_dict.copy()

#total stock value by multiplying stock qty with price
total_value ={**stock_dict_copy,**price_dict_copy}
for k, v in stock_dict_copy.items():
    for k2, v2 in price_dict_copy.items():
        if k == k2:
            total_value[k] = (v*v2)
            total_value_all=sum(total_value.values()) 
            tidy_total_value_all= "{:.2f}".format(total_value_all)
print("The total value of stock is:\t£",tidy_total_value_all)
final_stock_value= dict(total_value)

#merging final_stock_value with menu_dict_copy to show the breakdown of stock value per category
def merge_menu_stock (final_stock_value, menu_dict_copy):
    menu_stock = {**final_stock_value,**menu_dict_copy}
    for key,value in menu_stock.items():
        if key in final_stock_value and key in menu_dict_copy:
            menu_stock[key] = [value,final_stock_value[key]]
    return menu_stock
menu_stock = merge_menu_stock(final_stock_value,menu_dict_copy)
final_menu_stock=dict(menu_stock)
print("The breakdown of stock value per item:\n",final_menu_stock)











