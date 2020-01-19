
document.getElementById('demo').innerHTML = Date()
JavaScript accepts both double and single quotes
change html attribute values: <button onclick="document.getElementById('myImage').src='pic_bulbon.gif'">Turn on the light</button>
<button type="button" onclick="document.getElementById('demo').style.fontSize='35px'">Click Me!</button> change css
document.getElementById("demo").style.display = "none";
document.getElementById("demo").style.display = "block";  # show element
<img src="img/2019-04-23-10-03-21.png">
Old JavaScript examples may use a type attribute: <script type="text/javascript">. The type attribute is not required. JavaScript is the default scripting language in HTML.
The function is invoked (called) when a button is clicked:
<img src="img/2019-04-23-10-04-37.png">
document.getElementById("demo").innerHTML = 5 + 6;
<script>document.write(5 + 6);</script>  # using it after load will delete element
window.alert(5 + 6);
multiple statements on one line are allowed when seperated by semicolons
a = 5; b = 6; c = a + b;  ## Ending statements with semicolon is not required, but highly recommended.
For best readability, programmers often like to avoid code lines longer than 80 characters.
document.getElementById("demo").innerHTML =
"Hello Dolly!";
<img src="img/2019-04-23-10-09-11.png">
JavaScript keywords are used to identify actions to be performed.The var keyword tells the browser to create variables:
In JavaScript, identifiers are used to name variables (and keywords, and functions, and labels).
Numbers are not allowed as the first character.
<img src="img/2019-04-23-10-11-50.png">
JavaScript uses the Unicode character set.
After the declaration, the variable has no value (technically it has the value of undefined).
It's a good programming practice to declare all variables at the beginning of a script.
var person = "John Doe", carName = "Volvo", price = 200;  # seperated by comma and ended by semicolon
<img src="img/2019-04-23-10-19-10.png">
 <img src="img/2019-04-23-10-19-51.png">
 var x = "5" + 2 + 3;   # 523
var x = 2 + 3 + "5";   # 55
 <img src="img/2019-04-23-10-38-46.png">
 The **= operator is an experimental part of the ECMAScript 2016 proposal (ES7). It is not stable across browsers. Do not use it.
