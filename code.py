import PySimpleGUI as sg

sg.theme('Black')
layout = [
    [sg.VPush()],
    [sg.Text('TIME')],
    [sg.Button('Start'),sg.Button('Lap')],
    [sg.VPush()]
]

window = sg.Window(
    'StopWatch',
    layout,
    size = (500,500),
    no_titlebar = True,
    element_justification = 'center')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Start'):
        break

window.close()