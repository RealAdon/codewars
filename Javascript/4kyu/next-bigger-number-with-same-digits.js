// Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

//   12 ==> 21
//  513 ==> 531
// 2017 ==> 2071

// If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift, None in Rust):

//   9 ==> -1
// 111 ==> -1
// 531 ==> -1

// Solution:

function nextBigger(n) {
    // Convert the number to an array of digits
    let digits = n.toString().split('');
    let i = digits.length - 2;
    
    // Find the first digit that is less than the digit next to it, moving from right to left
    while (i >= 0 && digits[i] >= digits[i + 1]) {
        i--;
    }
    
    // If no such digit is found, return -1
    if (i == -1) return -1;
    
    // Find the smallest digit on right side of (i'th digit) that is greater than digits[i]
    let j = digits.length - 1;
    while (digits[j] <= digits[i]) {
        j--;
    }
    
    // Swap digits[i] and digits[j]
    [digits[i], digits[j]] = [digits[j], digits[i]];
    
    // Reverse the digits after the position i
    let right = digits.splice(i + 1).reverse();
    let result = parseInt([...digits, ...right].join(''), 10);
    
    return result;
}