JavaScript Types are Dynamic
var y = 123e5;      // 12300000
var z = 123e-5;     // 0.00123
car = undefined;    // Value is undefined, type is undefined
An empty value has nothing to do with undefined.
var car = "";    // The value is "", the typeof is "string"
You can empty an object by setting it to null:
person = null;    // Now value is null, but type is still an object
You can consider it a bug in JavaScript that typeof null is an object. It should be null.
You can also empty an object by setting it to undefined:
person = undefined;   // Now both value and type is undefined
typeof null                // object
A primitive data value is a single simple data value with no additional properties and methods: string number boolean undefined
Complex Data (function object)
A JavaScript function is defined with the function keyword, followed by a name, followed by parentheses ().
Functions often compute a return value. The return value is "returned" back to the "caller":
<img src="img/2019-04-23-10-50-01.png">
JavaScript objects are containers for named values called properties or methods. (The values are written as name:value pairs (name and value separated by a colon).)
<img src="img/2019-04-23-10-52-08.png">
A method is a function stored as a property which is actions that can be performed on objects.
<img src="img/2019-04-23-10-53-24.png">
<img src="img/2019-04-23-10-54-04.png">
HTML allows event handler attributes, with JavaScript code, to be added to HTML elements with single quotes or double quotes
In the following example, an onclick attribute (with code), is added to a <button> element:
<button onclick="this.innerHTML = Date()">The time is?</button>
<button onclick="displayDate()">The time is?</button>
<img src="img/2019-04-23-10-58-06.png">
var sln = txt.length;
escape : The 6 escape characters down below originally designed to control typewriters, teletypes, and fax machines. They do not make any sense in HTML.
<img src="img/2019-04-23-10-59-09.png">
<img src="img/2019-04-23-11-00-22.png">
Safe way : document.getElementById("demo").innerHTML = "Hello " +
"Dolly!";
Don't create strings as objects. It slows down execution speed.
The new keyword complicates the code. This can produce some unexpected results:
When using the === operator, equal strings are not equal, because the === operator expects equality in both type and value.Or even worse. Objects cannot be compared: Even without strict mode
<img src="img/2019-04-23-11-02-07.png">
var pos = str.indexOf("locate");
var pos = str.lastIndexOf("locate");
Both indexOf(), and lastIndexOf() return -1 if the text is not found.
var pos = str.indexOf("locate", 15);   # starting position
var pos = str.search("locate");
The search() method cannot take a second start position argument.
The indexOf() method cannot take powerful search values (regular expressions).
JavaScript Numbers are Always 64-bit Floating Point. This format stores numbers in 64 bits, where the number (the fraction) is stored in bits 0 to 51, the exponent in bits 52 to 62, and the sign in bit 63:
Integers (numbers without a period or exponent notation) are accurate up to 15 digits.
The maximum number of decimals is 17, but floating point arithmetic is not always 100% accurate:
var x = 0.2 + 0.1;         // x will be 0.30000000000000004
To solve the problem above, it helps to multiply and divide:
var x = (0.2 * 10 + 0.1 * 10) / 10;       // x will be 0.3
(123).toString();        // returns 123 from literal 123
(100 + 23).toString();   // returns 123 from expression 100 + 23
<img src="img/2019-04-23-11-08-09.png">
var x = 9.656;  // toFixed(2) is perfect for working with money.  return a string
x.toFixed(0);           // returns 10 string
x.toFixed(2);           // returns 9.66 string
var x = 9.656;
x.toPrecision();        // returns 9.656
x.toPrecision(2);       // returns 9.7   // 2 number
x.toPrecision(4);       // returns 9.656
valueOf() returns a number as a number.
var x = 123;
x.valueOf();            // returns 123 from variable x  The valueOf() method is used internally in JavaScript to convert Number objects to primitive values.
Number(true);          // returns 1
Number(false);         // returns 0
Number("10");          // returns 10
Number(new Date("2017-09-30"));    // returns 1506729600000   the number of milliseconds since 1.1.1970
// only the first number is converted
parseInt("10");         // returns 10
parseInt("10.33");      // returns 10
parseInt("10 20 30");   // returns 10
parseInt("10 years");   // returns 10
parseInt("years 10");   // returns NaN
parseFloat("10");        // returns 10
parseFloat("10.33");     // returns 10.33
POSITIVE_INFINITY is returned on overflow: var x = 1 / 0;
Trying to do arithmetic with a non-numeric string will result in NaN (Not a Number):  var x = 100 / "Apple";  // x will be NaN (Not a Number)
Putting a comma after the last element (like "BMW",)  is inconsistent across browsers.
IE 8 and earlier will fail.
var cars = [
  "Saab",
  "Volvo",
  "BMW",
];
Arrays are a special type of objects. The typeof operator in JavaScript returns "object" for arrays.
But, JavaScript arrays are best described as arrays.
Arrays use numbers to access its "elements". In this example, person[0] returns John:Objects use names to access its "members".
var x = cars.length;   // The length property returns the number of elements
var y = cars.sort();   // The sort() method sorts arrays
fruits.length;   // the length of fruits is 4（The length property is always one more than the highest array index.）
Access the laste array element var last = fruits[fruits.length - 1];
<img src="img/2019-04-23-11-17-40.png">
<img src="img/2019-04-23-11-18-47.png">
fruits.push("Lemon");    // adds a new element (Lemon) to fruits （push to the end）
or fruits[fruits.length] = "Lemon";    // adds a new element (Lemon) to fruits
Adding elements with higher indexes than length-1 can create undefined "holes" in an array:
Many programming languages support arrays with named indexes.
Arrays with named indexes are called associative arrays (or hashes).
JavaScript does not support arrays with named indexes.
In JavaScript, arrays always use **numbered** indexes.
If you use named indexes, JavaScript will redefine the array to a standard object.
After that, some array methods and properties will produce incorrect results.
<img src="img/2019-04-23-11-24-42.png">
<img src="img/2019-04-23-11-25-49.png">
typeof fruits;    // returns object
Array.isArray(fruits);   // To solve this problem ECMAScript 5 defines a new method returns true
The problem with this solution is that ECMAScript 5 is not supported in older browsers.
<img src="img/2019-04-23-11-28-21.png">
Or more precisely: it returns true if the object prototype contains the word "Array". //  indexOf("Array") > -1  = contain or include
fruits instanceof Array;   // returns true. The instanceof operator returns true if an object is created by a given constructor:
document.getElementById("demo").innerHTML = fruits.toString(); //Banana,Orange,Apple,Mango
document.getElementById("demo").innerHTML = fruits.join(" * ");
fruits.pop();              // Pop the end push the end   shift the first unshift the first
fruits[fruits.length] = "Kiwi";          // Appends "Kiwi" to fruits
delete fruits[0];           // Changes the first element in fruits to undefined
Using delete may leave undefined holes in the array. Use pop() or shift() instead.
fruits.splice(2, 0, "Lemon", "Kiwi");   // The second parameter (0) defines how many elements should be removed.
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 2, "Lemon", "Kiwi");
var myChildren = myGirls.concat(myBoys);   // Concatenates (joins) myGirls and myBoys
var myChildren = arr1.concat(arr2, arr3);   // Concatenates arr1 with arr2 and arr3
var myChildren = arr1.concat(["Emil", "Tobias", "Linus"]);
var citrus = fruits.slice(1);   // slice into a new array starting from index 1
var fruits = ["Banana", "Orange", "Lemon", "Apple", "Mango"];
var citrus = fruits.slice(1, 3);   // [orange, lemon] not including 3
All JavaScript objects have a toString() method.
fruits.sort();        // Sorts the elements of fruits   alphabetically
You can use it to sort an array in descending order: (reverse)
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.sort();        // First sort the elements of fruits
fruits.reverse();     // Then reverse the order of the elements
By default, the sort() function sorts values as strings. So it doesn't work for numbers, for example : "25" is bigger than "100"
Use a compare function to solve this problem
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
array descending
points.sort(function(a, b){return b - a});
If the result is negative a is sorted before b.
If the result is positive b is sorted before a.
If the result is 0 no changes is done with the sort order of the two values.
Sorting an Array in Random Order  points.sort(function(a, b){return 0.5 - Math.random()});
There are no built-in functions for finding the max or min value in an array :
var points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});
// now points[0] contains the lowest value
// and points[points.length-1] contains the highest value
Sorting a whole array is a very inefficient method if you only want to find the highest (or lowest) value.
function myArrayMax(arr) {
  return Math.max.apply(null, arr);
}  // = Math.max.apply(null, [1, 2, 3]) is equivalent to Math.max(1, 2, 3).
Math.min.apply(null, [1, 2, 3]) is equivalent to Math.min(1, 2, 3).
The fastest solution is to use a "home made" method.
This function loops through an array comparing each value with the highest value found:
<img src="img/2019-04-23-11-42-30.png">
<img src="img/2019-04-23-11-43-11.png">
sort objects in array
<img src="img/2019-04-23-11-44-07.png">
<img src="img/2019-04-23-11-44-27.png">
function myFunction(value, index, array) {
  txt = txt + value + "<br>";
}
possible to rewrite to
function myFunction(value) {
  txt = txt + value + "<br>";
}
The map() method creates a new array by performing a function on each array element.
function myFunction(value, index, array) {
  return value * 2;
}
function myFunction(value) {
  return value * 2;
}
The filter() method creates a new array with array elements that passes a test.
var numbers = [45, 4, 9, 16, 25];
var over18 = numbers.filter(myFunction);

function myFunction(value, index, array) {
  return value > 18;
}    // same to just use the value
The reduce() method runs a function on each array element to produce (reduce it to) a single value.
var numbers1 = [45, 4, 9, 16, 25];
var sum = numbers1.reduce(myFunction);

function myFunction(total, value, index, array) {
  return total + value;
}
=
function myFunction(total, value) {
  return total + value;
}
The reduce() method can accept an initial value:
function myFunction(total, value) {
  return total + value;
}

The reduceRight() works from right-to-left in the array. See also reduce().

The every() method check if all array values pass a test.
function myFunction(value, index, array) {
  return value > 18;
}

The some() method check if some array values pass a test.
var fruits = ["Apple", "Orange", "Apple", "Mango"];
var a = fruits.indexOf("Apple");
Array.indexOf() returns -1 if the item is not found.
array.indexOf(item, start)
Array.lastIndexOf() is the same as Array.indexOf(), but searches from the end of the array.

The find() method returns the value of the first array element that passes a test function.

