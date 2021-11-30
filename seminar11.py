fout = open ('output.txt', 'w')
line1 = 'This is some text\n'
x = 52
fout.write(line1)
fout.write(str(x))

fout.close()

import os
current_working_directory = os.getcwd()  # we can call it like 'cmd'
print('my current directory', current_working_directory)
print(os.listdir(current_working_directory))

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print(path)
        else:
           walk(path)
walk('.')

try:
    fin = open('bad_file')
except:
   print('Something went wrong')

def binarySearchRecursive(sequence, x, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    print('mid', sequence[mid])

    if x == sequence[mid]:
        return mid
    elif x < sequence[mid]:
        return binarySearchRecursive(sequence, x, left, mid - 1)
    elif x > sequence[mid]:
        return binarySearchRecursive(sequence, x, mid + 1, right)


if __name__ == "__main__":
    sample = [1, 2, 5, 6, 8, 10, 50, 70, 75, 77, 78, 79, 80, 81, 82, 85]
    x = 77
    print('Index of number ', x, 'is equal to ', binarySearchRecursive(sample, x, 0, len(sample) - 1))
