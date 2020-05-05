# python-basics


scalar types
---

 - Built in types
   - int - arbitrary precision integer
   - float - 64-bit floating point numbers 
   - None - the null object
   - bool - True/False - boolean logical values
    

 - **int** - unlimited precision signed integer
    ````python
   >>> 10
   10
   >>> 0b10
   22
   >>> 0o10
   8
   >>> 0x10
   16
   >>> int(3.5)     // gives floor value
   3
   >>> int(-3.5)
   -3
   >>> int("496")
   496
   >>> int("10000",3)   // converts base 3, value 10000 to decimal.
   81
    ````
   
 - **float** - 15-16 digits in decimal
     ````python
   >>> 3.125
   3.125
   >>> 3e8
   300000000.0
   >>> 1.616e-35
   1.616e-35
   >>> float("1.618")
   1.618
   >>> float("nan")
   nan
   >>> float("inf") // +ve infinity
   inf
   >>> float("-inf")
   -inf
   >>> 3.0+1  // int promoted to float during addition.
   4.0
     ````
  - **None**
    - Null value
    - Often represents the absence of a value
    ````python
    >>> None
    >>>
    >>> a=None
    >>>
    >>> a is None
    True
    ````
   - **Bool**
     ````python
     >>> True
     True
     >>> False
     False
     >>> bool(0)
     False
     >>> bool(42)
     True
     >>> bool(-1)
     True
     >>> bool(0.0)   // value other than 0, return True
     False
     >>> bool(0.207)
     True
     >>> bool(-1.112)
     True
     >>> bool([])
     False
     >>> bool([1,2,4])   // list is not empty 
     True
     >>> bool("Spam")
     True
     >>> bool("False")
     True
     >>> bool("False")  // value is not null hence returns true
     True
     ```` 