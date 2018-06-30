import _thread
import time

n = int(input("Enter a number : "))

def squre(n):
    if n > 0 :
        print("\nSqure = ",n**2)
        time.sleep(2)
        squre(n-1)

    
def cube(n):
    if n > 0 :
        print("\nCube = ",n**3)
        time.sleep(1)
        cube(n-1)

_thread.start_new_thread(squre,(n,))
_thread.start_new_thread(cube,(n,))

while True :
    pass
