int trig=D4;
int echo=D3;
int distance;
int tim;
void setup() {
Serial.begin(9600);
pinMode(trig,OUTPUT);
pinMode(echo,INPUT);

}

void loop() {
digitalWrite(12,LOW);
digitalWrite(trig,HIGH);
delay(1000);
digitalWrite(trig,LOW);
tim=pulseIn(echo,HIGH);
distance=(tim*0.034)/2;
Serial.print("distance");
Serial.println(distance);
}
