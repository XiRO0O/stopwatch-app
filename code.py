import PySimpleGUI as sg
from time import time

sg.theme('Black')
layout = [
    [sg.Push(), sg.Image ('x.png', pad = 0, enable_events = True, key = '-CLOSE-')],
    [sg.VPush()],
    [sg.Text('TIME', font = 'Impact 100', key = '-TIME-')],
    [sg.Button('Start', button_color = ('#FFFFFF','#666666'), font = 'Impact 15', border_width = 0, key = '-START-'),
    sg.Button('Lap', button_color = ('#FFFFFF','#666666'), font = 'Impact 15', border_width = 0, key = '-LAP-', visible = False)],
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
        if active:
            active = False
            window['-START-'].update('Reset')
            window['-LAP-'].update(visible = False)

        else:
            start_time = time()
            active = True
            window['-START-'].update('Stop')
            window['-LAP-'].update(visible = True)

    if active:
        elapsed_time = round(time() - start_time,1)
        window['-TIME-'].update(elapsed_time)

window.close()