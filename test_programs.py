
def char_length_occurence (character, los):
    """Creating 2 list for character occurence in the word and length of the word"""
    character_occurence = []
    lengh_of_word = []
    temp = 0
    max_number_of_occurence = 0
    for i in range(len(los)):
        temp = los[i].count(character)
        character_occurence.append(temp)
        lengh_of_word.append(len(los[i]))
        if temp > max_number_of_occurence:
            max_number_of_occurence = temp
    return (max_number_of_occurence, character_occurence, lengh_of_word)


def program1(sentence = "This is a very crazy long sentence and I want to educate everyone in this whole crazy world", character ="z"):
    """Program 1 for find the max occurence of the character in the string"""
    los = list(sentence.split(" "))
    print("Input sentence -> " + sentence)
    print("Input character -> " + character)

    ##Creating 2 list for character occurence in the word and length of the word
    (max_number_of_occurence, character_occurence, lengh_of_word) = char_length_occurence(character, los)
    if max_number_of_occurence == 0:
        print ("No matches found")
    else:
        index_matching_values = []

        i = -1
        ##Check if there are more than 1 word with character number of occurence
        if character_occurence.count(max_number_of_occurence) > 1:
            while True:
                try:
                    i = character_occurence.index(max_number_of_occurence, i + 1)
                    index_matching_values.append(i)
                except ValueError:
                    break
            max_number_of_occurence_word_index = 0
            max_number_of_occurence_len_word = 0
            for i in range(len(index_matching_values)):
                if max_number_of_occurence_len_word < lengh_of_word[index_matching_values[i]]:
                    max_number_of_occurence_len_word = lengh_of_word[index_matching_values[i]]
                    max_number_of_occurence_word_index = index_matching_values[i]

            print ("Final output -> " + los[max_number_of_occurence_word_index])
        else:
            print ("Final output -> " + los[character_occurence.index(max_number_of_occurence)])


def program2(test_number = 156):
    """Program 2 for find the longest continous sequence of 1s in its bin format"""
    print("Input number -> " + str(test_number))
    
    binary_string = format (test_number, 'b')
    number_occurence = 0
    max_occurence = 0
    for i in range(len(binary_string)):
        if binary_string[i] == '1':
            number_occurence = number_occurence + 1
            if number_occurence > max_occurence:
                max_occurence = number_occurence
        else:
            number_occurence = 0

    print("Max number of occurence for 1 in the binary format of number is " + str(max_occurence))


def main():
    program1()
    program2()
