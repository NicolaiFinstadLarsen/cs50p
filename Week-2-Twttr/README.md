---
title: "Just setting up my twttr - CS50's Introduction to Programming with Python"
source: https://cs50.harvard.edu/python/2022/psets/2/twttr/
date: 2025-01-19 12:11
tags: []
---


[source](https://cs50.harvard.edu/python/2022/psets/2/twttr/)

# Just setting up my twttr

> just setting up my twttr
>
> ' jack⚡️ (@jack) [March 21, 2006][1]

  [1]: https://twitter.com/jack/status/20?ref_src=twsrc%5Etfw

When texting or tweeting, it's not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called *twttr*. In a file called `twttr.py`, implement a program that prompts the user for a `str` of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

Hints

- Recall that a `str` comes with quite a few methods, per [docs.python.org/3/library/stdtypes.html#string-methods][2].
- Much like a `list`, a `str` is "iterable," which means you can iterate over each of its characters in a loop. For instance, if `s` is a `str`, you could print each of its characters, one at a time, with code like:


      for c in s:
          print(c, end="")


  [2]: https://docs.python.org/3/library/stdtypes.html#string-methods

## Demo

## Before You Begin

Log into [cs50.dev][3], click on your terminal window, and execute `cd` by itself. You should find that your terminal window's prompt resembles the below:

  [3]: https://cs50.dev/

    $

Next execute

    mkdir twttr

to make a folder called `twttr` in your codespace.

Then execute

    cd twttr

to change directories into that folder. You should now see your terminal prompt as `twttr/ $`. You can now execute

    code twttr.py

to make a file called `twttr.py` where you'll write your program.

## How to Test

Here's how to test your code manually:

- Run your program with `python twttr.py`. Type `Twitter` and press Enter. Your program should output:


      Twttr   


- Run your program with `python twttr.py`. Type `What's your name?` and press Enter. Your program should output:


      Wht's yr nm?


- Run your program with `python twttr.py`. Type `CS50` and press Enter. Your program should output


      CS50


You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

    check50 cs50/problems/2022/python/twttr

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2022/python/twttr
