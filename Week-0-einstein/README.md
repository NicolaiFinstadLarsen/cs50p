title: "Einstein - CS50's Introduction to Programming with Python"
source: https://cs50.harvard.edu/python/2022/psets/0/einstein/
date: 2025-01-17 11:41
tags:


[source](https://cs50.harvard.edu/python/2022/psets/0/einstein/)

# Einstein

Even if you haven't studied physics (recently or ever!), you might have heard that \\E = mc\^2\\, wherein \\E\\ represents energy (measured in Joules), \\m\\ represents mass (measured in kilograms), and \\c\\ represents the speed of light (measured approximately as 300000000 meters per second), per [Albert Einstein][1] et al. Essentially, the formula means that mass and energy are equivalent.

  [1]: https://en.wikipedia.org/wiki/Albert_Einstein

In a file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

Hints

- Recall that `input` returns a `str`, per [docs.python.org/3/library/functions.html#input][2].
- Recall that `int` can convert a `str` to an `int`, per [docs.python.org/3/library/functions.html#int][3].
- Recall that Python comes with several built-in functions, per [docs.python.org/3/library/functions.html][4].

  [2]: https://docs.python.org/3/library/functions.html#input
  [3]: https://docs.python.org/3/library/functions.html#int
  [4]: https://docs.python.org/3/library/functions.html

## Demo

## Before You Begin

Log into [cs50.dev][5], click on your terminal window, and execute `cd` by itself. You should find that your terminal window's prompt resembles the below:

  [5]: https://cs50.dev/

    $

Next execute

    mkdir einstein

to make a folder called `einstein` in your codespace.

Then execute

    cd einstein

to change directories into that folder. You should now see your terminal prompt as `einstein/ $`. You can now execute

    code einstein.py

to make a file called `einstein.py` where you'll write your program.

## How to Test

Here's how to test your code manually:

- Run your program with `python einstein.py`. Type `1` and press Enter. Your program should output:


        90000000000000000


- Run your program with `python einstein.py`. Type `14` and press Enter. Your program should output:


        1260000000000000000


- Run your program with `python einstein.py`. Type `50` and press Enter. Your program should output


        4500000000000000000


You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

    check50 cs50/problems/2022/python/einstein

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2022/python/einstein
