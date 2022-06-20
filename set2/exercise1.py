"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement.

TODO: Start a list of important programming vocabulary in your readme.md for 
this week. E.g. the word "calling" means something in a programming context, 
what does it mean?
"""
import platform

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"
# I think this will run each variable in sequence within the function
some_words = ["what", "does", "this", "line", "do", "?"] # defines a list of words


# Print outcome of variable "word"
for word in some_words: 
    print(word) # Loops print function for each word listed in variable "some_words"

# Prints outcome of variable "x"
for x in some_words:
    print(x) # ^^

# Prints outcome of variable "some_words"
print(some_words) # Prints words in one line without looping print function

# Creates a condition for script to decide what function to run next. In this case, if there are more thna 3 words, the script will run the print function
if len(some_words) > 3: # Correct!
    print("some_words contains more than 3 words")

# Defines the function "usefulFunction()"
def usefulFunction(): # Correct!
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # Prints outcome of function"platform.uname()"
    print(platform.uname()) #Correct - but in this case, system information

# Calls function and runs, in this case, no outcome

usefulFunction() # Calls function and runs it