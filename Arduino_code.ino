#include <Wire.h>
#include <Adafruit_AMG88xx.h>

#define SERIAL_BAUDRATE 9600

Adafruit_AMG88xx amg;
void setup() {
  Serial.begin(SERIAL_BAUDRATE);
  Serial.println("Arduino initialized");

  bool status = amg.begin();
  if (!status) {
    Serial.println("Could not find a valid AMG8833 sensor, check wiring!");
    while (1);
  }
}
void loop() {

  float pixels[AMG88xx_PIXEL_ARRAY_SIZE];
  amg.readPixels(pixels);

  for (int i = 0; i < AMG88xx_PIXEL_ARRAY_SIZE; i++) {
    Serial.print(pixels[i]);
    Serial.print(",");
  }
  Serial.println(); 
  Serial.flush();   

  delay(100);
}
