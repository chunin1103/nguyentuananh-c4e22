var height = 30;
var weight = 40;
function BMI(weight, height){
    return (weight / height) / height; ;
}
BMI(231,23)
if (BMI < 16){
    answer ='Severely Underweighted';
}
else if (16 <= BMI <18.5){
    answer ='Underweight';
}
else if (18.5 <= BMI <25){
    answer ='Normal';
}
else if (25 <= BMI <30){
    answer ='Overweight';
}
else if (30 < BMI){
    answer ='Obese man';
}
else {
    answer ='r you not human ;)';
}
var d = 1 + 2 + "3";      

<!DOCTYPE html>
<html>
<body>

<script>
function BMI() {
    var weight = 17; 
    var height = 170/100;
    var greeting;
    if (weight < 18) {
        greeting = "Good dfyfeafa";
    } else {
        greeting = "Good evening";
    }
    document.write(greeting);
}
BMI()
</script>

</body>
</html>
