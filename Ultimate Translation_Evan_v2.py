'''
Program: Language Translation
Author: Evan
Description:The program is to translate from English or Franch to Franch or English
Revisions:Utilizing dictionary instead of lists
'''

# Step1: Create dictionary of english and french words.
english = {
            'chicken': 'poulet',
            'salt': 'sel',
            'apple': 'pomme',
            'earth': 'terre',
            'bean': 'haricot',
            'water': 'eau',
            'milk': 'lait'
           }
french = {
            'poulet': 'chicken',
            'sel': 'salt',
            'pomme': 'apple',
            'terre': 'earth',
            'haricot': 'bean',
            'eau': 'water',
            'lait': 'milk',
            }
    
approval = ['granted','yes','of course','yes i would','y','yea','ye']
dismissal = ['no','no thank you', 'nope','end','dismiss','n']
enlan = ['english','e','eng']
frlan = ['french','f','fra']


print('Program to translate words from English to French and vice-versa \n')

word = input('Enter an English or French word to translate: ')

# Step 2: using f string to transform the english words and french words.
while word != '':
    word = word.lower()
    if word in english:
        print(f'{"The English word "}\'{word}\'{" is "}\'{english[word]}\'{" in French."}')
    elif word in french:
        print(f'{"The French word "}\'{word}\'{" is "}\'{french[word]}\'{" in English."}')
    else:
#Step3: if the word user inpted is not belong to neither english dictionary nor french words.
        print(f'{"The "}\'{word}\'{" was not found in English or French word lists."}')
        new = input(f'{"Would you like to add "}\'{word}\'{" to the lists? <y>es or <n>o "}')
#Step 4: inquire whether should add the new word to dictionary.
        if new in approval:
#Step5: Update the word.
            lang = input(f'{"What language is "}\'{word}\'{" in? <E>nglish or <F>rench "}')
            if lang in enlan:
                add = input('Enter an French word to translate: ')
                english.update({word:add})
                french.update({add:word})#update the dictionary.
            elif lang in frlan:
                add = input('Enter an English word to translate: ')
                french.update({word:add})
                english.update({add:word})
                #update the dictionary
                
            else:

#Step6:  if words do not belong to dictionary, console will report "language not supported"
                print('Language not supported.')
        elif new in dismissal: 
            print('New word not added.')
        else:
            print('Answer not recognized.')
#Step7:  Continue the while loop for scratching new word.        
    word = input('\nEnter an English or French word to translate: ')

print('Exiting...')
    

