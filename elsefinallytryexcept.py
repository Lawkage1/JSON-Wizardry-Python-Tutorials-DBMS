# f1 = open("Alankar.txt")
#
# try:
#     f1 = open("Alankar.txt")
#     # f2 = open("yoshimaru.txt")
#
#
# except Exception as e:
#     print(e)
#
# except EOFError as u:
#     print("ye hai EOF error",u)
#
# except IOError as x:
#     print("yeh hai IO error",x)
#
# else:
#     print("ig there was no error!?")
#
# finally:
#     print("mai to print houga bhai")
#     f1.close()


#restaurant manager
import json
restaurant_menu = '''{
    "menu":[
        {
            "dish":"Pizza",
            "price":"449",
            "time": "20 mins",
            "toppings": "extra cheese +49 extra"
        },
        {
            "dish":"Burger",
            "price":"128",
            "time":"8 mins",
            "toppings":"extra cheese +29 extra"
        }
    ]
}'''

data = json.loads(restaurant_menu)
# print(data)

with open("restaurant.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)

try:
    file = open("restaurant.json","r")
    print(file.read())

except Exception as e:
    print(e)

else:
    print("would you like anything else sir?")

finally:
    file.close()

