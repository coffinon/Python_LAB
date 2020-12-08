with open("input.txt", "r") as input_file:
    text = input_file.read()
    input_file.close()

word_list = [" się", " i", " oraz", " nigdy", " dlaczego"]

for word in word_list:
    text = text.replace(word, "")

with open("output.txt", "w") as output_file:
    output_file.write(text)
    output_file.close()
