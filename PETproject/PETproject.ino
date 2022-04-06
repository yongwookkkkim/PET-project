// if the floor is necessary
#include <Servo.h>

const int rodHoriControl=10;
const int rodVertControl=11;
const int wheelControl=9;
const int bottleCheck0=A0;
const int bottleCheck1=A1;
const int bottleCheck2=A2;
const int bottleCheck3=A3;
const int bottleDistance=900;
int bottlePlace;

void setup() {
  for (int i=wheelControl; i<=rodVertControl; i++){
    pinMode(i, OUTPUT);
  }
  Serial.begin(38400);
}

void loop() {
  // store current place of the rod
  int currentRodPlace=bottlePlace;

  // find the position of the bottle label
  if (analogRead(bottleCheck0)>=bottleDistance){
    bottlePlace=0;
  }
  else if (analogRead(bottleCheck1)>=bottleDistance){
    bottlePlace=1;
  }
  else if (analogRead(bottleCheck2)>=bottleDistance){
    bottlePlace=2;
  }
  else if (analogRead(bottleCheck3)>=bottleDistance){
    bottlePlace=3;
  }
  else{
    // this means no bottle
  }
  // adjustRodHeight
  // pump in
  delay(500);
  // pump stop
  delay (1000);
  // push rods
  // spin wheel
  delay (1000);
  // pull rods
  // stop wheel
  delay(500);
  // hereafter optional
  // open floor
  delay(2000);
  //close floor
  delay(1000);
}

void adjustRodHeight(int bottlePlace, int currentRodPlace){
  int timePerFloor=1000;
  // digitalWrite(rodVertControl, HIGH);
  // delay((bottlePlace - currentRodPlace)*bottle);
  // digitalWrite(rodVertControl, LOW);
}
