# Analysing a solar cell with Python - Part 3

## For more advanced Hive members.

* Can you abstract out the parameter extraction function and use it to analyse an entire folder of data files?

```python
import os

for directory, subdirectories, files in os.walk('directory'):
    for file in files:
        if file is appropriate .txt file:
            import data
            plot data
            extract parameters
```

* The file names are taken from the coordinates at which each cell is measure across a larger plate (x-y.txt). Can you make a 3D plot of the parameters as a function of position?
