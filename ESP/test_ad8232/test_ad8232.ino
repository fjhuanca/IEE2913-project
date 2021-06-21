
void setup() {
// initialize the serial communication:
Serial.begin(115200);
pinMode(10, INPUT); // Setup for leads off detection LO +
pinMode(11, INPUT); // Setup for leads off detection LO -
pinMode(A2, INPUT);
 
}
 
void loop() {
 
if((digitalRead(10) == 1)||(digitalRead(11) == 1) && 0){
Serial.println('!');
}
else{
// send the value of analog input 0:
Serial.print(1024);
Serial.print(' ');
Serial.println(analogRead(A2));
}
//Wait for a bit to keep serial data from saturating
delay(1);
}
