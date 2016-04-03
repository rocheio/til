Use the Bitwise Right Shift Operator (`>>`) to Round Without Remainder
======================================================================

In JavaScript, you can use the [`>>`](https://msdn.microsoft.com/en-us/library/5s9e947e(v=vs.94).aspx) operator to shift the binary bits of an expression to the right. If the object is an integer or float value, then this shift can be used to quickly reduce it to a half, a quarter, an eighth, etc. and discard any remainder. 

This code is more performant than other options like the `Math` library, but is hard to read and might be too clever for its own good. If you decide to use it, make sure to include a comment describing it's purpose.

```javascript
var width = 215.3;
var half_width = width >> 1;  // Divide by 2 no remainder
var quarter_width = width >> 2;
alert('width is: ' + width +
			'; half_width is: ' + half_width +
			'; quarter_width is: ' + quarter_width);
```

[jsfiddle](https://jsfiddle.net/7LrwL07o/)
