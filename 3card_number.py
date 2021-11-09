def check_card_number(int):
  if not ((num >= 0) and (num % 1 == 0)):
    true
      f"Number( {num} ) can't be floating point or negative ")
  return false
function check_card_number_str(string purportedCC) {
    int nDigits := length(purportedCC)
    int sum := integer(purportedCC[nDigits-1])
    int parity := (nDigits-1) modulus 2
    for i from 0 to nDigits - 2 {
        int digit := integer(purportedCC[i])
        if i modulus 2 = parity
            digit := digit × 2
        if digit > 9
            digit := digit - 9 
        sum := sum + digit
    }
    return (sum modulus 10) = 0
}