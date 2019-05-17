# CHAOTIC ATTRACTORS

> An attractor is a set of numerical values toward which a system tends to evolve, for a wide variety of starting conditions of the system. A strange attractor is an attractor that exhibits fractal properties [[Wikipedia](https://en.wikipedia.org/wiki/Attractor)].

##### To do:
* Convert to C++
* Write scripts for more attractors
* Fix double dialog window issue
* Write descriptions of each attractor for website
* Combine scripts into one plugin

| Attractor            | Complete  | Language |
|:--------------------:|:---------:|:--------:|
| 3-Layer              | No        | Python |
| Aizawa               | Yes       | Python |
| Chen                 | Yes       | Python |
| Chua I               | Yes       | Python |
| Chua II              | Yes       | Python |
| Cubic Map            | No        | Python |
| De Jong              | Yes       | Python |
| Duffing              | Yes       | Python |
| Henon                | Yes       | Python |
| Ikeda                | No        | Python |
| Kakadu               | No        | Python |
| Kaneko I             | No        | Python |
| Kaneko II            | No        | Python |
| Kaplan-Yorke         | No        | Python |
| Lorenz I-III         | Yes       | Python |
| Lotka-Volterra       | Yes       | Python |
| Lozi                 | No        | Python |
| Metz                 | No        | Python |
| Metzler              | No        | Python |
| Moore                | Yes       | Python |
| Multi-Chua I         | No        | Python |
| Multi-Chua II        | No        | Python |
| Pickover             | No        | Python |
| QHenon               | No        | Python |
| Quadratic Map        | No        | Python |
| Quartic Map          | No        | Python |
| Quintic Map          | No        | Python |
| Rabinovich-Fabrikant | Yes       | Python |
| Rikitake             | Yes       | Python |
| Roessler             | Yes       | Python |
| Strick               | No        | Python |

## Algorithms
---
Generally, for continuous attractor functions, the generator function will follow the format:
```py
def attractor( param1, paramn, x0, y0, z0, delta, N, xFactor, yFactor, zFactor):
    
    # create spline object
    spline = c4d.SplineObject(N, c4d.SPLINETYPE_LINEAR)
    spline.SetName(ObjectName)

    # set first point to initial coordinates
    x = x0
    y = y0
    z = z0

    for i in range(N):
        # calculate distance to move in each direction (x, y, z)
        dx = difference_x
        dy = difference_y
        dz = difference_z
        
        # add difference to last point with global scaling factor
        x = x + delta * dx
        y = y + delta * dy
        z = z + delta * dz
        
        # add calculated point to spline with individual-axis scaling factors
        spline.SetPoint(i, c4d.Vector(x*xFactor, y*yFactor, z*zFactor))
        
    return spline
```
### 1. Aizawa Attractor
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 100000 |
| a | 0.95 |
| b | 0.7 |
| c | 0.6 |
| d | 3.5 |
| e | 0.25 |
| f | 0.1 |
| delta | 0.01 |
| x0 | 0.1 |
| y0 | 0.0 |
| z0 | 0.0 |
| factor | 100 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dx = (z-b) * x - d * y
dy = (d * x) + (z-b) * y
dz = c + (a * z) - ((z * z * z)/3) - (x * x + y * y) * (1 + e * z) + (f * z * x * x * x)
```

### 2. Chen Attractor
NOTE: many modifications of this system exist. See Wikipedia's [Multiscroll Attractor](https://en.wikipedia.org/wiki/Multiscroll_attractor) page.
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 20000 |
| a | 35 |
| b | 8.0/3.0 |
| c | 28 |
| delta | 0.002 |
| x0 | -3.0 |
| y0 | 2.0 |
| z0 | 20.0 |
| factor | 5 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dy = (c - a) * x - x * z + c * y
dz = x * y - b * z
```

### 3. Chua Attractors
#### a) Chua I
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 20000 |
| a | 15.6 |
| b | 1.0 |
| c | 25.58 |
| d | -1.0 |
| e | 0.0 |
| delta | 0.01 |
| x0 | 1.0 |
| y0 | 1.0 |
| z0 | 1.0 |
| factor | 5 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
h = e * x + (d + e) * (abs(x+1) - abs(x-1))
dx = a * (y - x - h)
dy = b * (x - y + z)
dz = y * -c
```

Where h is described by the following function:
```py
def hFinderI(x):
    d = 0
    
    if c % 2 == 0: 
        d = PI
        
    if x >= 2 * a * c:
        h = ((b * PI) / (2 * a)) * (x - 2 * a * c)
    if x <= -2 * a * c:
        h = ((b * PI) / (2 * a)) * (x + 2 * a * c)
    if -2 * a * c < x < 2 * a * c:
        h = b * sin((x * PI) / (2 * a) + d)
    return h
```

#### b) Chua II
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 30000 |
| alpha | 10814 |
| beta | 14.0 |
| a | 1.3 |
| b | 0.11 |
| c | 2.0 |
| delta | 0.01 |
| x0 | 1.0 |
| y0 | 0.0 |
| z0 | 0.0 |
| xFactor | 10 |
| yFactor | 50 |
| zFactor | 10 |
| distance | 0.1 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dx = alpha * (y - h)
dy = x - y + z
dz = -beta * y
PP = sqrt((x - xa) * (x - xa) + (y - ya) * (y - ya) + (z - za) * (z - za))
```

Where h is described by the following function:
```py
def hFinderII(x):
    sum = 0
    for k in range(1, 7):
        sum += ((m[k-1] - m[k]) * (abs(x + c[k]) - abs(x-c[k])))
    h = m[5] * x + 0.5 * sum
    return h
```

### 4. DeJong Attractor
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 1000 |
| a | 0.95 |
| b | 0.7 |
| c | 0.6 |
| d | 3.5 |
| delta | 0.01 |
| x0 | 0.0 |
| y0 | 0.2 |
| factor | 100 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dx = math.sin(a * y) - math.cos(b * x)
dy = math.sin(c * x) - math.cos(d * y)
```

### 5. Duffing Attractor
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 25000 |
| a | 0.25 |
| b | 0.3 |
| c | 1.0 |
| delta | 0.01 |
| x0 | 0.0 |
| y0 | 0.2 |
| factor | 1000 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dx = y
dy = x - x * x * x - a * y + b * math.cos(w * t)
```

### 6. Henon Attractor
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 25000 |
| a | 0.25 |
| b | 0.3 |
| c | 1.0 |
| delta | 0.01 |
| x0 | 0.0 |
| y0 | 0.2 |
| factor | 1000 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```x = 1 + y - a * x * x
y = b * x
```

### 7. Ikeda Attractor
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 50000 |
| a | 1.0 |
| b | 0.9 |
| c | 0.4 |
| d | 6.0 |
| delta | 0.01 |
| x0 | 0.0 |
| y0 | 0.0 |
| z0 | 0.0 |
| factor | 1 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dx = a + b * (x * math.cos(z) - y * math.sin(z))
dy = b * (x * math.sin(z) + y * math.cos(z))
dz = c - d/(1 + x * x + y * y)
```

### 8. Lorenz Attractors
#### a) Lorenz I
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 10000 |
| a | 10.0 |
| b | 28.0 |
| c | 8.0/3.0 |
| delta | 0.01 |
| x0 | 1.0 |
| y0 | 1.0 |
| z0 | 1.0 |
| factor | 0.2 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dx = a * (y - x)
dy = x * (b - z)- y
dz = x * y - c * z
```

#### b) Lorenz II
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 2000 |
| a | 10.0 |
| b | 28.0 |
| c | 6.0 |
| delta | 0.01 |
| x0 | 1.0 |
| y0 | 1.0 |
| z0 | 1.0 |
| factor | 5 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
h = 3 * sqrt(x * x + y * y)
dx = (-(a + 1) * x + (a - b + z) * y)/3+ ((1 - a) * (x * x - y * y)+2 * (b + a - z) * x * y)/h
dy = ((b - a - z) * x - (a + 1) * y)/3 + (2 * (a - 1) * x * y + (b + a - z) * (x * x - y * y))/h
dz = (3 * x * x * y - y * y * y)/2 - c * z
```

#### c) Lorenz III
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 2000 |
| a | 10.0 |
| b | 28.0 |
| c | 6.0 |
| delta | 0.01 |
| x0 | 1.0 |
| y0 | 1.0 |
| z0 | 1.0 |
| factor | 5 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
h = 3 * sqrt(x * x + y * y)
dx = ( -a * x * x * x + (2 * a + b - z) * x * x * y + (a - 2) * x * y * y + (z - b) * y * y * y) / (2 * (x * x + y * y))
dy = ((b - z) * x * x * x + (a - 2) * x * x * y + (-2 * a - b + z) * x * y * y - a * y * y * y) / (2 * (x * x + y * y))
dz = (2 * x * x * x * y - 2 * x * y * y * y - c * z)
```

### 9. Lotka-Volterra Attractor
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 2000 |
| a | 2.9851 |
| b | 3.0 |
| c | 2.0 |
| delta | 0.01 |
| x0 | 1.0 |
| y0 | 1.0 |
| z0 | 1.0 |
| factor | 100 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
dx = x - x * y + c * x * x - a * z * x * x
dy = x * y - y
dz = a * z * x * x - b * z
```

### 10. Multi-Chua Attractors
#### a) Multi-Chua I
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 30000 |
| alpha | 10.82 |
| beta | 14.286 |
| a | 1.3 |
| b | 0.11 |
| c | 7.0 |
| d | 0.0 |
| delta | 0.01 |
| x0 | 1.0 |
| y0 | 1.0 |
| z0 | 0.0 |
| factorx | 10 |
| factory | 50 |
| factorz | 10 |
| width | 150 |
| maxFloat | 1000000 |
| maxInt | 100000000 |
#### Equations
```
h  = -b * sin(((pi * x)/(2 * a)) - d)
dx = alpha * (y - h)
dy = x - y + z
dz = -beta * y
```

### 11. Rabinovich-Fabrikant Attractor
#### Initial Parameters
| Param | Value |
| ------ | ----- |
| N | 100000 |
| a | 1.1 |
| b | 0.87 |
| delta | 0.001 |
| x0 | -1.05 |
| y0 | 0.9 |
| z0 | 1.01 |
| factor | 50 |
#### Equations
```
dx = y * (z - 1 + x * x) + b * x
dy = x * (3 * z + 1 - x * x) + b * y
dz = -2 * z * (a + x * y)
```

---

##### More Information
* [Jurgen Meier](http://www.3d-meier.de)
* [Paul Bourke](http://paulbourke.net)
* [Algosome](http://www.algosome.com)
* [Ben Tamari](http://www.bentamari.com)
* [MAXON Python SDK](https://developers.maxon.net/docs/Cinema4DPythonSDK/html/index.html)
* [MAXON C++ SDK](https://developers.maxon.net/docs/Cinema4DCPPSDK/html/index.html)