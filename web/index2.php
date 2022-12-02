<html>

<head>

<title>Компания "Торговый мир"</title>

</head>

<body>

<?
#error_reporting(E_ALL);
#exec("E: "  );
#exec("cd e:\_py\bots\_MariBot\results");


#chdir("e:\_py\bots\_MariBot\results")
#exec("python stat_count.py");

#exec("E: && cd e:\_py\bots\_MariBot\results && python stat_count.py"  );

$run = "python e:\_py\bots\_MariBot\results\stat_count_v2.py $_POST[role]";
$run2 = "E: && cd e:\_py\bots\_MariBot && python stat_count_v2.py $_POST[role]";
exec($run2);



$fh = fopen('stat2','r');
$all = fgets($fh);
$tmp1 = explode(" ",fgets($fh));
$tmp2 = explode(" ",fgets($fh));
$tmp3 = explode(" ",fgets($fh));
$tmp4 = explode(" ",fgets($fh));
$tmp5 = explode(" ",fgets($fh));
$tmp6 = explode(" ",fgets($fh));
$tmp7 = explode(" ",fgets($fh));
$tmp8 = explode(" ",fgets($fh));
$tmp9 = explode(" ",fgets($fh));
$tmp10 = explode(" ",fgets($fh));
$tmp11 = explode(" ",fgets($fh));
$tmp12 = explode(" ",fgets($fh));
$tmp13 = explode(" ",fgets($fh));

if($_POST['role'] == 'role_1')
$role = "студент";
if($_POST['role'] == 'role_2')
$role = "школьник";
if($_POST['role'] == 'role_3')
$role = "госслужащий";
if($_POST['role'] == 'role_4')
$role = "Пенсионер";
if($_POST['role'] == 'role_5')
$role = "Фрилансер";
if($_POST['role'] == 'role_6')
$role = "Безработный";
if($_POST['role'] == 'role_7')
$role = "Домохозяйка";
?>  

<h1>Статистика <?= $result1?></h1>
<h1>Роль: <?echo $role?></h1>
<h1>Методика пройдена  <?=$all?> раз</h1>
<?php
  // The global $_POST variable allows you to access the data sent with the POST method by name
  // To access the data sent with the GET method, you can use $_GET
  $say = htmlspecialchars($_POST['role']);
  $to  = htmlspecialchars($_POST['to']);

  //echo  $say, ' ', $to;
  //echo $run2;
?>


<b>Таблица распределения дисфункции и компенсаторных механизмов по шкалам опросника</b>.<br>

<table border="2" align="center" cellpadding="10">

<tr>

<td bgcolor="yellow" align="center"><b>N/N</b></td>

<td bgcolor="yellow" align="center"><b>Дисфункция</b></td>

<td bgcolor="yellow" align="center"><b>Норма</b></td>

<td bgcolor="yellow" align="center"><b>Компенсация</b></td>

</tr>

<tr>

<td align="center">Шкала 1. Выраженность аффективных переживаний субъекта и его отношения к ним</td>

