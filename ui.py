import Note


def create_note(number):
    title = check_len_text_input(
        input('Enter the Name of the note: '), number)
    body = check_len_text_input(
        input('Enter a description of the note: '), number)
    return Note.Note(title=title, body=body)


def menu():
    print("\nThis is the Notes program. The following functions are available:\n\n1 - outputting all notes from a file\n2 - adding a note\n3 - deleting a note\n4 - editing a note\n5 - selecting notes by date\n6 - show a note on id\n7 - exit\n\nEnter the function number: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'The text should be larger {n} characters\n')
        text = input('Enter the text: ')
    else:
        return text


def goodbuy():
    print("If you liked the implementation of the Note, please transfer the some money to the My account 12345 6789 9876 5432 !")
