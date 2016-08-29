# Make a Random Hex Color using Math

*from [jlindsk and Randson Oliveira](http://www.paulirish.com/2009/random-hex-color-code-snippets/#comment-786938138)*

In JavaScript, it's easy to create a random hex color value using the power of math. Just get a random float value, convert it to a string hex value, slice a six segment long section from it, then convert that to upper case.

```javascript
var color = '#' + Math.random().toString(16).slice(2, 8).toUpperCase();
```
