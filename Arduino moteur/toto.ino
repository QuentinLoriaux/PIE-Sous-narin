#include <Servo.h>

Servo esc; // Crée un objet de type Servo pour contrôler l'ESC

void setup() {
  esc.attach(9); // Connecte l'ESC au pin 9 de l'Arduino
  esc.writeMicroseconds(1000); // Envoie une impulsion de 1000 microsecondes pour initialiser l'ESC
  delay(2000); // Attendez 2 secondes pour laisser l'ESC s'initialiser
}

void loop() {
  esc.writeMicroseconds(1500); // Envoie une impulsion de 1500 microsecondes pour maintenir le moteur à la position neutre
  delay(5000); // Attendez 5 secondes

  esc.writeMicroseconds(2000); // Envoie une impulsion de 2000 microsecondes pour accélérer le moteur à pleine vitesse
  delay(5000); // Attendez 5 secondes

  esc.writeMicroseconds(1000); // Envoie une impulsion de 1000 microsecondes pour arrêter le moteur
  delay(5000); // Attendez 5 secondes
}