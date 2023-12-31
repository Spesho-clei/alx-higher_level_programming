#!/usr/bin/node

// Get the first argument
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Check if the conversion is successful
if (!isNaN(size)) {
  // Loop to print the square
  for (let i = 0; i < size; i++) {
    let row = '';
    for (let j = 0; j < size; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
