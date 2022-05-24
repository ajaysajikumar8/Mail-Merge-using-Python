PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt", mode= "r") as name_file:
    names = name_file.readlines()


with open("./Input/Letters/starting_letter.txt", mode= "r") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        striped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER,striped_name)
        with open(rf"C:\Users\ajays\Downloads\Mail+Merge+Project+Start\Mail Merge Project Start\Output\ReadyToSend\letter_for_{striped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)


