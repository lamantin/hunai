<?php

$text ='"Egy parafa dugó, mely semmiben sem különbözött a többi parafa dugótól (Hirt G. Sándornak mondta magát, de mit jelent egy név? Egy név semmit se jelent), beleesett a vízbe.

Egy ideig, amint az várható volt, úszott a víz színén, aztán különös dolog történt. Lassan merülni kezdett, lesüllyedt a fenékre, és nem jött föl többé.

Magyarázat nincs"';
$cmd = "espeak -vhu+f5 ".$text;

shell_exec($cmd);
