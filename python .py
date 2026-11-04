def decoretor1(func):
    def inner_fun():
        print("hii1")
        func()
        print("bye1")
    return inner_fun

def decoretor2(func):
    def inner_fun():
        print("hii2")
        func()                      #decoretor exiction flow
        print("bye2")
    return inner_fun                #decoretor3(decoretor2(decoretor1(ok)))

def decoretor3(func):
    def inner_fun():
        print("hii3")
        func()
        print("bye3")
    return inner_fun 

@decoretor3
@decoretor2
@decoretor1 
def Ok():
    print("Rohit")
    

Ok()


tracebaack
NameError
number = 1 

since no numb variable is
defined it will give NameError.
print(numb)
Output:
Traceback (most recent call last):
  File "gfg.py", line 5, in 
    print(numb)  
NameError: name 'numb' is not defined

IndexError

Accessing the index out
of range will raise IndexError
print(mylist[10])
Output:
Traceback (most recent call last):
  File "gfg.py", line 5, in 
    print(mylist[10])
IndexError: list index out of range


KeyError
DICT ={ "a" :25, "b" :65 }
​
# A is not mapped in dict
# will raise KeyError
print(DICT["A"])
Output:
Traceback (most recent call last):
  File "gfg.py", line 5, in 
    print(DICT["A"])
KeyError: 'A'


TypeError
c = 'b'+3
print(c)
Output:
Traceback (most recent call last):
  File "gfg.py", line 1, in 
    c = 'b'+3
TypeError: must be str, not int


valueError
print(int('xyz'))
Traceback (most recent call last):
  File "gfg.py", line 1, in 
    print(int('xyz'))
ValueError: invalid literal for int() with base 10: 'xyz'


ImportError /ModuleNotFound
import module_does_not_exist
Traceback (most recent call last):
  File "gfg.py", line 1, in 
    import module_does_not_exist
ModuleNotFoundError: No module named 'module_does_not_exist'


Multithreading in Python allows multiple threads (smaller units of a process) to run concurrently,
enabling efficient multitasking. 
It is especially useful for I/O-bound tasks like file handling, network requests,or user interactions.


multiprocessing is a package that supports spawning processes using an API similar to the threading module.
The multiprocessing package offers both local and remote concurrency, 
effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. 
Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
It runs on both POSIX and Windows.



started learning git hub
This error means GitHub is not allowing you to push code because the GitHub account currently authenticated on your computer does not have permission to access the repositor