# Python GUI for Monitor and Saving Arduino, ESP and Teensy Serial Data

## Features
- This project is provided app based on python PySimpleGUI to read and save data from serial port.
- Serial port data could be serial print out data from arduino, ESP or Teensy.
- Data could be send in some column or single column that separated by comma.
- Data is displayed at output log for every line that come from serial port.
- Data is saved txt file.

## Libraries/Packages
- Python 3.10.4
- PySerial
- PySimpleGUI

## Files
- Python GUI file [`PythonGUI_to_read_SerialData.py`](/Python%20File/PythonGUI_to_read_SerialData.py) 
- Example Arduino file [`ArduinoSerialOutput.ino`](/ArduinoSerialOutput/ArduinoSerialOutput.ino)
- Executable file for windows [`PythonGUI_to_read_SerialData.exe`](/Python%20File/Executable%20Dist/dist/PythonGUI_to_read_SerialData.exe))
  ##### I haven't try this exe file. I recommend to run `PythonGUI_to_read_SerialData.py` than this exe file.
- Example data log file  [`ExampleDataLog-7.txt`](/ExampleDataLog/ExampleDataLog-7.txt))
  
## Python GUI Screenshoot
&nbsp;

![GUI screenshoot - 2.jpg](./Python%20File/GUI%20screenshoot%20-%202.jpg)

***Figure. 1.*** *App read and save serial monitor data.*

## Log File Screenshoot
![example log data.jpg](./ExampleDataLog/example%20log%20data.jpg)

***Figure. 2.*** *Example of data log file.*