<td align="center"><?= $tmp1[0]?> (<?= number_format(($tmp1[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp1[0] - $tmp1[1] ?> (<?= number_format((($all - $tmp1[0] - $tmp1[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp1[1]?> (<?= number_format(($tmp1[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Шкала 2. Степень опредмеченности желания субъекта</td>

<td align="center"><?= $tmp2[0]?> (<?= number_format(($tmp2[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp2[0] - $tmp1[1] ?> (<?= number_format((($all - $tmp2[0] - $tmp2[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp2[1]?> (<?= number_format(($tmp2[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Шкала 3. Cтепень активности взаимодействия субъекта с реальностью</td>

<td align="center"><?= $tmp3[0]?> (<?= number_format(($tmp3[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp3[0] - $tmp3[1] ?> (<?= number_format((($all - $tmp3[0] - $tmp3[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp3[1]?> (<?= number_format(($tmp3[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Шкала 4. Умение прогнозировать результат предпринимаемых действий</td>

<td align="center"><?= $tmp4[0]?> (<?= number_format(($tmp4[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp4[0] - $tmp4[1] ?> (<?= number_format((($all - $tmp4[0] - $tmp4[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp4[1]?> (<?= number_format(($tmp4[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Шкала 5. Межличностное взаимодействие субъекта</td>

<td align="center"><?= $tmp5[0]?> (<?= number_format(($tmp5[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp5[0] - $tmp5[1] ?> (<?= number_format((($all - $tmp5[0] - $tmp5[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp5[1]?> (<?= number_format(($tmp5[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Шкала 6. Cостояние самооценки субъекта</td>

<td align="center"><?= $tmp6[0]?> (<?= number_format(($tmp6[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp6[0] - $tmp6[1] ?> (<?= number_format((($all - $tmp6[0] - $tmp6[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp6[1]?> (<?= number_format(($tmp6[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Шкала 7. Отношение к негативному опыту и степень фиксированности на имеющихся затруднениях</td>

<td align="center"><?= $tmp7[0]?> (<?= number_format(($tmp7[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp7[0] - $tmp7[1] ?> (<?= number_format((($all - $tmp7[0] - $tmp7[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp7[1]?> (<?= number_format(($tmp7[1]*100/$all), 2)?>%)</td>

</tr>

</table>

<b>Таблица распределения дисфункции и компенсации по механизмам методики</b>.<br>

<table border="2" align="center" cellpadding="10">

<tr>

<td bgcolor="yellow" align="center"><b>N/N</b></td>

<td bgcolor="yellow" align="center"><b>Дисфункция</b></td>

<td bgcolor="yellow" align="center"><b>Норма</b></td>

<td bgcolor="yellow" align="center"><b>Компенсация</b></td>

</tr>

<tr>

<td align="center">Механизм самоопредмечивания</td>

<td align="center"><?= $tmp8[0]?> (<?= number_format(($tmp8[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp8[0] - $tmp8[1] ?> (<?= number_format((($all - $tmp8[0] - $tmp8[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp8[1]?> (<?= number_format(($tmp8[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Механизм самооценивания</td>

<td align="center"><?= $tmp9[0]?> (<?= number_format(($tmp9[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp9[0] - $tmp9[1] ?> (<?= number_format((($all - $tmp9[0] - $tmp9[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp9[1]?> (<?= number_format(($tmp9[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Механизм самоформирования</td>

<td align="center"><?= $tmp10[0]?> (<?= number_format(($tmp10[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp10[0] - $tmp10[1] ?> (<?= number_format((($all - $tmp10[0] - $tmp10[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp10[1]?> (<?= number_format(($tmp10[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Механизм самоотеждествления</td>

<td align="center"><?= $tmp11[0]?> (<?= number_format(($tmp11[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp11[0] - $tmp11[1] ?> (<?= number_format((($all - $tmp11[0] - $tmp11[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp11[1]?> (<?= number_format(($tmp11[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Механизм самоопределения</td>

<td align="center"><?= $tmp12[0]?> (<?= number_format(($tmp12[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp12[0] - $tmp12[1] ?> (<?= number_format((($all - $tmp12[0] - $tmp12[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp12[1]?> (<?= number_format(($tmp12[1]*100/$all), 2)?>%)</td>

</tr>

<tr>

<td align="center">Механизм самоодобрения</td>

<td align="center"><?= $tmp13[0]?> (<?= number_format(($tmp13[0]*100/$all), 2)?>%)</td>

<td align="center"><?=$all - $tmp13[0] - $tmp13[1] ?> (<?= number_format((($all - $tmp13[0] - $tmp13[1])*100/$all), 2)?>%)</td>

<td align="center"><?= $tmp13[1]?> (<?= number_format(($tmp13[1]*100/$all), 2)?>%)</td>

</tr>

</table>

<?php
fclose($fh); 
?>

Более подробно об ассортименте товаров и услуг вы можете узнать в нашем отделе сбыта.

</body>

</html>