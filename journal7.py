import sys

if len(sys.argv) < 2:
    print("Usage: python scores.py <score1> <score2> <score3> ...")
    sys.exit()

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)

print("Scores:", scores)
print("Sum:", total)
print("Average:", average)
