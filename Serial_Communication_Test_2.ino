#include <Tone.h>

// Initializing tones
Tone tone1;
Tone tone2;
Tone tone3;

// Initializing scan stuffs
String input;
int ledState1 = HIGH;
int ledState2 = HIGH;
int ledState3 = HIGH;
const int ledPin1 = 5;
const int ledPin2 = 6;
const int ledPin3 = 7;

// Begin Serial Communication and Tones
void setup() {
  Serial.begin(9600);
  Serial.flush();
  Serial.setTimeout(50);

  tone1.begin(8);
  tone2.begin(9);
  tone3.begin(10);

  pinMode(ledPin1, OUTPUT);
  pinMode(ledPin2, OUTPUT);
  pinMode(ledPin3, OUTPUT);
  digitalWrite(ledPin1, HIGH);
  digitalWrite(ledPin2, HIGH);
  digitalWrite(ledPin3, HIGH);

  Serial.println("Script starting...");
}

//Main Loop
void loop() {  

  //Scans for input in Serial
  if (Serial.available()){
    char received = Serial.read();
    input += received;

    //If something is entered into Serial...
    if (received == '\n'){
      
      //Shut off existing tone
      if (input.length() == 3){
        String driveStr = input.substring(0,1);
        int drive = driveStr.toInt();
        
        String stateStr = input.substring(1,2);
        int state = stateStr.toInt();  
        
        if(drive == 1){
          tone1.stop();
          
          if (ledState1 == LOW) {
            ledState1 = HIGH;
          } else {
            ledState1 = LOW;
          }

          // set the LED with the ledState of the variable:
          digitalWrite(ledPin1, ledState1);
          
        }
        
        if(drive == 2){
          tone2.stop();
          
          if (ledState2 == LOW) {
            ledState2 = HIGH;
          } else {
            ledState2 = LOW;
          }
      
          // set the LED with the ledState of the variable:
          digitalWrite(ledPin2, ledState2);
          
        }
        if(drive == 3){
          tone3.stop();

          if (ledState3 == LOW) {
            ledState3 = HIGH;
          } else {
            ledState3 = LOW;
          }

          // set the LED with the ledState of the variable:
          digitalWrite(ledPin3, ledState3);
          
        }
      }

      //Start tone with 2-digit hertz rate
      if (input.length() == 5){

        
        String driveStr = input.substring(0,1);
        int drive = driveStr.toInt();
        
        String noteStr = input.substring(1,3);
        int note = noteStr.toInt();
            
        String stateStr = input.substring(3,4);
        int state = stateStr.toInt();  
        if(drive == 1){
          tone1.play(note);
        }
        if(drive == 2){
          tone2.play(note);
        }
        if(drive == 3){
          tone3.play(note);
        }
      }

      //Start tone with 3-digit hertz rate
      if (input.length() == 6){
        String driveStr = input.substring(0,1);
        int drive = driveStr.toInt();
        
        String noteStr = input.substring(1,4);
        int note = noteStr.toInt();
            
        String stateStr = input.substring(4,5);
        int state = stateStr.toInt();  
        if(drive == 1){
          tone1.play(note);
        }
        if(drive == 2){
          tone2.play(note);
        }
        if(drive == 3){
          tone3.play(note);
        }
      }

      //Start tone with 4-digit hertz rate
      if (input.length() == 7){
        String driveStr = input.substring(0,1);
        int drive = driveStr.toInt();
        
        String noteStr = input.substring(1,5);
        int note = noteStr.toInt();
            
        String stateStr = input.substring(5,6);
        int state = stateStr.toInt();  
        if(drive == 1){
          tone1.play(note);
        }
        if(drive == 2){
          tone2.play(note);
        }
        if(drive == 3){
          tone3.play(note);
        }
      }

      //Resets input after each command
      input = "";
    }
  }
}


