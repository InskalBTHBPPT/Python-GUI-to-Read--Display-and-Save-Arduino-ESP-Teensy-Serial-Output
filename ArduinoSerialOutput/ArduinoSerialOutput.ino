//#include <Arduino.h>
/*
This ino file printed out some column data separated by "," to serial port
*/


//****_Inisasi settingan untuk jeda antar looping_****//
// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;        // will store last time loop update

// constants won't change:
// interval at which to looping (milliseconds)
const long interval = 50; //sampling 20 Hz   
/************************************************************************************/

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:

  // check to see if it's time to run program; that is, if the difference
  // between the current time and last time run program is bigger than
  // the interval at which you want to run program.
  unsigned long currentMillis = millis();
  float sin_val;
  float cos_val;
  float tan_val;
  
  if (currentMillis - previousMillis >= interval) {
    // save the last time you start doing something in program
    previousMillis = currentMillis;
    Serial.print(previousMillis/1000.00); // print time stamp in unit second for 1st column
    Serial.print(",");
    
    /* Next column example data 
       You can add your sensors data for next columns
    */

    // 2nd column example, printout sinus data of time stamp
    sin_val = sin(previousMillis/1000.00);
    Serial.print(sin_val);
    Serial.print(",");

    // 3rd column example, printout cosinus data of time stamp
    cos_val = cos(previousMillis/1000.00);
    Serial.print(cos_val);
    Serial.print(",");

    // 4th column example, last column before new line. Printout tangen data of time stamp
    tan_val = tan(previousMillis/1000.00);
    Serial.println(tan_val);

    
   } //end loop interval
}