The findIndex() method returns the index of the first array element that passes a test function.
## JavaScript Date Objects
var d = new Date();
7 numbers specify year, month, day, hour, minute, second, and millisecond (in that order):
var d = new Date(2018, 11, 24, 10, 33, 30, 0);   // Mon Dec 24 2018 10:33:30 GMT+0100 (Central European Standard Time)  ///// JavaScript counts months from 0 to 11.
You cannot omit month. If you supply only one parameter it will be treated as milliseconds. // instead of year
var d = new Date(99, 11, 24);    // == 1999 Dec
var d = new Date(9, 11, 24);  // == 1909 Dec
### data string
var d = new Date("October 13, 2014 11:13:00");
JavaScript stores dates as number of milliseconds since January 01, 1970, 00:00:00 UTC (Universal Time Coordinated). Now the time is: 1556027665410 milliseconds past January 01, 1970
**Zero time is January 01, 1970 00:00:00 UTC.**
new Date(milliseconds) creates a new date object as zero time plus milliseconds:
var d = new Date(100000000000);
var d = new Date(-100000000000);
One day (24 hours) is 86 400 000 milliseconds.
When you display a date object in HTML, it is automatically converted to a string, with the toString() method.
document.getElementById("demo").innerHTML = d;   ===  document.getElementById("demo").innerHTML = d.toString();
The toUTCString() method converts a date to a UTC string (a date display standard).
The toDateString() method converts a date to a more readable format:
<img src="img/2019-04-23-16-02-00.png">
The ISO 8601 syntax (YYYY-MM-DD) is also the preferred JavaScript date format: var d = new Date("2015-03-25");
### data methods
getTime() getFullYear() getMonth() 0-11  getDate() 1-31 getHours() 0-23 getMinutes() 0-59 The getDay() method returns the weekday of a date as a number (0-6):
var months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
document.getElementById("demo").innerHTML = months[d.getMonth()];
### data set methods
setFullYear()
## Math
The JavaScript Math object allows you to perform mathematical tasks on numbers.
Math.PI;            // returns 3.141592653589793
Math.round(4.7);    // returns 5
Math.round(4.4);    // returns 4
Math.pow(8, 2);      // returns 64
Math.sqrt(64);      // returns 8
Math.abs(x) returns the absolute (positive) value of x:
ceil floor sin cos min max random (0-1, inclusive-exclusive) //float
Math.E        // returns Euler's number
Math.PI       // returns PI
Math.SQRT2    // returns the square root of 2
Math.SQRT1_2  // returns the square root of 1/2
Math.LN2      // returns the natural logarithm of 2
Math.LN10     // returns the natural logarithm of 10
Math.LOG2E    // returns base 2 logarithm of E
Math.LOG10E   // returns base 10 logarithm of E
Math.random() always returns a number lower than 1.
### random integers
Math.floor(Math.random() * 10);     // returns a random integer from 0 to 9
Math.floor(Math.random() * 11);      // returns a random integer from 0 to 10
Math.floor(Math.random() * 10) + 1 (minimum);  // returns a random integer from 1 to 10
function getRndInteger(min, max) {
  return Math.floor(Math.random() * (max - min) ) + min;
}
## boolean
Boolean(10 > 9)        // returns true
(10 > 9)              // also returns true
10 > 9                // also returns true
### comparisons and conditions
Everything With a "Value" is True
Everything Without a "Value" is False  The Boolean value of 0 (zero) is false:
The Boolean value of -0 (minus zero) is false:
The Boolean value of "" (empty string) is false:  + undefined + null + false + NaN
When using the === operator, equal booleans are not equal, because the === operator expects equality in both type and value.
var x = new Boolean(false);
var y = new Boolean(false);

// (x == y) is false because objects cannot be compared
x = 5
Comparing two JavaScript objects will always return false.
!=	not equal	x != 8	true
!==	not equal value or not equal type
&& || !
var voteable = (age < 18) ? "Too young":"Old enough";
isNaN(age)  // test if a number
## 50% random link generator
if (Math.random() < 0.5) {
  text = "<a href='https://w3schools.com'>Visit W3Schools</a>";
} else {
  text = "<a href='https://wwf.org'>Visit WWF</a>";
}
## switch and break and defaut
switch (new Date().getDay()) {
  case 6:
    text = "Today is Saturday";
    break;
  case 0:
    text = "Today is Sunday";
    break;
  default:
    text = "Looking forward to the Weekend";
}
Sometimes you will want different switch cases to use the same code.
  case 4:
  case 5:
    text = "Soon it is Weekend";
    break;
Switch cases use strict comparison (===).
## Different Kinds of Loops
for (i = 0; i < 5; i++) {
  text += "The number is " + i + "<br>";
}    ## run something for 5 times
And you can omit statement 1 (like when your values are set before the loop starts):
for (i = 0, len = cars.length, text = ""; i < len; i++) {
  text += cars[i] + "<br>";
}
If you omit statement 2, you must provide a break inside the loop. Otherwise the loop will never end. This will crash your browser. Read about breaks in a later chapter of this tutorial.
Statement 3 can do anything like negative increment (i--), positive increment (i = i + 15), or anything else.
### The JavaScript for/in statement loops through the properties of an object:
```javascript
var person = {fname:"John", lname:"Doe", age:25};

var text = "";
var x;
for (x in person) {
  text += person[x];
}
```
### while
while (condition) {
  // code block to be executed
}
do {
  text += "The number is " + i;
  i++;
}
while (i < 10);

for (;cars[i];) {
  text += cars[i] + "<br>";
  i++;
}   =  while
while (cars[i]) {
  text += cars[i] + "<br>";
  i++;
}

for (i = 0, len = cars.length, text = ""; i < len; i++) {
  text += cars[i] + "<br>";
}  // the first statement doesn't have to be i alone

for (i = 0; i < 10; i++) {
  if (i === 3) { break; }
  text += "The number is " + i + "<br>";
}

for (i = 0; i < 10; i++) {
  if (i === 3) { continue; }
  text += "The number is " + i + "<br>";
}  // continue the code without doing anything

## type conversion
### test type
Number() converts to a Number, String() converts to a String, Boolean() converts to a Boolean.

<img src="img/2019-04-23-16-29-23.png">
<img src="img/2019-04-23-16-29-56.png">
The data type of NaN is number
The data type of an array is object
The data type of a date is object
The data type of null is object
The data type of an undefined variable is undefined *
The data type of a variable that has not been assigned a value is also undefined *
The typeofoperator is not a variable. It is an operator. Operators ( + - * / ) do not have any data type.
"John".constructor                // Returns function String()  {[native code]}
(3.14).constructor                // Returns function Number()  {[native code]}
false.constructor                 // Returns function Boolean() {[native code]}
[1,2,3,4].constructor             // Returns function Array()   {[native code]}
{name:'John',age:34}.constructor  // Returns function Object()  {[native code]}
new Date().constructor            // Returns function Date()    {[native code]}
function () {}.constructor        // Returns function Function(){[native code]}
  return myArray.constructor.toString().indexOf("Array") > -1;
