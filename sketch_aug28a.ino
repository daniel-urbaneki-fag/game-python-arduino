int VRx = A0; // Pino do eixo X
int VRy = A1; // Pino do eixo Y
int SW = 2;   // Pino do botão (se necessário)

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial
  pinMode(SW, INPUT_PULLUP); // Configura o botão com pull-up interno
}

void loop() {
  int xValue = analogRead(VRx); // Lê o valor do eixo X
  int yValue = analogRead(VRy); // Lê o valor do eixo Y
  int buttonState = digitalRead(SW); // Lê o estado do botão

  // Envia os valores para o computador via Serial
  Serial.print("X:");
  Serial.print(xValue);
  Serial.print(" Y:");
  Serial.print(yValue);
  Serial.print(" Button:");
  Serial.println(buttonState);

  delay(100); // Pequeno atraso para evitar sobrecarga da comunicação serial
}