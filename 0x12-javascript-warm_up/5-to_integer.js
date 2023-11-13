#!/usr/bin/node

// Get the first argument
const arg = process.argv[2];

// Convert the argument to an integer
const argAsInt = parseInt(arg);

// Check if the conversion is successful
if (!isNaN(argAsInt)) {
  console.log(`My number: ${argAsInt}`);
} else {
  console.log("Not a number");
}