=   return myArray.constructor === Array;
  return myDate.constructor === Date;

The global method String() can convert numbers to strings.
The Number method toString() does the same.
<img src="img/2019-04-23-17-21-45.png">
String(false)      // returns "false"
String(true)       // returns "true"
false.toString()   // returns "false"
true.toString()    // returns "true"
The unary + operator can be used to convert a variable to a number:
If the variable cannot be converted, it will still become a number, but with the value NaN (Not a Number):
JavaScript automatically calls the variable's toString() function when you try to "output" an object or a variable:

## regular expression
A regular expression is a sequence of characters that forms a search pattern.

/pattern/modifiers;
var patt = /w3schools/i; //i  is a modifier (modifies the search to be case-insensitive).

he search() method uses an expression to search for a match, and returns the position of the match.

The replace() method returns a modified string where the pattern is replaced.

<img src="img/2019-04-23-17-26-57.png">
<img src="img/2019-04-23-17-27-28.png">
<img src="img/2019-04-23-17-27-45.png">
<img src="img/2019-04-23-17-30-11.png">
var patt = /e/;
patt.test("The best things in life are free!");  ==  //

```javascript
/e/.test("The best things in life are free!"); //return true
var obj = /e/.exec("The best things in life are free!");
document.getElementById("demo").innerHTML =
"Found " + obj[0] + " in position " + obj.index + " in the text: " + obj.input;
```
## errors and exceptions

When an error occurs, JavaScript will normally stop and generate an error message.

The technical term for this is: JavaScript will throw an exception (throw an error).

JavaScript will actually create an Error object with two properties: name and message.

```javascript
try {
  adddlert("Welcome guest!");
}
catch(err) {
  document.getElementById("demo").innerHTML = err.message;
}
```
Modern browsers will often use a combination of JavaScript and built-in HTML validation, using predefined validation rules defined in HTML attributes: JavaScript Errors - Throw and Try to Catch

Error Name Values
<img src="img/2019-04-23-17-40-24.png">
If you assign a value to a variable that has not been declared, it will automatically become a GLOBAL variable.
<img src="img/2019-04-23-17-41-09.png">
All modern browsers support running JavaScript in "Strict Mode".

In HTML, the global scope is the window object. All global variables belong to the window object.

<img src="img/2019-04-23-17-42-04.png">
In a web browser, global variables are deleted when you close the browser window (or tab), but remain available to new pages loaded into the same window (of a browser).

Hoisting is JavaScript's default behavior of moving all declarations to the top of the current scope (to the top of the current script or the current function).

JavaScript Declarations are Hoisted
In JavaScript, a variable can be declared after it has been used.

Variables and constants declared with let or const are not hoisted!

JavaScript only hoists declarations, not initializations.

<img src="img/2019-04-23-17-44-33.png">

Because of hoisting, y has been declared before it is used, but because initializations are not hoisted, the value of y is undefined.

## strict mode

"use strict"; Defines that JavaScript code should be executed in "strict mode".

With strict mode, you can not, for example, use undeclared variables.

All modern browsers support "use strict" except Internet Explorer 9 and lower:

"use strict";
x = 3.14;       // This will cause an error because x is not declared
### this

In an object method, this refers to the "owner" of the method.

When used alone, the owner is the Global object, so this refers to the Global object.

In a browser window the Global object is [object Window]:

 In strict mode, when used alone, this also refers to the Global object [object Window]:

In a JavaScript function, the owner of the function is the default binding for this.
So, in a function, this refers to the Global object [object Window].

JavaScript strict mode does not allow default binding.

So, when used in a function, in strict mode, this is undefined.

In HTML event handlers, this refers to the HTML element that received the event:

<img src="img/2019-04-23-17-49-45.png">

## ECMAScript ES2015 introduced two important new JavaScript keywords: let and const.

Variables declared with the var keyword can not have Block Scope.

Variables declared inside a block {} can be accessed from outside the block.

<img src="img/2019-04-23-17-51-11.png">

Variables declared Locally (inside a function) have Function Scope.
Before ES2015 JavaScript did not have Block Scope.

<img src="img/2019-04-23-17-51-53.png">
<img src="img/2019-04-23-17-52-04.png">
<img src="img/2019-04-23-17-53-11.png">
<img src="img/2019-04-23-17-53-33.png">
In the second example, using let, the variable declared in the loop does not redeclare the variable outside the loop.

With JavaScript, the global scope is the JavaScript environment.

In HTML, the global scope is the window object.
Global variables defined with the var keyword belong to the window object:
Global variables defined with the let keyword do not belong to the window object:

<img src="img/2019-04-23-17-55-00.png">
  <img src="img/2019-04-23-17-55-34.png">
<img src="img/2019-04-23-17-55-53.png">
Array and objects constant can be modifed but not redeclared or reassign: reference type

The const keyword is not supported in Internet Explorer 10 or earlier.

Redeclaring or reassigning an existing var or let variable to const, in the same scope, or in the same block, is not allowed:

<img src="img/2019-04-23-18-14-01.png">

The keyword const is a little misleading.


It does NOT define a constant value. It defines a constant reference to a value.

Because of this, we cannot change constant primitive values, but we can change the properties of constant objects.

## debugging

Programming code might contain syntax errors, or logical errors.

Searching for (and fixing) errors in programming code is called code debugging.

Debugging is not easy. But fortunately, all modern browsers have a built-in JavaScript debugger.

Built-in debuggers can be turned on and off, forcing errors to be reported to the user.

With a debugger, you can also set breakpoints (places where code execution can be stopped), and examine variables while the code is executing.

At each breakpoint, JavaScript will stop executing, and let you examine JavaScript values.

After examining values, you can resume the execution of code (typically with a play button).

var x = 15 * 5;
debugger;
document.getElementById("demo").innerHTML = x;  // if debugger is available

Debugging is the process of testing, finding, and reducing bugs (errors) in computer programs.
The first known computer bug was a real bug (an insect) stuck in the electronics.

## Best practice

Do not use tabs (tabulators) for indentation. Different editors interpret tabs differently.

For readability, avoid lines longer than 80 characters.

Hyphens can be mistaken as subtraction attempts. Hyphens are not allowed in JavaScript names.
Global variables written in UPPERCASE (We don't, but it's quite common)

Underscores:

Many programmers prefer to use underscores (date_of_birth), especially in SQL databases.

Underscores are often used in PHP documentation.

PascalCase:

PascalCase is often preferred by C programmers.

