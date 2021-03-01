# Title
*SLee*, 03/01/2021

## Structured Error Handling (Try-Except)
When you are programming, you fix your bugs immediately and make sure the code runs smoothly. However, it often happens that other people introduce new bugs when they use your program.

## Raising Custom Erros
Python automatically generates errors based on conditions defined by the Python Runtime. However, you can also "raise" errors based on custom conditions.

```
#---------------------------------------------------------#
# Title: Listing 13
# Description: A try-catch with manually raised errors
# SLee, 03/01/2021, Created Script
#---------------------------------------------------------#

try:
    new_file_name = input("Enter the name of the file you want to make: ")
    if new_file_name.isnumeric():
      raise Exceiption('Do not use numbers for the file\'s name')
except Exceiption as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
```

## Summary
