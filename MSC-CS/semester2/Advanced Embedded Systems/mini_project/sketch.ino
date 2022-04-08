#include <Keypad.h>
#include <LiquidCrystal_I2C.h>

const int ROW    = 4; // four rows
const int COLUMN = 4; // four columns

char keyMap[ROW][COLUMN] = {
  {'1','2','3', 'A'},
  {'4','5','6', 'B'},
  {'7','8','9', 'C'},
  {'*','0','#', 'D'}
};

byte pinRows[ROW] = {9, 8, 7, 6};      // connect to the row pinouts of the keypad
byte pinColumns[COLUMN] = {5, 4, 3, 2}; // connect to the column pinouts of the keypad

Keypad keypad = Keypad(makeKeymap(keyMap), pinRows, pinColumns, ROW, COLUMN);
LiquidCrystal_I2C lcdDisplay(0x27, 16, 2); // I2C address 0x27, 16 column and 2 rows

int cursorColumn = 0;
int cursorRow = 0;

void setup(){
	// initialize the LCD.
	lcdDisplay.init();
	lcdDisplay.backlight();
}

void loop(){
  char key = keypad.getKey();

  if (key) {

    lcdDisplay.setCursor(cursorColumn, cursorRow); 
    lcdDisplay.print(key);
    cursorColumn++;


    if(cursorColumn == 16) {        
      cursorColumn = 0;
      cursorRow = 1;
      
    }  

    if(cursorRow == 1  && cursorColumn == 5) {
      lcdDisplay.clear();
      cursorColumn = 0;
      cursorRow = 0;   
    }  
   
  }
}