camelCase:

camelCase is used by JavaScript itself, by jQuery, and other JavaScript libraries.

Use Lower Case File Names

If you move from a case insensitive, to a case sensitive server, even small errors can break your web site.

To avoid these problems, always use lower case file names (if possible).

Avoid global variables, avoid new, avoid ==, avoid eval()

Strict mode does not allow undeclared variables.

Declarations on Top
It is a good coding practice to put all declarations at the top of each script or function.
(Provide a single place to look for local variables)
It is a good coding practice to initialize variables when you declare them.

Don't Use new Object()
var x1 = {};           // new object
var x2 = "";           // new primitive string
var x3 = 0;            // new primitive number
var x4 = false;        // new primitive boolean
var x5 = [];           // new array object
var x6 = /()/;         // new regexp object
var x7 = function(){}; // new function object

"Hello" - "Dolly"    // returns NaN does not generate an error but returns NaN (Not a Number):

Undefined values can break your code. It is a good habit to assign default values to arguments. Use Parameter Defaults

Avoid Using eval()

All numbers in JavaScript are stored as 64-bits Floating point numbers (Floats).

All programming languages, including JavaScript, have difficulties with precise floating point values:

var x = 0.1;
var y = 0.2;
var z = x + y            // the result in z will not be 0.3
var z = (x * 10 + y * 10) / 10;       // z will be 0.3

Never break a return statement.

If you use a named index, when accessing an array, JavaScript will redefine the array to a standard object.

Trailing commas in object and array definition are legal in ECMAScript 5.

WARNING !!
points = [40, 100, 1, 5, 25, 10,];

Internet Explorer 8 will crash.

JSON does not allow trailing commas.

if (typeof myObj === "undefined")  but not
if (myObj === null) don't
if (myObj !== null && typeof myObj !== "undefined")
use if (typeof myObj !== "undefined" && myObj !== null)
// take away
If you want to test if an object is not null, you must test if it not undefined first.

JavaScript does not create a new scope for each code block.

for (var i = 0; i < 10; i++) {
  // some code
}
return i;  // i = 10

## Bad performance / performance

Statements or assignments that can be placed outside the loop will make the loop run faster.

<img src="img/2019-04-23-19-45-01.png">
The bad code accesses the length property of an array each time the loop is iterated.

Accessing the HTML DOM is very slow, compared to other JavaScript statements.
If you expect to access a DOM element several times, access it once, and use it as a local variable:
<img src="img/2019-04-23-19-45-44.png">

Reduce DOM Size
Every attempt to search the DOM (like getElementsByTagName) will benefit from a smaller DOM.

Avoid Unnecessary Variables
<img src="img/2019-04-23-19-46-36.png">

The HTTP specification defines that browsers should not download more than two components in parallel.

While a script is downloading, the browser will not start any other downloads. In addition all parsing and rendering activity might be blocked.

defer="true"
<img src="img/2019-04-23-19-47-43.png">

Avoid using the with keyword. It has a negative effect on speed. It also clutters up JavaScript scopes.

The with keyword is not allowed in strict mode.

<img src="img/2019-04-23-19-48-41.png">
<img src="img/2019-04-23-19-49-06.png">
Internet Explorer does not support ECMAScript 2015.

Browser Support for ES7 (ECMAScript 2016)
Chrome	68	May 2018
Opera	47	Jul 2018
IE 9* was the first browser to support ECMAScript 5 (2011).  ECMASCript 5 =2009
var str = "       Hello World!        ";
alert(str.trim());  // remove from both sides
Array.isArray()
The JavaScript function JSON.parse() is used to convert the text into a JavaScript object:
var obj = JSON.parse('{"name":"John", "age":30, "city":"New York"}');
Use the JavaScript function JSON.stringify() to convert it into a string.
myJSON is now a string, and ready to be sent to a server:

JSON does not allow trailing commas

## ES 6

The find() method returns the value of the first array element that passes a test function.

The findIndex() method returns the index of the first array element that passes a test function.

epsilon = In mathematics, a small positive infinitesimal quantity, usually denoted epsilon or epsilon, whose limit is usually taken as epsilon->0.

Number.isSafeInteger(10);    // returns true
Number.isSafeInteger(12345678901234567890);  // returns false
<img src="img/2019-04-23-20-01-25.png">

isNaN("Hello");       // returns true

### Arrow functions

You don't need the function keyword, the return keyword, and the curly brackets.

// ES5
var x = function(x, y) {
   return x * y;
}

// ES6
const x = (x, y) => x * y;

Arrow functions do not have their own this. They are not well suited for defining object methods.

Arrow functions are not hoisted. They must be defined before they are used.

Using const is safer than using var, because a function expression is always constant value.

You can only omit the return keyword and the curly brackets if the function is a single statement. Because of this, it might be a good habit to always keep them:
You can only omit the return keyword and the curly brackets if the function is a single statement.
better practice: const x = (x, y) => { return x * y };

## JSON JavaScript Object Notation
JSON is language independent
JSON names require double quotes. JavaScript names do not.
So : "firstName":"John"

## JS forms
Automatic HTML form validation does not work in Internet Explorer 9 or earlier.

### JavaScript Validation API
  if (document.getElementById("id1").validity.rangeOverflow) {
    txt = "Value too large";
  }
The validity property of an input element contains a number of properties related to the validity of data:

checkValidity()

## Object
In JavaScript, objects are king. If you understand objects, you understand JavaScript.

Primitive values are immutable (they are hardcoded and therefore cannot be changed).
if x = 3.14, you can change the value of x. But you cannot change the value of 3.14.

Objects are variables too. But objects can contain many values.  A JavaScript object is a collection of named values

The named values, in JavaScript objects, are called properties.   "firstName"  property : "John" value

An object method is an object property containing a function definition.

JavaScript objects are containers for named values, called properties and methods.

JavaScript Objects are Mutable
Objects are mutable: They are addressed by reference, not by value.

var x = person;  // This will not create a copy of person.
The object x is not a copy of person. It is person. Both x and person are the same object.
Note: JavaScript variables are not mutable. Only JavaScript objects.

<img src="img/2019-04-23-20-17-24.png">
The JavaScript for...in statement loops through the properties of an object.

delete person.age;   // or delete person["age"];
The delete operator should not be used on predefined JavaScript object properties. It can crash your application.

In JavaScript, all attributes can be read, but only the value attribute can be changed (and only if the property is writable).

Property Attributes: The value is one of the property's attributes. Other attributes are: enumerable, configurable, and writable.

