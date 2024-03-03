import file_operation
import Note
import ui

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = ui.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('A note has been added...')


def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Enter the date in the format dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Note.Note.get_date(notes):
                print(Note.Note.map_note(notes))
    if logic == True:
        print('There is not a single note...')


def id_edit_del_show(text):
    id = input('Enter the id of the required note: ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('The note has been changed...')
            if text == 'del':
                array.remove(notes)
                print('The note has been deleted...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('There is no such note, perhaps you entered the wrong one id')
    file_operation.write_file(array, 'a')
