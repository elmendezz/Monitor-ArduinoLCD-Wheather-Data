#include <LiquidCrystal.h>

// --- CONFIGURACIÓN DE PINES (Tus pines originales) ---
// RS=12, E=11, D4=7, D5=6, D6=5, D7=4
LiquidCrystal lcd(12, 11, 7, 6, 5, 4);

const int motorPin = 2;

void setup() {
  pinMode(motorPin, OUTPUT);
  // Asumiendo que tu módulo de relevador/motor se apaga con HIGH
  digitalWrite(motorPin, HIGH); 
  
  Serial.begin(9600);
  lcd.begin(16, 2); 
  
  // Mensaje de bienvenida
  lcd.clear();
  lcd.print("Monitor Tecate");
  lcd.setCursor(0,1);
  lcd.print("Esperando PC...");
}

void loop() {
  if (Serial.available() > 0) {
    // Leemos todo el texto hasta que hay un salto de línea
    String data = Serial.readStringUntil('\n');
    data.trim();
    
    if (data.startsWith("#")) {
       actualizarPantalla(data);
    }
    else if (data == "S") {
       lcd.clear(); lcd.print("Sesion Activa");
       blinkMotor(1); 
    } 
    else if (data == "N") {
       lcd.clear(); lcd.print("Notificacion");
       blinkMotor(2);
    } 
    else if (data == "U") {
       lcd.clear(); lcd.print("Modo USB");
       blinkMotor(3);
    }
  }
}

// Función para separar el texto en dos líneas
void actualizarPantalla(String data) {
  // Quitamos el primer caracter '#'
  data = data.substring(1);
  
  int separador = data.indexOf('|');
  
  if (separador != -1) {
    String linea1 = data.substring(0, separador);
    String linea2 = data.substring(separador + 1);
    
    lcd.clear();
    
    // Imprimimos Línea 1 (Clima)
    lcd.setCursor(0,0);
    lcd.print(linea1);
    
    // Imprimimos Línea 2 (Internet)
    lcd.setCursor(0,1);
    lcd.print(linea2);
  }
}

void blinkMotor(int veces) {
  for(int k=0; k<veces; k++){
    digitalWrite(motorPin, LOW);  // Enciende
    delay(200);
    digitalWrite(motorPin, HIGH); // Apaga
    delay(200);
  }
}
