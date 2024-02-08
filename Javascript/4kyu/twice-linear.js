// Consider a sequence u where u is defined as follows:

//     The number u(0) = 1 is the first one in u.
//     For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
//     There are no other numbers in u.

// Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

// 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13, then 7 gives 15 and 22 and so on...
// Task:

// Given parameter n the function dbl_linear (or dblLinear...) returns the element u(n) of the ordered (with <) sequence u (so, there are no duplicates).
// Example:

// dbl_linear(10) should return 22

// Solution:

function dblLinear(n) {
    let u = [1]; // Initial sequence with u(0) = 1
    let yi = 0;  // Index for y = 2 * x + 1
    let zi = 0;  // Index for z = 3 * x + 1
    for (let i = 0; i < n; i++) {
        // Generate the next y and z values
        let y = 2 * u[yi] + 1;
        let z = 3 * u[zi] + 1;

        // Add the next value in the sequence (the smaller of y and z)
        // Also, if y and z are equal, increase both yi and zi to skip duplicates
        if (y < z) {
            u.push(y);
            yi++;
        } else if (y > z) {
            u.push(z);
            zi++;
        } else { // y == z, so add one and skip the next duplicate
            u.push(y);
            yi++;
            zi++;
        }
    }
    return u[n];
}