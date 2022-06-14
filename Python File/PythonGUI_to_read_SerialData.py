#Read and Save Serial Data

import serial
import PySimpleGUI as sg
import threading
import time
looprun = 0

def read_serial_thread(comport,baudrate,pathfilelog,window):
    try:
        file_log = open(pathfilelog, "a") #using append methode to file
        print('File Log Ready')


    except Exception as b:
        print ("error saving file: " + str(b))

    try:
        ser = serial.Serial(comport,baudrate)
        print('Succesful Connected to Serial Port COM:'+comport+'  Baudrate:'+baudrate)
    except Exception as a:
        print ("error open serial port: " + str(a))

    if ser.isOpen():
        print ("OK")
        try:
            ser.flushInput() #flush input buffer, discarding all its contents
            ser.flushOutput()#flush output buffer, aborting current output
                             #and discard all that is in buffer

            while looprun == 1:
                file_log = open(pathfilelog, "a")
                line = str(ser.readline()) #change data type from byte to string
                line = line[2:][:-5] #slicing 'b and \r\n'
                file_log.writelines(line+"\n") # write/append new data from serial port to file
                print(line) #write data to output 
                file_log.close()


        except Exception as e1:
            print ("error" + str(e1))

    else:
        print ("cannot open serial port ")


def GUI_WINDOWS_EVENT():
    """
    Starts and executes the GUI
    Reads data from a global variable and displays
    Returns when the user exits / closes the window
    """
    global looprun #declare as global so if looprun is changed here than all will change

    sg.theme('DarkGreen5')

    com=('COM3','COM4','COM5','COM6','COM7','COM8','COM9','COM10','COM11','COM12','COM13')
    baud_rate=('9600','38400','115200') #at least there are two baud rate option

    parameter_serial_layout=[
               [sg.Text('COM port:'), sg.InputCombo(com,default_value='COM13',size=(15, 1), key ='-COMPORT-')],
               [sg.Text('baud rate:'), sg.InputCombo(baud_rate,default_value='115200',size=(15, 1),key='-BAUDRATE-')],
               [sg.Button('Connect to Serial Port', size=(20,1))],
               [sg.Button('Stop Read Data', size=(20,1))]
           ]
    parameter_save_file=[
        [sg.InputText(key='-PathFileLog-',size=(100,5)),
        sg.FileSaveAs(initial_folder='/tmp')]

        ]

    clear_output = [
        [sg.Button('Clear Output', size=(30,1))]]

    layout1 = [
        [sg.Output(size=(80, 20),key = '_output_'),
         sg.Frame('Parameter Serial Port',parameter_serial_layout)],
        [sg.Frame('Log Path File Name',parameter_save_file)],
        [sg.Frame('',clear_output)]
            ]

    #layout2=[[sg.Button('Save Education Details')]]

    #Define Layout with Tabs
    '''
    tabgrp = [[sg.TabGroup([[sg.Tab('Serial Monitor', layout1, title_color='Red',border_width =10, background_color='Green',
                                    element_justification= 'center'),
                        sg.Tab('Graph', layout2,title_color='Blue',background_color='Green')]],
                        tab_location='centertop', title_color='Red', tab_background_color='Purple',selected_title_color='White',
                        selected_background_color='Gray', border_width=5)]]
    '''

    window = sg.Window('Read Serial Data', layout1, finalize=True)
    #window =sg.Window("Tabs",tabgrp,finalize=True)

    timeout = thread = None
    # --------------------- EVENT LOOP ---------------------

    while True:
        event, values = window.read(timeout=timeout)

        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        elif event.startswith('Connect') and not thread:
            looprun = 1
            print ('Prepare to Connect to Serial Port COM:'+values['-COMPORT-']+'  Port:'+values['-BAUDRATE-'])
            thread = threading.Thread(target=read_serial_thread, args=(values['-COMPORT-'],values['-BAUDRATE-'],values['-PathFileLog-'],window), daemon=True)
            thread.start()

        elif event.startswith('Stop'):
            looprun = 0
            thread = None
            #print ('data stop')
            sg.popup('Data Stop')

        elif event.startswith('Clear'):
            looprun = 0
            thread = None
            #print ('data stop')
            sg.popup('Data Stop and Clear')
            time.sleep(1)
            window.FindElement('_output_').Update('') #clear output elemen

    window.close()


if __name__ == '__main__':
    GUI_WINDOWS_EVENT()
    print('Exiting Program')
