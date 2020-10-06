void setup()
{
  Serial.begin(9600);
}

void loop()
{
  int sensorValue = analogRead(A5);
  float voltage = sensorValue * (5.0 / 1023);
  Serial.println(voltage);
  delay(5);  
}

