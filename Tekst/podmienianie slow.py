with open("input.txt", "r") as input_file:
    text = input_file.read()
    input_file.close()

word_dict = {
            " i": " oraz",
            " oraz": " i",
            " nigdy": " prawie nigdy",
            " dlaczego": " czemu"}

for word in word_dict:
    text = text.replace(word, word_dict[word])

with open("output_replaced.txt", "w") as output_file:
    output_file.write(text)
    output_file.close()
