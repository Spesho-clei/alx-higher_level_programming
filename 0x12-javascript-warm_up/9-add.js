#!/usr/bin/node

// Define the add function
function add(a, b) {
  return a + b;
}

// Get the first and second arguments
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Convert the arguments to integers
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

// Check if the conversion is successful
if (!isNaN(num1) && !isNaN(num2)) {
  // Call the add function and print the result
  console.log(add(num1, num2));
} else {
  console.log('Invalid input. Please provide two integers.');
}
