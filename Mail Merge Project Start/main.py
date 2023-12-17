with open("./Input/Names/invited_names.txt") as invited_names:
    names = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt") as template:
    template_contents = template.read()
    for n in names:
        name = n.strip()
        new_letter = template_contents.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}", mode="w") as finished_letter:
            finished_letter.write(new_letter)
