<?php
echo "Hello World" ;

// single-line comment

/*
This is a
multi-line comment
*/

// jerkvbfvbj
// eknvoiwern
// jwenfvownr  (***We can comment them by selecting them all using cursor and Ctrl + '/' to comment, only in VSC)

// we can use various HTML tags such as <br>, <h1>,,etc. in PHP
// for break echo "<br>";  for making bold like head  echo "<h1>...</h1>";


// VARIABLE
$variable = 45;
echo $variable;

//arthimatic operator 
$a = 3;
$b = 2;
echo $a + $b; //for adding two integer numberic variable
echo $a - $b; // for subtraction.
// we can similary other arithmatic operators. (+,-,*,/)

// assignment operator
$newVariable = $a; // This is to change any exisisting variable
//similary it can also be:
// $newVariable += 1 ..This will add 1 in 3 which is $a. We can also do 

// Logic operator
//this generally deals with AND(&&), OR (||), XOR and NOT operators(!)


//IF..ELSE CONDITION
$age = 5;
 if($age>18){
     echo "You are an adult";
 }
 elseif($age==10){
     echo "You are a decade year old";
 }
 else{
    echo "You are a kid";
 }

 //ARRAYS
 $langauges = array("Python", "C++", "PHP", "Javascript");
 echo $langauges[0] // array elements start with 0,1,2...
 //echo count($languages) .  this will let us know the number of elements in an array

 //LOOPS 
 /*
$loop_variable = 0
while($loop_variable <= 10) {
    echo "The value of loop variable is: "
    echo $loop_variable;
    $loop_variable++;
 }    
  This will make from 0 to 10.
  */

// FUNCTIONS
/*
function print5(){
    echo "FIVE;"
}
print5();
*/
//var_dump is one such function and we can define various function for executions.

?>