// Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

// Example
// createPhoneNumber([1, 2, 3, 4, 5, 6, 

// Solution:

function createPhoneNumber(numbers){
    return '(' + numbers.slice(0, 3).join('') + ') ' + numbers.slice(3, 6).join('') + '-' + numbers.slice(6).join('');
}
