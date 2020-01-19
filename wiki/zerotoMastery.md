## html css

### class is actually like a methode, change sth. to sth

### div > p parent is a div */

### h2 + p p right after h2 */

### footer: clear both <kbd>padding</kbd> = inside the box  top right bottom left margin = outside  for the inside content = width and height rem = root em */

### critical rander path
css minifier https://cssminifier.com/ */

does this apply to button ?
![](img/2019-01-14-16-38-50.png)
Few years ago when box shadow not fully implemented (webkit = safari + chrome)
![](img/2019-01-14-16-44-54.png)
[css transform](https://robots.thoughtbot.com/transitions-and-transformsreresponsive design
[exercices](https://learn.freecodecamp.org/responsive-web-design/basic-css/)

### box shadow to be used in my website too

### grid great for two dimensions = spectro website

### Sometimes prebuilt css in browsers : normalizing css

## Ressources

https://daneden.github.io/animate.css/
media queries
https://css-tricks.com/snippets/css/media-queries-for-standard-devices/
noshit ui icons
react tilt
https://www.creative-tim.com/product/paper-kit-2
animate.css to animate things
tachyons
stripe
twilio
jsonplaceholder
royalty free icon 
https://leaverou.github.io/css3patterns/  nice background patterns
heroku/digital ocean/amazon web services/engine yard
dev ops
grid malven 
create tim for templates and functions bases on bootstrap4  paper kit


## Javascript
### Babel = language translator
nfn
anfn
Getelement by tag id class
New methods queryselector  queryselectorall
getAttribute
setAttribute
className // best
classList (not supported in IE and opera)
add
remove
toogle
innerHTML
parentelement children
### selecting takes memory, so the better is to cache (ae) to a variable
We don't want the whole website to rerender   (paint flashing)
### Destructuring
![](img/2019-01-15-16-48-55.png)
### Object properties
![](img/2019-01-15-16-49-46.png)
### Template strings (backticks)
![](img/2019-01-15-16-51-02.png)
### Default arguments so that the function wouln't fail
![](img/2019-01-15-16-52-24.png)

### arrow function if single return
![](img/2019-01-15-16-53-37.png)
### closure:child scope has access to parent scope
### Curring and compose
![](img/2019-01-15-17-06-45.png)
### Side effect (we don't know it happened, something we do that affected the outside world, change a variable in a function scope ...)
![](img/2019-01-15-17-08-34.png)
### functional purity (always return something deterministic determinism, it always does the same thing, same input = same return)
![](img/2019-01-15-17-10-17.png### )
### advanced array operations

![](img/2019-01-15-17-17-46.png)
### map on an array (no return undefined compared to previous operation coz here we have to return)
![](img/2019-01-15-17-22-52.png)
### filter can be useful to check contain something with ===
![](img/2019-01-15-17-37-16.png)
### reduce 34, all three are PURE functions returning always something
![](img/2019-01-15-17-40-11.png)
### call stack (stackoverflow) Javascript is a single-thread language that can be non-blocking
asynchronous
Javascript engine (V8 for chrome) should be in a run-time env integrated in browser (call stack + web api (ajax for asynchronous programming) + callback queue + event loop(check if there's something in the callback queue))
### from inline javascript to
1. inline issues : code reusability + pollution of global name space
2. script tag issues : lack of dependancy resolution (order matters)
3. 1+2 (each time a new page = copy paste)
4. IIFE (no pollution, order matters, still dependancy)
5. browsify (common js as follow), read through all the files = module bundler
what source file shows
<script src = "bundle.js"></script>
what developper sees :
![](img/2019-01-15-18-00-58.png)
6. a lot more .... finally ES6 import and export function + webpack 2 (used in React)
![](img/2019-01-15-18-03-15.png)
### NPM created using V8 engine initially built for node js or yarn (javascript share, )
node allows javascript to run outside of the browser
### Semver: Semantic Versioning
a.b.c (c = bug patch release; b = minor release ,features, c = major release )
npm install with package.json
## React
Only the children know the change not the parents ( one way data flow downstream)
React bot converts from the virtual dom to dom, the react becomes the painter
![](img/2019-01-16-14-31-42.png)
import syntax is possible with webpack
reactdom = react bot  react native = mobile
./ just remember it
if no js then js by Default
module standard is capitalized
Return needs a bracket
React html = virtual DOM