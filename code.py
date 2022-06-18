import PySimpleGUI as sg
from time import time

sg.theme('Black')
layout = [
    [sg.Push(), sg.Image ('x.png', pad = 0, enable_events = True, key = '-CLOSE-')],
    [sg.VPush()],
    [sg.Text('TIME', font = 'Impact 100', key = '-TIME-')],
    [sg.Button('Start', button_color = ('#FFFFFF','#666666'), border_width = 0, key = '-START-'),
    sg.Button('Lap', button_color = ('#FFFFFF','#666666'), border_width = 0, key = '-LAP-')],
    [sg.VPush()]]

window = sg.Window(
    'StopWatch',
    layout,
    size = (400,400),
    no_titlebar = True,
    element_justification = 'center')
start_time = 0
active = False

while True:
    event, values = window.read(timeout = 10)
    if event in (sg.WIN_CLOSED, '-CLOSE-'):
        break

    if event == '-START-':
        start_time = time()
        active = True

    if active:
        elapsed_time = round(time() - start_time,1)
        window['-TIME-'].update(elapsed_time)

window.close()