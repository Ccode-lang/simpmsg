# simpmsg
A API for easily sending messages with sockets.
# Client example
```python
import simpmsg
import random
import time

internet = simpmsg.simpserve()
while True:
    try:
        n = random.randint(1,2)
        time.sleep(1)
        print(n)
        if n == 1:
            internet.sendmsg("hello", "0.0.0.0", 5000)
        if n == 2:
            internet.sendmsg("goodbye", "0.0.0.0", 5000)
    except:
        internet.sendmsg("end", "0.0.0.0", 5000)
        break

```
# Server example
```python3
import simpmsg

internet = simpmsg.simpserve()
internet.initserver("0.0.0.0", 5000)
print(internet.port)
while True:
    com = internet.getmsg()[1]
    if com == "hello":
        print("client said hello")
    if com == "end":
        print("client ended connection")
    else:
        print("client did not say hello")
    


```
