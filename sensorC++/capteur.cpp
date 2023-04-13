#include <wiringPi.h>
#include <iostream>
#include <fstream>
#include <unistd.h>
#include <python.h>

const int num_leds = 64;
APA102 strip(num_leds, 0, 0);

int main(void)
{
    wiringPiSetupGpio();
    pinMode(17, INPUT);

    strip.clearStrip();
    strip.show();

    int i = 0;

    while (1) {
        if (digitalRead(17)) {
            i++;
            strip.clearStrip();
            for (int j = 0; j < num_leds; j++) {
                strip.setPixelColor(j, 0xFF0000); // Rouge
            }
            strip.show();
        } else {
            strip.clearStrip();
            strip.show();
        }
        delay(55);
    }

    return 0;
}
