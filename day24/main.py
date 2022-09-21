#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

names = []
with open('Input/Names/invited_names.txt') as file:
    names = file.readlines()

template_lines = []
with open('Input/Letters/starting_letter.txt') as file:
    template_lines = file.readlines()

for name in names:
    name = name.strip()
    with open(f"Output/ReadyToSend/letter_{name}.txt", 'w') as file:
        for line in template_lines:
            file.write(line.replace('[name]', name))
