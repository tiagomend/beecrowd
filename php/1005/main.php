<?php

function averageOne()
{
    // Lê os valores de entrada
    $a = (float)trim(fgets(STDIN));
    $b = (float)trim(fgets(STDIN));

    // Define os pesos
    $weightOfA = 3.5;
    $weightOfB = 7.5;

    // Calcula a média ponderada
    $media = ($a * $weightOfA + $b * $weightOfB) / ($weightOfA + $weightOfB);

    // Retorna o resultado formatado
    return sprintf("MEDIA = %.5f", $media);
}

echo averageOne() . PHP_EOL;
