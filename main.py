
with open("/Users/HP/PycharmProjects/Mail Merge/Input/names/invited_names.txt", mode="r") as names:
    names_list = names.readlines()
    print(names_list)

for name in names_list:
    name_data = name.strip("\n")
    with open("/Users/HP/PycharmProjects/Mail Merge/Input/Letters/starting_letter.txt", mode="r") as file:
        data = file.read()
        x = data.replace("[name]", f"{name_data}")
    with open(f"./output/readytosend/letter_for_{name_data}.txt", mode="w") as mail:
        mail.write(x)
