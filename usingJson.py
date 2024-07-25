""" JSON- JAVASCRIPT OBJECT NOTATION""" #used to convert one data into another type of data i.e., parsing

import json

#converting Json to python
# player = '{"name": "Ronaldo","age": "36","profession":"footballer"}'
# result = json.loads(player)
# print("data after conversion")
# print(result["age"])
# print(type(result))
#
# people_string = '''{
#     "people":[
#         {
#             "name":"doflamingo",
#             "email":"doffy123@gmail.com",
#             "phone": "+62 345216961",
#             "work": "instructor",
#             "have_license":true
#         },
#         {
#             "name":"trafalgar",
#             "email":"trao24@gmail.com",
#             "work": "driver",
#             "phone": null,
#             "have_license":false
#         }
#     ]
# }'''
# my_result = json.loads(people_string)
# print(my_result)
# # print(type(my_result["people"]))
#
# for person in my_result["people"]:
#     del person["have_license"]
#     # print(person['email'])
# # del my_result["people"]["have_license"]
# modified_result = json.dumps(my_result, indent = 4,sort_keys=True)
# print(modified_result)

with open('charStates.json' , 'r') as f:
    data = json.load(f)
    print(data)
for params in data['states']:
    # print(params['names'],params['area'])
    del params['area_code']
    # print(params)

with open('newStates.json','w') as x:
    val = json.dump(data,x,indent=2,sort_keys=True)
    print(val)

new_data = {
    'name':'peter parker',
    'area':'new york city',
    'area_code':'11223344'
}
with open('newStates.json','a') as fp:
    val1 = json.dump(new_data,fp,indent=2,sort_keys=True)
    print(val1)


