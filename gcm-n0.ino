#include <Wire.h>
#include <SoftwareSerial.h>
#include <Adafruit_ADXL345_U.h>

// Bluetooth pins
const int btTx = 3;
const int btRx = 2;
SoftwareSerial bluetooth(btRx, btTx);

// Touch inputs
const int touchLeft = 5;
const int touchRight = 6;
const int touchEnableCursor = 7;

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);

// Sensitivity
const float sensitivity = 3.5;
const int deadzone = 1;

void setup() {
  bluetooth.begin(9600);
  Wire.begin();

  pinMode(touchLeft, INPUT);
  pinMode(touchRight, INPUT);
  pinMode(touchEnableCursor, INPUT);

  if (!accel.begin()) {
    bluetooth.println("NO_ADXL");
    while (1);
  }

  accel.setRange(ADXL345_RANGE_2_G);
  bluetooth.println("READY");
}

void loop() {
  sensors_event_t event;
  accel.getEvent(&event);

  bool moveEnabled = digitalRead(touchEnableCursor) == HIGH;
  bool leftClick = digitalRead(touchLeft) == HIGH;
  bool rightClick = digitalRead(touchRight) == HIGH;

  int x = 0, y = 0;
  if (moveEnabled) {
    float ax = event.acceleration.x;
    float ay = event.acceleration.y;

    if (abs(ax) > deadzone) x = (int)(ax * sensitivity);
    if (abs(ay) > deadzone) y = (int)(ay * sensitivity);

    bluetooth.print("M:");
    bluetooth.print(x);
    bluetooth.print(",");
    bluetooth.println(y);
  } else {
    bluetooth.print("C:");
    bluetooth.print(leftClick);
    bluetooth.print(",");
    bluetooth.println(rightClick);
  }

  delay(15);  // Low enough for speed, high enough for reliability
}