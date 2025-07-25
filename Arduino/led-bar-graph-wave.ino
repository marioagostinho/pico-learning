const uint8_t LED_PINS[] = {6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
const size_t NUM_LEDS = sizeof(LED_PINS) / sizeof(LED_PINS[0]);

void setup() {
  for (size_t i = 0; i < NUM_LEDS; ++i)
  {
    pinMode(LED_PINS[i], OUTPUT);
  }
}

void loop() {
  for (size_t i = 0; i < NUM_LEDS; ++i)
  {
    digitalWrite(LED_PINS[i], HIGH);
    delay(200);
    digitalWrite(LED_PINS[i], LOW);
  }
}