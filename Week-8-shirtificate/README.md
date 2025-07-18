---
title: "CS50 Shirtificate - CS50's Introduction to Programming with Python"
source: https://cs50.harvard.edu/python/2022/psets/8/shirtificate/
date: 2025-06-08 10:31
tags: []
description: >
  
---


[source](https://cs50.harvard.edu/python/2022/psets/8/shirtificate/)

# CS50 Shirtificate

[![][1]][2]

  [1]: https://cs50.harvard.edu/python/2022/psets/8/jharvard.png
  [2]: https://cs50.harvard.edu/python/2022/psets/8/jharvard.pdf

Suppose that you'd like to implement a CS50 "shirtificate," a PDF with an image of an [I took CS50][3] t-shirt, [shirtificate.png][4], customized with a user's own name.

  [3]: https://cs50.harvardshop.com/collections/print/products/i-took-cs50-unisex-t-shirt
  [4]: https://cs50.harvard.edu/python/2022/psets/8/shirtificate.png

In a file called `shirtificate.py`, implement a program that prompts the user for their name and outputs, using [fpdf2][5], a CS50 shirtificate in a file called `shirtificate.pdf` similar to [this one for John Harvard][6], with these specifications:

  [5]: https://pypi.org/project/fpdf2/
  [6]: https://cs50.harvard.edu/python/2022/psets/8/jharvard.pdf

- The [orientation][7] of the PDF should be Portrait.
- The [format][7] of the PDF should be A4, which is 210mm wide by 297mm tall.
- The top of the PDF should say "CS50 Shirtificate" as [text][8], centered horizontally.
- The shirt's [image][9] should be centered horizontally.
- The user's name should be on top of the shirt, in white [text][10].

  [7]: https://py-pdf.github.io/fpdf2/PageFormatAndOrientation.html
  [8]: https://py-pdf.github.io/fpdf2/Text.html
  [9]: https://py-pdf.github.io/fpdf2/Images.html
  [10]: https://py-pdf.github.io/fpdf2/TextStyling.html

All other details we leave to you. You're even welcome to add borders, colors, and [lines][11]. Your shirtificate needn't match John Harvard's precisely. And no need to wrap long names across multiple lines.

  [11]: https://py-pdf.github.io/fpdf2/Shapes.html#lines

Before writing any code, do read through fpdf2's [tutorial][12] to learn how to use it. Then skim fpdf2's [API][13] (application programming interface) to see all of its functions and parameters therefor.

  [12]: https://py-pdf.github.io/fpdf2/Tutorial.html
  [13]: https://py-pdf.github.io/fpdf2/fpdf/

No need to submit any PDFs with your code. But, if you would like, you're welcome (but not expected) to share a shirtificate with your name on it in any of [CS50's communities][14]!

  [14]: https://cs50.harvard.edu/python/communities

Hints

- Note that fpdf2 comes with a `class` called `FPDF`, which has quite a few methods, per [py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF][15]. You can install it with:

      pip install fpdf2

- Note that you can extend `FPDF` and instantiate your own subclass thereof in order to add a header to every page of a PDF, per

  py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image

  . Or you can add it as text yourself.

- Note that you can disable automatic page breaks, which might otherwise cause your PDF to overflow from one page to two, with `set_auto_page_break`, per [py-pdf.github.io/fpdf2/Margins.html][16].
- Note that a [cell][17]'s height can be negative, to move it upward.
- You can open `shirtificate.pdf`, once outputted, by clicking it in VS Code's file explorer.

  [15]: https://py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF
  [16]: https://py-pdf.github.io/fpdf2/Margins.html
  [17]: https://py-pdf.github.io/fpdf2/Text.html#cell

## Demo

## Before You Begin

Log into [cs50.dev][18], click on your terminal window, and execute `cd` by itself. You should find that your terminal window's prompt resembles the below:

  [18]: https://cs50.dev/

    $

Next execute

    mkdir shirtificate

to make a folder called `shirtificate` in your codespace.

Then execute

    cd shirtificate

to change directories into that folder. You should now see your terminal prompt as `shirtificate/ $`. Now execute

    wget https://cs50.harvard.edu/python/2022/psets/8/shirtificate/shirtificate.png

to get a copy of the `shirtificate.png` image for your certificate. Finally, execute

    code shirtificate.py

to make a file called `shirtificate.py` where you'll write your program.

## How to Test

Here's how to test your code manually:

- Run your program with `shirtificate.py`. Make sure your program prompts you for a name. Enter your own name and press Enter. Your program should create a file, `shirtificate.pdf`, containing the name you entered as input overlaid on a rendering of `shirtificate.png`.
- Try a few other names for good measure, too!

You can execute the below to check your code using `check50`, a program that CS50 will use to test your code when you submit. But be sure to test it yourself as well!

    check50 cs50/problems/2022/python/shirtificate

Green smilies mean your program has passed a test! Red frownies will indicate your program output something unexpected. Visit the URL that `check50` outputs to see the input `check50` handed to your program, what output it expected, and what output your program actually gave.

## How to Submit

In your terminal, execute the below to submit your work.

    submit50 cs50/problems/2022/python/shirtificate