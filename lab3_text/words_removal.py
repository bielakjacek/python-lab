input_file = open("sonet-adam-mickiewicz.txt", 'r', encoding='utf-8')
output_file = open("output_removal.txt", 'w', encoding='utf-8')

for line in input_file:
    new_line = line.replace("dlaczego", "").replace("nigdy", "").replace("oraz", "").replace('i', "").replace("się", "")
    output_file.write(new_line)
