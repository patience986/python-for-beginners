print("hello world")
print("concatenate" + "lion")
print("hello", "there")
print('he said "Hi"')
print(1 + 3)
print(1 - 3)
print(1 / 3)
print(1 * 3)
# variables
exVar = 100
print(exVar)

'''
# This section demonstrates a list and a for loop that iterates through its elements.
exampleList = [1, 6, 7, 3, 6, 9, 0]
for thing in exampleList:
    print(thing)

# This section shows another for loop using the range function to iterate through numbers 1 to 10.
# Inside the loop, it also demonstrates conditional statements (if, elif, else) comparing the values of x and y.
for x in range(1, 11):
    print(x)
    x = 2
    y = 2
    z = 10
    if x > y:
        print(x, "is greater than", y)
    if x < y:
        print(x, "is less than", y)
    if x == y:
        print(x, "is the same", y)

# This section is another example of conditional statements (if, elif, else) comparing x and y.
x = 13
y = 6
if x < y:
    print(x, "is less than", y)
if x > y:
    print(x, "is greater than", y)
else:
    print(x, "is not less than", y)

# This section demonstrates the use of if, elif (else if), and else conditional statements to check multiple conditions.
x = 3
y = 7
z = 10
if x > y:
    print(x, "is greater than", y)
elif x < z:
    print(x, "is less than", z)
else:
    print('nothing was the case')

# This section introduces a simple function definition (though it doesn't do anything as it only has a 'pass' statement).
# It also shows some basic arithmetic before the function definition.
x = 1
y = 3
print(x + y)


def example():
    x=1
    y=3
    print(x+y)
    if x<y:
       print(x,"is less than",y)
def main():
    example()
    '''

def addition (num1,num2):
    answer = num1 + num2
    return answer

# It looks like there might have been a slight indentation issue and an attempt to call the function inside its definition.
# Here's how you would typically call and use the 'addition' function:
result = addition(5, 6)
print(result)

# Or you could directly print the result:
print(addition(10, 2))