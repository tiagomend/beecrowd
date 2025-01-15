<?php
function simple_product()
{
    $a = intval(fgets(STDIN));
    $b = intval(fgets(STDIN));
    return "PROD = " . ($a * $b);
}

echo simple_product() . "\n";