The delete keyword does not delete inherited properties, but if you delete a prototype property, it will affect all objects inherited from the prototype.

In a function definition, this refers to the "owner" of the function.

In the example above, this is the person object that "owns" the fullName function.

Built-In Methods:

var x = message.toUpperCase();
This example uses a lang property to get the value of the language property.
Getters and
  get lang() {
    return this.language;
  }
  document.getElementById("demo").innerHTML = person.lang;
This example uses a lang property to set the value of the language property.
  set lang(lang) {
    this.language = lang;
  }
 person.lang = "en";

get is better than function coz it allows to access x as a property instead of as a function
<img src="img/2019-04-23-20-29-05.png">
<img src="img/2019-04-23-20-29-12.png">

## JavaScript Object Constructors
function Person(first, last, age, eye) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eye;
}
It is considered good practice to name constructor functions with an upper-case first letter.

### Add a method
myFather.name = function () {
  return this.firstName + " " + this.lastName;
};
### Add property and methods to Constructor
You cannot add a new method or property to an object constructor the same way you add a new method to an existing object.

As you can see above, JavaScript has object versions of the primitive data types String, Number, and Boolean. But there is no reason to create complex objects. Primitive values are much faster.

Use object literals {} instead of new Object().

Use string literals "" instead of new String().

Use number literals 12345 instead of new Number().

Use boolean literals true / false instead of new Boolean().

Use array literals [] instead of new Array().

Use pattern literals /()/ instead of new RegExp().

Use function expressions () {} instead of new Function().

var x7 = function(){};  // new function object

## Javascript Object property

All JavaScript objects inherit properties and methods from a prototype.

Date objects inherit from Date.prototype
Array objects inherit from Array.prototype
Person objects inherit from Person.prototype

The Object.prototype is on the top of the prototype inheritance chain:

Date objects, Array objects, and Person objects inherit from Object.prototype.

The JavaScript prototype property allows you to add new properties to object constructors:

<img src="img/2019-04-23-20-43-00.png">
Only modify your own prototypes. Never modify the prototypes of standard JavaScript objects.

## Object methods

Object.defineProperty(person, "language", {value : "NO"}); (object, property, {value : value})
ES5 allows the following property meta data to be changed:

<img src="img/2019-04-23-20-45-03.png">

Object.defineProperty(person, "language", {writable:false});
Object.defineProperty(person, "language", {enumerable:false});
Listing All Properties
Object.getOwnPropertyNames(person);  // Returns an array of properties
Object.defineProperty(person, "language", {enumerable:false});
Object.keys(person);  // Returns an array of enumerable propertie
// An enumerable property is one that can be included in and visited during for..in loops (or a similar iteration of properties, like Object.keys()).
### add getter and setter
Object.defineProperty(person, "fullName", {
  get : function () {return this.firstName + " " + this.lastName;}
});
<img src="img/2019-04-23-20-48-25.png">

## Functions

A JavaScript function can also be defined using an expression.

A function expression can be stored in a variable:

The function above is actually an anonymous function (a function without a name).

Functions stored in variables do not need function names. They are always invoked (called) using the variable name.

