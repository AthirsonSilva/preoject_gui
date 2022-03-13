import PySimpleGUI as sg

# Create windows and layout
def login_window():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Welcome to the product register. Click the button to continue.')], 
        [sg.Button('Next')], 
    ]

    return sg.Window('Login', layout = layout, finalize = True)

def window_request():
    sg.theme('Reddit')
    layout = [
        [sg.Text("Product's data")],
        [sg.Text('Name')],
        [sg.Input()],
        [sg.Text('ID')],
        [sg.Input()],
        [sg.Text('Price')],
        [sg.Input()],
        [sg.Text('Quantity')],
        [sg.Input()],
        [sg.Button('Back'), sg.Button('Send request')],
    ]

    return sg.Window('Request', layout = layout, finalize = True)

# Create initials windows
window1, window2 = login_window(), None

# Create a loop to read events
while True:
    window, event, values = sg.read_all_windows()
    # Window closed
    if (window == window1 or window == window2) and event == sg.WIN_CLOSED:
        break 
    # Next window
    if window == window1 and event == 'Next':
        window1.hide()
        window2 = window_request()
    # Previous window
    if window == window2 and event == 'Back':
        window2.hide()
        window1.un_hide()
# Events listeners actions
    if window == window2 and event == 'Send request':
        if values['pizza1'] == True and values['pizza2'] == True:
            sg.popup('Were requested a pepperoni and portuguese pizza')
        elif values['pizza1'] == True:
            sg.popup('Was requested a pepperoni pizza')
        elif values['pizza2'] == True:
            sg.popup('Was requested a portuguese pizza')
