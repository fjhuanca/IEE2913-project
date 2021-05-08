/*Piezo sensor with Arduino.
  Serial monitor readings.
  created by the SriTu Tech team.
  Read the code below and use it for any of your creation

 Codigo extraido de: https://srituhobby.com/how-does-work-piezo-sensor-piezo-sensor-with-arduino-uno-board/
*/
 
void setup() {
  Serial.begin(9600);//enable serial monitor
  for (byte a = 2; a <= 6; a++) {
    pinMode(a, OUTPUT);
  }
}
int value1=0;
int value0=0;
int muest=100;
void loop() {
  value1=value0;
  int value = analogRead(A1);//read analog value and put in to the variable
    for (int b = 1; b <= muest; b++) {
      delay(1);
      value += analogRead(A1);
  }
  int value0 = value/(muest+1);
  int valuep= (value0+value1)/2;
  

  Serial.println(valuep);//print serial monitor
 
  for (int a = 1; a <= 5; a++) {
    if (value > a * 20) {
      digitalWrite(a + 1, HIGH);
    } else {
      digitalWrite(a + 1, LOW);
    }
  }
}
