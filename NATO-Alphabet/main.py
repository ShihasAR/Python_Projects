import pandas
phonetic = pandas.read_csv("nato_phonetic_alphabet.csv")




def nato():
    name = input("enter word: ").upper()
    list_n = list(name)
    try :
        new_dict = {row.letter: row.code for (index, row) in phonetic.iterrows()}
        result = [new_dict[n] for n in list_n]
    except KeyError:
        print("Sorry alphabets only. ")
        nato()
    else:
        print(result)

nato()




