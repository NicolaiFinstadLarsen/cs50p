---
title: "Felipe's Taqueria - CS50's Introduction to Programming with Python"
source: https://cs50.harvard.edu/python/2022/psets/3/taqueria/
date: 2025-01-31 05:41
tags: []
---


[source](https://cs50.harvard.edu/python/2022/psets/3/taqueria/)

# Felipe's Taqueria

Note that, as of [2023-10-25T11:59:00+00:00][1], the prices of Felipe's have been updated!

  [1]: https://time.cs50.io/20231025T115900Z

![][2]

  [2]: https://cs50.harvard.edu/python/2022/psets/3/felipes-logo.png

One of the most popular places to eat in [Harvard Square][3] is [Felipe's Taqueria][4], which offers a [menu][5] of entrees, per the `dict` below, wherein the value of each key is a price in dollars:

  [3]: https://en.wikipedia.org/wiki/Harvard_Square
  [4]: https://www.felipesboston.com/
  [5]: https://www.felipesboston.com/menu

    {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

In a file called `taqueria.py`, implement a program that enables a user to place an order, prompting them for items, one per line, until the user inputs control-d (which is a common way of ending one's input to a program). After each inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign (`$`) and formatted to two decimal places. Treat the user's input case insensitively. Ignore any input that isn't an item. Assume that every item on the menu will be [titlecased][6].

  [6]: https://docs.python.org/3/library/stdtypes.html#str.title

Hints

- Note that you can detect when the user has inputted control-d by catching an [`EOFError`][7] with code like:


      try:
          item = input()
      except EOFError:
          ...


  You might want to print a new line so that the user's cursor (and subsequent prompt) doesn't remain on the same line as your program's own prompt.

- Inputting control-d does not require inputting Enter as well, and so the user's cursor (and subsequent prompt) might thus remain on the same line as your program's own prompt. You can move the user's cursor to a new line by printing `\n` yourself!
- Note that a `dict` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#mapping-types-dict][8], among them `get`, and supports operations like:


      d[key]


  and


      if key in d:
          ...


  wherein `d` is a `dict` and `key` is a `str`.

- Be sure to avoid or catch any [`KeyError`][9].

  [7]: https://docs.python.org/3/library/exceptions.html#EOFError
  [8]: https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
  [9]: https://docs.python.org/3/library/exceptions.html#KeyError

## Demo

## Before You Begin

Log into [cs50.dev][10], click on your terminal window, and execute `cd` by itself. You should find that your terminal window's prompt resembles the below:

  [10]: https://cs50.dev/

    $

Next execute

    mkdir taqueria

to make a folder called `taqueria` in your codespace.

Then execute

    cd taqueria

to change directories into that folder. You should now see your terminal prompt as `taqueria/ $`. You can now execute

    code taqueria.py

to make a file called `taqueria.py` where you'll write your program.

## How to Test

Here's how to test your code manually:

- Run your program with `python taqueria.py`. Type `Taco` and press Enter, then type `Taco` again and press Enter. Your program should output:


      Total: $6.00


  and continue prompting the user until they input control-d.

- Run your program with `python taqueria.py`. Type `Baja Taco` and press Enter, then type `Tortilla Salad` and press enter. Your program should output:


      Total: $12.25


  and continue prompting the user until they input control-d.

- Run your program with `python taqueria.py`. Type `Burger` and press Enter. Your program should reprompt the user.

Be sure to try other foods and vary the casing of your input. Your program should behave as expected, case-insensitively.

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

    check50 cs50/problems/2022/python/taqueria

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2022/python/taqueria
