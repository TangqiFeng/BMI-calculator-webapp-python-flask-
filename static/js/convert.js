 /*

 author: Qi Fu 

 function : cm-inch, pound-kg convert function

 */

 function one() {
     var height_feet = document.getElementById("height_feet").value
     var height_inches = document.getElementById("height_inches").value
     var centimeter = document.getElementById("centimeter").value
     if (height_feet > 0 && centimeter > 0) {
         document.getElementById("height_feet").value
         document.getElementById("centimeter").value
         alert("please input ccorrectly value")
     } else if (centimeter > 0 && height_inches > 0) {
         document.getElementById("height_inches").value
         document.getElementById("centimeter").value
         alert("please input ccorrectly value")
     } else if (height_feet > 0) {
         var centimeter = height_feet * 30.48 + height_inches * 2.54
         document.getElementById("centimeter").value = Math.round(centimeter)
     } else if (centimeter > 0) {
         var height_feet = centimeter / 30.48 - height_inches * 2.54
         document.getElementById("height_feet").value = Math.floor(height_feet)
         var height_inches = (height_feet - Math.floor(height_feet)) * 12
         document.getElementById("height_inches").value = Math.round(height_inches)
     }
 }

 function clear1() {
     var height_feet = ''
     var height_inches = ''
     var centimeter = ''
     document.getElementById("height_feet").value = height_feet
     document.getElementById("height_inches").value = height_inches
     document.getElementById("centimeter").value = centimeter
 }

 function two() {
     var pound = document.getElementById("pound").value
     var kilogram = document.getElementById("kilogram").value
     if (pound > 0 && kilogram > 0) {
         document.getElementById("kilogram").value
         document.getElementById("pound").value
         alert("please input ccorrectly value")
     } else if (pound > 0) {
         var kilogram = pound * 0.4535924
         document.getElementById("kilogram").value = kilogram
     } else if (kilogram > 0) {
         var pound = kilogram * 2.2046226
         document.getElementById("pound").value = pound
     }
 }

 function clear2() {
     var pound = ''
     var kilogram = ''
     document.getElementById("pound").value = pound
     document.getElementById("kilogram").value = kilogram
 }