var x = function (a, b) {return a * b};
function functionName(parameters) {

Hoisting is JavaScript's default behavior of moving declarations to the top of the current scope.

Because of this, JavaScript functions can be called before they are declared:

Function expressions will execute automatically if the expression is followed by ().
The function above is actually an anonymous self-invoking function (function without name).

<img src="img/2019-04-24-08-05-12.png">

But, JavaScript functions can best be described as objects.
The arguments.length property returns the number of arguments received when the function was invoked:

The toString() method returns the function as a string:
A function designed to create new objects, is called an object constructor.

function myFunction(a, b) {
  return arguments.length;
}

Arrow functions do not have their own this. They are not well suited for defining object methods.

JavaScript functions have a built-in object called the arguments object.

If a function is called with too many arguments (more than declared), these arguments can be reached using the arguments object.

The code inside a JavaScript function will execute when "something" invokes it.

myFunction() and window.myFunction() is the same function:
window.myFunction(10, 2);    // Will also return 20
Global variables, methods, or functions can easily create name conflicts and bugs in the global object.

When a function is called without an owner object, the value of this becomes the global object.

Invoking a function as a global function, causes the value of this to be the global object.
Using the window object as a variable can easily crash your program.

In JavaScript all functions are object methods.

If a function is not a method of a JavaScript object, it is a function of the global object (see previous chapter).

The call() method is a predefined JavaScript method.

It can be used to invoke (call) a method with an owner object as an argument (parameter).

var person = {
  fullName: function(city, country) {
    return this.firstName + " " + this.lastName + "," + city + "," + country;
  }
}
var person1 = {
  firstName:"John",
  lastName: "Doe"
}
person.fullName.call(person1, "Oslo", "Norway");

The call() method takes arguments separately.

The apply() method takes arguments as an array.

<img src="img/2019-04-24-08-15-20.png">

The apply() method is very handy if you want to use an array instead of an argument list.

Math.max.apply(null, [1,2,3]); // Will also return 3
The first argument (null) does not matter. It is not used in this example.
Math.max.apply(Math, [1,2,3]); // Will also return 3

In JavaScript strict mode, if the first argument of the apply() method is not an object, it becomes the owner (object) of the invoked function. In "non-strict" mode, it becomes the global object.

## JavaScript function Closures
Global variables can be made local (private) with closures.
Global and local variables with the same name are different variables. Modifying one, does not modify the other.

Variables created without the keyword var, are always global, even if they are created inside a function.
A closure is a function having access to the parent scope, even after the parent function has closed.
We also need to find a way to execute counter = 0 only once.
This is called a JavaScript closure. It makes it possible for a function to have "private" variables.

var add = (function () {
  var counter = 0;
  return function () {counter += 1; return counter}
})();

add();
add();
add();

// the counter is now 3  self-invoking function

## DOM

<img src="img/2019-04-24-08-23-25.png">
The DOM is a W3C (World Wide Web Consortium) standard.

* Core DOM - standard model for all document types
* XML DOM - standard model for XML documents
* HTML DOM - standard model for HTML documents
The HTML DOM is a standard object model and programming interface for HTML. It defines:

In the DOM, all HTML elements are defined as objects.

document.getElementById("demo").innerHTML = "Hello World!";
In the example above, getElementById is a method, while innerHTML is a property.

var x = document.getElementsByTagName("p");
var x = document.getElementById("main");
var y = x.getElementsByTagName("p");

var x = document.getElementsByClassName("intro");
// Finding elements by class name does not work in Internet Explorer 8 and earlier versions.

var x = document.querySelectorAll("p.intro"); // p element with class = "intro"
// The querySelectorAll() method does not work in Internet Explorer 8 and earlier versions.

This example finds the form element with id="frm1", in the forms collection, and displays all element values:
var x = document.forms["frm1"];
  for (i = 0; i < x.length ;i++) {
    text += x.elements[i].value + "<br>";
  }
document.getElementById("myImage").src = "landscape.jpg";
document.getElementById("p2").style.color = "blue";
<button type="button"
onclick="document.getElementById('id1').style.color = 'red'">
Click Me!</button>
<input type="button" value="Hide text" onclick="document.getElementById('p1').style.visibility='hidden'">

### animation
All animations should be relative to a container element.
<div id ="container">
  <div id ="animate">My animation will go here</div>
</div>

<h1 onclick="changeText(this)">Click on this text!</h1>

The onload and onunload events are triggered when the user enters or leaves the page.

The onload event can be used to check the visitor's browser type and browser version, and load the proper version of the web page based on the information.

function myFunction() {
  var x = document.getElementById("fname");
  x.value = x.value.toUpperCase();
}
</script>
</head>
<body>

Enter your name: <input type="text" id="fname" onchange="myFunction()">

<div onmouseover="mOver(this)" onmouseout="mOut(this)"

The onmousedown, onmouseup, and onclick events are all parts of a mouse-click. First when a mouse-button is clicked, the onmousedown event is triggered, then, when the mouse-button is released, the onmouseup event is triggered, finally, when the mouse-click is completed, the onclick event is triggered.

Change the background-color of an input field when it gets focus.

<h1 onmouseover="style.color='red'"
onmouseout="style.color='black'">
Mouse over this text</h1>

Note that you don't use the "on" prefix for the event; use "click" instead of "onclick".

  element.addEventListener("click", function(){ alert("Hello World!"); });
The addEventListener() method allows you to add many events to the same element, without overwriting existing events:

Example
element.addEventListener("click", myFunction);
element.addEventListener("click", mySecondFunction);

Add an Event Handler to the window Object
window.addEventListener("resize", function(){
  document.getElementById("demo").innerHTML = sometext;
});
### use anonymous function to proceed arguments
element.addEventListener("click", function(){ myFunction(p1, p2); });
### event bubbling and event capturing
If you have a <p> element inside a <div> element, and the user clicks on the <p> element, which element's "click" event should be handled first?

In bubbling the inner most element's event is handled first and then the outer: the <p> element's click event is handled first, then the <div> element's click event.
In capturing the outer most element's event is handled first and then the inner: the <div> element's click event will be handled first, then the <p> element's click event.

addEventListener(event, function, useCapture);

The default value is false, which will use the bubbling propagation, when the value is set to true, the event uses the capturing propagation.

element.removeEventListener("mousemove", myFunction);
Try it Yourself »

// in IE 8 and earlier versions. However, for these specific browser versions, you can use the attachEvent() method to attach an event handlers to the element, and the detachEvent() method to remove it

// cross brower solution
var x = document.getElementById("myBtn");
if (x.addEventListener) {     // For all major browsers, except IE 8 and earlier
  x.addEventListener("click", myFunction);
} else if (x.attachEvent) {   // For IE 8 and earlier versions
  x.attachEvent("onclick", myFunction);
}

## Dom navigation
<img src="img/2019-04-24-09-39-22.png">
New nodes can be created, and all nodes can be modified or deleted.

The terms parent, child, and sibling are used to describe the relationships.

<img src="img/2019-04-24-09-39-55.png">
<img src="img/2019-04-24-09-40-28.png">
A common error in DOM processing is to expect an element node to contain text.

<title id="demo">DOM Tutorial</title>  // here the title element doesn't contain text
It contains a text node with the value "DOM Tutorial".

var myTitle = document.getElementById("demo").firstChild.nodeValue;
var myTitle = document.getElementById("demo").childNodes[0].nodeValue;

<script>
alert(document.body.innerHTML);
</script>

alert(document.documentElement.innerHTML);// the full html
The nodeName property specifies the name of a node. = same as the tag name
The nodeType property is read only. It returns the type of a node. =

### Create nodes
var para = document.createElement("p");
var node = document.createTextNode("This is new.");
para.appendChild(node);

var element = document.getElementById("div1");
element.appendChild(para);

If you don't want that you can use the insertBefore() method:
element.insertBefore(para, child);
var child = document.getElementById("p1");
parent.removeChild(child);

// The node.remove() method does not work in any versions of the Internet Explorer browser.

It would be nice to be able to remove an element without referring to the parent.
But sorry. The DOM needs to know both the element you want to remove, and its parent
// common workaround
var child = document.getElementById("p1");
child.parentNode.removeChild(child);

To replace an element to the HTML DOM, use the replaceChild() method:

parent.replaceChild(para, child); // replace child with para, substitue

## JavaScript HTML DOM Collections

document.getElementById("demo").innerHTML = myCollection.length;

var x = document.getElementsByTagName("p");
However, you cannot use array methods like valueOf(), pop(), push(), or join() on an HTMLCollection.
An HTMLCollection is NOT an array!

## The HTML DOM NodeList Object
var myNodelist = document.querySelectorAll("p");
The forEach() method calls a provided function once for each element in an array, in order.
return exits the function so it works badly on forEach

HTMLCollection items can be accessed by their name, id, or index number. (tags etc)

NodeList items can only be accessed by their index number.

## The Browser Object Model (BOM) allows JavaScript to "talk to" the browser.

The window object is supported by all browsers. It represents the browser's window.

All global JavaScript objects, functions, and variables automatically become members of the window object.

window.document.getElementById("header");  =  document.getElementById("header");

All global JavaScript objects, functions, and variables automatically become members of the window object.

<img src="img/2019-04-24-09-57-17.png">

```javascript
<script>
var w = window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var h = window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;

var x = document.getElementById("demo");
x.innerHTML = "Browser inner window width: " + w + ", height: " + h + ".";
</script>
```

```javascript
window.open() - open a new window
window.close() - close the current window
window.moveTo() - move the current window
window.resizeTo() - resize the current window
```
### JavaScript Window Screen
The screen.width property returns the width of the visitor's screen in pixels.
document.getElementById("demo").innerHTML =
"Screen Width: " + screen.width;   // 1280*800 for this mac book pro

screen.availWidth; // minus interface feature like the Windows Taskbar
screen.availHeight; // 1280 * 777
screen.colorDepth;
The screen.colorDepth property returns the number of bits used to display one color.

All modern computers use 24 bit or 32 bit hardware for color resolution:

24 bits =      16,777,216 different "True Colors"
32 bits = 4,294,967,296 different "Deep Colors"
Older computers used 16 bits: 65,536 different "High Colors" resolution.

Very old computers, and old cell phones used 8 bits: 256 different "VGA colors".

The #rrggbb (rgb) values used in HTML represents "True Colors" (16,777,216 different colors)

screen.pixelDepth // For modern computers, Color Depth and Pixel Depth are equal.

window.location.href // url on the current page // https://www.w3schools.com/js/js_window_location.asp
Try it Yourself »
The window.location.hostname property returns the name of the internet host (of the current page). // www.w3schools.com
window.location.pathname
window.location.protocol
window.location.port  // If the port number is default (80 for http and 443 for https), most browsers will display 0 or nothing.
The window.location.assign() method loads a new document.

history.back() - same as clicking back in the browser
history.forward() - same as clicking forward in the browser
navigator.cookieEnabled;
navigator.appName;  // "Netscape" is the application name for both IE11, Chrome, Firefox, and Safari.
navigator.appCodeName // always mozilla
navigator.product // always Gecko
navigator.appVersion; // a lot of true information
The information from the navigator object can often be misleading, and should not be used to detect browser versions because:

Different browsers can use the same name
The navigator data can be changed by the browser owner
Some browsers misidentify themselves to bypass site tests
Browsers cannot report new operating systems, released later than the browser
navigator.language
navigator.onLine
The javaEnabled() method returns true if Java is enabled:
navigator.javaEnabled()

The window.confirm() method can be written without the window prefix.

A prompt box is often used if you want the user to input a value before entering a page.
window.prompt("sometext","defaultText");

if (person == null || person == "") {
  txt = "User cancelled the prompt.";
} else {
  txt = "Hello " + person + "! How are you today?";
}

alert("Hello\nHow are you?"); // linebreaks

The setTimeout() and setInterval() are both methods of the HTML DOM Window object.

<button onclick="setTimeout(myFunction, 3000)">Try it</button> // wait 3 seconds
The clearTimeout() method stops the execution of the function specified in setTimeout().

## Cookies
Cookies are data, stored in small text files, on your computer.

document.cookie = "username=John Doe";
With a path parameter, you can tell the browser what path the cookie belongs to. By default, the cookie belongs to the current page.
document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC; path=/";
document.cookie = "username=John Doe; expires=Thu, 18 Dec 2013 12:00:00 UTC";
var x = document.cookie;
Delete a Cookie with JavaScript //Just set the expires parameter to a passed date:
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

## AJAX
AJAX stands for Asynchronous JavaScript And XML. AJAX is a technique for accessing web servers from a web page.
AJAX is not a programming language.

AJAX just uses a combination of:

A browser built-in XMLHttpRequest object (to request data from a web server)
JavaScript and HTML DOM (to display or use the data)

AJAX is a misleading name. AJAX applications might use XML to transport data, but it is equally common to transport data as plain text or JSON text.

The keystone of AJAX is the XMLHttpRequest object.

The XMLHttpRequest object can be used to exchange data with a web server behind the scenes. This means that it is possible to update parts of a web page, without reloading the whole page.

var xhttp = new XMLHttpRequest();

For security reasons, modern browsers do not allow access across domains.
If you want to use the example above on one of your own web pages, the XML files you load must be located on your own server.
Old versions of Internet Explorer (5/6) use an ActiveX object instead of the XMLHttpRequest object:

if (window.XMLHttpRequest) {
   // code for modern browsers
   xmlhttp = new XMLHttpRequest();
 } else {
   // code for old IE browsers
   xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}

To send a request to a server, we use the open() and send() methods of the XMLHttpRequest object:

GET is simpler and faster than POST, and can be used in most cases.

However, always use POST requests when:

A cached file is not an option (update a file or database on the server).
Sending a large amount of data to the server (POST has no size limitations).
Sending user input (which can contain unknown characters), POST is more robust and secure than GET.

xhttp.open("GET", "demo_get.asp", true);
xhttp.open("GET", "demo_get.asp?t=" + Math.random(), true);

xhttp.open("GET", "demo_get2.asp?fname=Henry&lname=Ford", true);

xhttp.open("POST", "demo_post.asp", true);

xhttp.open("POST", "ajax_test.asp", true);
xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
xhttp.send("fname=Henry&lname=Ford");

xhttp.open("GET", "ajax_test.asp", true);
By sending asynchronously, the JavaScript does not have to wait for the server response, but can instead:

execute other scripts while waiting for server response
deal with the response after the response is ready

xhttp.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    document.getElementById("demo").innerHTML = this.responseText;
  }
};
xhttp.open("GET", "ajax_info.txt", true);
xhttp.send();

