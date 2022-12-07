def solve(num):
   res = ""
   table = [
      (1000, "M"),
      (900, "CM"),
      (500, "D"),
      (400, "CD"),
      (100, "C"),
      (90, "XC"),
      (50, "L"),
      (40, "XL"),
      (10, "X"),
      (9, "IX"),
      (5, "V"),
      (4, "IV"),
      (1, "I"),
   ]
   for cap, roman in table:
      d, n = divmod(num, cap) 
      res += roman * d
      num = n

   return res

num = int(input("Enter a number:"))

print(solve(num))

