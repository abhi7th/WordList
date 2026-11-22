import numpy as np

def num_letters(num_rows, num_columns):
    return 2 * num_rows + 2 * num_columns - 4

assert num_letters(3, 4) == 10  # 3 is num_rows, 4 is num_columns

assert num_letters(6, 7) == 22
assert num_letters(2, 2) == 4
assert num_letters(5, 5) == 16
assert num_letters(4, 3) == 10
print("Checking assertions.")

data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
rows, columns = data.shape
#collect all letters - fill in your code here 
words = []
words.extend(data[0, :])
words.extend(data[-1, ::-1])
words.extend(data[1:-1, -1])
words.extend(data[-2:0:-1, 0])
words = [str(w) for w in words]
print(words)

assert len(words) == num_letters(rows, columns)

