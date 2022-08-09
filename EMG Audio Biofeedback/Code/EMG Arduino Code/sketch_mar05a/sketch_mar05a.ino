import Serial
void setup() {
Serial.begin(9600);
}​
​
void loop() {
// read the input on analog pin 0:
int sensorValue = analogRead(A0);
float voltage = sensorValue * (20.0 / 1023.0);
// print out the value you read:
Serial.println(voltage);
}
