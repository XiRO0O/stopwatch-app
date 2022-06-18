import PySimpleGUI as sg

sg.theme('Black')
layout = [
    [sg.Push(), sg.Image ('x.png', pad = 0, enable_events = True, key = '-CLOSE-')],
    [sg.VPush()],
    [sg.Text('TIME', font = 'Impact 100')],
    [sg.Button('Start', button_color = '#FF0000', border_width = 0),
    sg.Button('Lap', button_color = '#FF0000', border_width = 0)],
    [sg.VPush()]
]

window = sg.Window(
    'StopWatch',
    layout,
    size = (400,400),
    no_titlebar = True,
    element_justification = 'center')

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

window.close()