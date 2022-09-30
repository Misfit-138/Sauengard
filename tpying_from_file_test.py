from typing_module import typing

hint_file = open("hint_event_1.txt", "r")
if hint_file.readable():
    typing(hint_file.read())
