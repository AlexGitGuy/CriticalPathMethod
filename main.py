import data_input

read_data = data_input.load_data_from_file()

for data in read_data.items():
    print(f"{data[0]}\n\t" + "\n\t".join([str(elem) for elem in data[1]]))

