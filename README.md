# pirple_python
This gives the overview of python basics and has the assignment solution of python in pirple
## main.py
What's your favorite song?
Think of all the attributes that you could use to describe that song. That is: all of it's details or "meta-data". These are attributes like "Artist", "Year Released", "Genre", "Duration", etc. Think of as many different characteristics as you can.
In your text editor, create an empty file and name it main.py
Now, within that file, list all of the attributes of the song, one after another, by creating variables for each attribute, and giving each variable a value. Here's an example:
```
Genre = "Jazz"
```
Give each variable its own line. Then, after you have listed the variables, print each one of them out.
 For example:
```
Artist = "Dave Brubeck"
Genre = "Jazz"
DurationInSeconds = 328

print(Artist)
print(Genre)
print(DurationInSeconds)
```
Your actual assignment should be significantly longer than the example above. Think of as many characteristics of the song as you can. Try to use Strings,  Integers and Decimals (floats)!
## function_assignment.py
Let's return to the music example from assignment one. Pick 3 of the attributes you listed. For our example we're going to say "Genre", "Artist" and "Year". Create a new Python file and create 3 functions with the same name as those attributes. So in this example we'd have one function named "genre" another named "artist" and another called "year".
When someone calls any of those functions, that function should return the corresponding value for that attribute. For example, if we call the "Artist" function our function would return "Dave Brubeck". Yours should return whatever values make sense for your music choice.
## if_assignment.py
Create a function that accepts 3 parameters and checks for equality between any two of them
Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
## list_assignment.py
Create a global variable called myUniqueList. It should be an empty list to start.
Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should return False;
Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value of myUniqueList to show that it worked.
## basic_loop_assignment.py
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
