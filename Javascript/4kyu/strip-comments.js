// Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

// Example:

// Given an input string of:

// apples, pears # and bananas
// grapes
// bananas !apples

// The output expected would be:

// apples, pears
// grapes
// bananas

// The code would be called like so:

// var result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
// result should == "apples, pears\ngrapes\nbananas"

// Solution:

function solution(input, markers) {
    // Split the input into lines
    return input
      .split('\n')
      .map(line => {
        // For each line, check for each marker
        markers.forEach(marker => {
          // Find the index of the marker in the line
          const index = line.indexOf(marker);
          // If the marker is found, truncate the line up to that index
          if (index !== -1) {
            line = line.substring(0, index);
          }
        });
        // Trim the line to remove trailing whitespace
        return line.trimEnd();
      })
      // Join the processed lines back together
      .join('\n');
  }