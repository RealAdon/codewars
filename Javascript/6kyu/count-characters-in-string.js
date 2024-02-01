// The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

// What if the string is empty? Then the result should be empty object literal, {}.

// Solution:

function count(string) {
  let counts = {}
  string.split('').forEach(function(char){
    if (char in counts){
      counts[char] = counts[char] + 1
    } else {
      counts[char] = 1
    }
  })
  return counts
}
