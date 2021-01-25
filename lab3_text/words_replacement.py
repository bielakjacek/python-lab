input_file = open("sonet-adam-mickiewicz.txt", 'r', encoding='utf-8')
output_file = open("output_replacement.txt", 'w', encoding='utf-8')

replacing_dict = {
    "i": "oraz",
    "oraz": "i",
    "nigdy": "prawie nigdy",
    "prawie nigdy": "nigdy" ,
    "dlaczego": "czemu",
    "czemu": "dlaczego"
}

for line in input_file:
    new_line = line.replace(replacing_dict["oraz"], replacing_dict["i"])
    new_line = new_line.replace(replacing_dict["i"], replacing_dict["oraz"])
    new_line = new_line.replace(replacing_dict["prawie nigdy"], replacing_dict["nigdy"])
    new_line = new_line.replace(replacing_dict["czemu"], replacing_dict["dlaczego"])
    output_file.write(new_line)
