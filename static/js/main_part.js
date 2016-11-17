 /*

 author: Tangqi Feng 

 function : calculate the BMI

 */


 function lookme(form) {
     var bmi;
     if (!checkform(form)) return false;
     comput(form);
     bmi = form.weight.value * 10000 / eval(form.height.value * form.height.value);
     form2.bmi.value = bmi;
     if (bmi > 40) {
         form2.nowstat.value = "Oh, you can buy clothes ? You too, too ... too fat";
     } else if (bmi > 30) {
         form2.nowstat.value = "Wow ! You're too fat ! Must start to lose weight, listen to me right";
     } else if (bmi > 27) {
         form2.nowstat.value = "Damn ! You are more fat, and quickly began to lose weight plan !";
     } else if (bmi > 22) {
         form2.nowstat.value = "Be careful ! A little fat, you can eat less ? Also a lot of exercise ! :)";
     } else if (bmi >= 21) {
         form2.nowstat.value = "I am so envious of you,You have a devil figure ! :)";
     } else if (bmi >= 18) {
         form2.nowstat.value = "A little thin,You should eat more !";
     } else if (bmi >= 16) {
         form2.nowstat.value = "You must have been abused, hurry to eat a lot !";
     } else {
         form2.nowstat.value = "Wow ! Front chest back, just like a wire pole.You need to see a doctor !!";
     }
     return true;
 }

 function comput(form) {
     if (form.sex.options.selectedIndex == "0")
         form2.legendweight.value = Math.round(50 + (2.3 * (form.height.value - 152)) / 2.54);
     else
         form2.legendweight.value = Math.round(45.5 + (2.3 * (form.height.value - 152)) / 2.54);
 }

 function checkform(form) {
     if (form.weight.value == null || form.weight.value.length == 0 ||
         form.height.value == null || form.height.value.length == 0) {
         alert("Do you think I am God ? You do not tell me anything, how do I calculate !!!");
         return false;
     }
     if (form.weight.value <= 0) {
         alert("You will hit the lightest Guinness world record, be careful of gravity does not work for you !");
         return false;
     }
     if (form.weight.value > 500) {
         alert("You do not test, Your weight has crushed my scales.");
         return false;
     }
     if (form.height.value <= 0) {
         alert("You so short, smaller than the ants ?");
         return false;
     }
     if (form.height.value >= 300) {
         alert("you are so tall ! Can you help me pick the stars ?");
         return false;
     }
     return true;
 }

 function ClearForm() {
     form2.bmi.value = "";
     form2.nowstat.value = "";
     form2.legendweight.value = "";
 }