import pprint
temp_list = [{"no":cnt,"name":"name"+str(cnt)} for cnt in range(10)]

pprint.pprint(temp_list)

temp2_list = [temp["no"] for temp in temp_list]

pprint.pprint(temp2_list)

filtered_list = list(
    filter(
        lambda x:x % 2 == 0,
        [temp["no"] for temp in temp_list]
    )
)

pprint.pprint(filtered_list)