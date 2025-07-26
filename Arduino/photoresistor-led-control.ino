const uint8_t SENSOR_PIN = 28;
const uint8_t LED_PIN = 15;

const uint16_t LIGHT_THRESHOLD = 500;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  const int sensorValue = analogRead(SENSOR_PIN);
  digitalWrite(LED_PIN, sensorValue >= LIGHT_THRESHOLD ? HIGH : LOW);

  delay(500);
}
