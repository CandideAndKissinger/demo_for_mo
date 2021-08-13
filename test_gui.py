from tkinter.constants import TRUE
import PySimpleGUI as sg


def file_address_gui():
        event, values = sg.Window('Select File',
                [[sg.Text('Filename')], [sg.Input(),sg.FileBrowse()],
                [sg.OK(), sg.Cancel()]]).read(close=TRUE)
        return values
