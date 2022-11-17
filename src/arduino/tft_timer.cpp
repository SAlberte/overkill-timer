#include <Adafruit_ST7735.h> // Hardware-specific library for ST7735

#include <BitArray.h>

#include <Fonts/FreeMonoBold12pt7b.h>

#ifdef __arm__
// should use uinstd.h to define sbrk but Due causes a conflict
extern "C"
char * sbrk(int incr);
#else // __ARM__
extern char * __brkval;
#endif // __arm__

#define TFT_CS 10
#define TFT_RST 8
#define TFT_DC 9

String TIME = "";

Adafruit_ST7735 tft = Adafruit_ST7735(TFT_CS, TFT_DC, TFT_RST);

void setup() {
  Serial.begin(9600);
  randomSeed(analogRead(0));
  tft.initR(INITR_BLACKTAB);
  tft.setRotation(1);
  tft.fillScreen(ST77XX_BLACK);

}

String formatTime(String time_) {
  int colon_counter = 0;
  String new_time = "";
  for (int i = 0; i < time_.length(); i++) {
    if (time_[i] == ':')
      colon_counter += 1;
    if (colon_counter == 2) {
      new_time = String(new_time + '\n');
      colon_counter = 0;
    }
    new_time = String(new_time + time_[i]);
  }
  return new_time;
}

void loop() {
  bool is_change = false;
  if (Serial.available() > 0) {
    TIME = Serial.readStringUntil('\n');
    is_change = true;
  }

  if (is_change) {
    Serial.println(formatTime(TIME));
    tft.fillScreen(ST77XX_BLACK);
    tft.setCursor(10, 50);
    tft.setFont( & FreeMonoBold12pt7b);
    tft.setTextColor(0xF800);
    tft.setTextSize(2);
    tft.print(formatTime(TIME));
  }

}