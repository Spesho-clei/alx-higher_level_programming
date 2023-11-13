#!/usr/bin/node

// Get the first argument
const arg = process.argv[2];

// Convert the argument to an integer
const numOccurrences = parseInt(arg);

// Check if the conversion is successful
if (!isNaN(numOccurrences)) {
  // Loop to print "C is fun" x times
  for (let i = 0; i < numOccurrences; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
