with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        name=name.strip()
        print(name)
        with open(r"R:\100 day of code\24th\Input\Letters\starting_letter.txt") as letter:
            with open(f"letter_for_{name}.txt",'w') as let:
                for _ in letter :
                    let.write(_.replace("[name]",name))