Sometimes async = false are used for quick testing. You will also find synchronous requests in older JavaScript code.

Since the code will wait for server completion, there is no need for an onreadystatechange function:

Example
xhttp.open("GET", "ajax_info.txt", false);
xhttp.send();
document.getElementById("demo").innerHTML = xhttp.responseText;

function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML =
      this.responseText;
    }
  };

A callback function is a function passed as a parameter to another function.

## parse xml to render as table
https://www.w3schools.com/js/js_ajax_applications.asp
https://www.w3schools.com/js/js_ajax_examples.asp

## Json

<h2>Convert a JavaScript object into a JSON string, and send it to the server.</h2>

<script>
var myObj = { name: "John", age: 31, city: "New York" };
var myJSON = JSON.stringify(myObj);
window.location = "demo_json.php?x=" + myJSON;

// Storing data:
myObj = {name: "John", age: 31, city: "New York"};
myJSON = JSON.stringify(myObj);
localStorage.setItem("testJSON", myJSON);

// Retrieving data:
text = localStorage.getItem("testJSON");
obj = JSON.parse(text);
document.getElementById("demo").innerHTML = obj.name;

Data is in name/value pairs

JSON names require double quotes. JavaScript names don't.

In JSON, string values must be written with double quotes:

JSON values cannot be one of the following data types:

a function
a date
undefined

null is possible

Or, you can use the second parameter, of the JSON.parse() function, called reviver.

You should avoid using functions in JSON, the functions will lose their scope, and you would have to use eval() to convert them back into functions.

You can loop through object properties by using the for-in loop:

In a for-in loop, use the bracket notation to access the property values:

## Json vs jQuery
element.parentNode.removeChild(element);  // remove an element
myElement.textContent = "Hello Sweden!";
var myParent = myElement.parentNode; // get parent node

## 












