const uint8_t BUZZER_PIN = 15;
const uint8_t TRIG_PIN = 17;
const uint8_t ECHO_PIN = 16;

const uint16_t BUZZER_INTERVAL = 1000;
const uint16_t BUZZER_FREQ = 1000;
const uint8_t BUZZER_DURATION = 100;

const uint8_t DISTANCE_INTERVAL = 200;
const float DISTANCE_THRESHOLD = 25.f;

unsigned long lastBuzzerRead = 0;
unsigned long lastDistanceRead = 0;

unsigned long currentDistance;

void setup() {
   pinMode(BUZZER_PIN, OUTPUT);
   pinMode(TRIG_PIN, OUTPUT);
   pinMode(ECHO_PIN, INPUT);
}

void loop() {
  const unsigned long currentMillis = millis();

  if (currentMillis - lastDistanceRead >= DISTANCE_INTERVAL)
  {
    lastDistanceRead = currentMillis;
    currentDistance = GetDistance();
  }

  if (currentDistance > DISTANCE_THRESHOLD)
  {
    noTone(BUZZER_PIN);
  }
  else
  {
    const float newBuzzerInterval = (currentDistance * BUZZER_INTERVAL) / DISTANCE_THRESHOLD;

    if (currentMillis - lastBuzzerRead >= newBuzzerInterval)
    {
      lastBuzzerRead = currentMillis;
      tone(BUZZER_PIN, BUZZER_FREQ, BUZZER_DURATION); 
    }
  }
}

float GetDistance()
{
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  const long duration = pulseIn(ECHO_PIN, HIGH);
  const float distance = duration * 0.034 / 2;

  return distance;
}