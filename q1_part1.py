#https://adventofcode.com/2024/day/1

lines = """3   4
4   3
2   5
1   3
3   9
3   3"""

def solve(lines):
   left = []
   right = []
   lines = lines.split("\n")
   for l in lines:
      left.append(l.split("   ")[0])
      right.append(l.split("   ")[1])
   left.sort()
   right.sort()
   res = []
   for i in range(len(left)):
      res.append(abs(int(left[i])-int(right[i])))
   return sum(res)

print(solve(lines))
