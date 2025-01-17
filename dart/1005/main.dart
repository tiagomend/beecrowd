import 'dart:io';

void main() {
  print(averageOne());
}

String averageOne() {
  // Lê os valores de entrada
  double a = double.parse(stdin.readLineSync()!);
  double b = double.parse(stdin.readLineSync()!);

  // Define os pesos
  double weightOfA = 3.5;
  double weightOfB = 7.5;

  // Calcula a média ponderada
  double media = (a * weightOfA + b * weightOfB) / (weightOfA + weightOfB);

  // Retorna o resultado formatado
  return 'MEDIA = ${media.toStringAsFixed(5)}';
}
