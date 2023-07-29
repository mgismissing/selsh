# Selsh
This innovative programming language similar to Python makes programs a lot shorter and fast!
## How it works
I will do an example. Say you need to manually ```print``` 10 different strings, one per line, using Python. How would you do that?  
With a lot of methods actually. You could print them out one by one and use 10 lines of code, or you could pack these strings in a list and create a ```for i in list: print(i)``` and use 2-3 lines.  
But what if I told you that with Selsh you could do that using no more than 20 characters in one line?
Here's the code in Python:
``` python
for i in list[...]: print(i)
```
And here's the code in Selsh:
```
#i:list[...]^@i
```
Let's analyze the code, should we?
The hash ```#``` repeats code for every item found in a list.  
The ```i``` tells the hash that if an item is found it will set ```i``` to the current item.  
The colon ```:``` tells the hash that the list is present right after it.  
```list[...]``` is nothing more than a list with its content.  
The ```^``` is a separator between actions, like a newline. In this case it means "then do".  
The ```@``` symbol means output, in this case the default output is the console.  
Finally, ```i``` is the content argument of output.
