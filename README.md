/*
  ===========================================================
  PROYECTO: SISTEMA DE MONITOREO CLIMÁTICO DOMÉSTICO
  MATERIA: ELECTRÓNICA
  ALUMNO: ELMENDEZZ
  ===========================================================
*/

-- TITULO DEL PROYECTO: Monitor de Temperatura y Humedad con Arduino

## Introducción
Este proyecto consiste en el diseño y construcción de un dispositivo 
electrónico casero capaz de medir las condiciones ambientales de una 
habitación. El objetivo es proporcionar una lectura constante de la 
temperatura y la humedad relativa a través de una interfaz digital.

## Objetivos del Proyecto
1. Implementar un sensor de precisión para la recolección de datos.
2. Configurar una pantalla LCD para la visualización de información.
3. Desarrollar un programa en C++ (Arduino) que gestione los periféricos.

## Materiales Utilizados
* Placa de desarrollo compatible con Arduino Uno o Nano.
* Sensor de humedad y temperatura (Modelo DHT11 o DHT22).
* Pantalla de cristal líquido (LCD) de 16x2 caracteres.
* Módulo adaptador I2C (para simplificar el cableado).
* Cables de conexión tipo jumper.
* Protoboard para el montaje de los componentes.

## Procedimiento de Montaje
1. Conexión del Sensor: Se conecta el pin de datos del sensor al pin 
   digital 2 del Arduino.
2. Conexión de la Pantalla: Se vinculan los pines SDA y SCL a las 
   entradas analógicas A4 y A5 respectivamente.
3. Alimentación: Todos los componentes se alimentan con la línea de 
   5 voltios de la placa Arduino.

## Instrucciones de Uso
1. Descargar el código fuente desde este repositorio.
2. Instalar las librerías "DHT" y "LiquidCrystal_I2C" en el IDE de Arduino.
3. Conectar la placa a la computadora mediante un cable USB.
4. Compilar y subir el programa a la placa.
5. Observar las mediciones en la pantalla instalada.

## Conclusiones
El sistema permite un control eficiente del clima interior, siendo una 
herramienta útil para el hogar y un ejercicio práctico fundamental 
para el aprendizaje de la programación y la electrónica básica.

---
-- Repositorio: https://github.com/elmendezz/Monitor-ArduinoLCD-Wheather-Data
-- Fecha: 2024
