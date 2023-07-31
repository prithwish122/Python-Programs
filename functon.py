"""x="awesome"

def myfunc():
    print("Python is "+x)


myfunc()    """

"""x="awesome"#global variable

def fun():
    x="fantastic"#local varible
    print("Python is "+x)
 
fun()
print("Python is "+x)"""


x="Execellent"
def myfun():
    global x#global variable
    x="fantastic" 
myfun()
print("Python is"+x)     
