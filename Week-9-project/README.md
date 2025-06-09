# Backtester
#### Video Demo:  <URL HERE>
#### Description:

# What is it?

Backtester is my final project for the cs50p course from Harvards online computer science course.
The backtester is a project I have been wanting to make since i started this course. 

The name really says it all, it's a backtester for a financial instrument. To see if a strategy has an edge in the marked, its normall to backtest it. 

## Why make a backester?

The reason I want to learn to code is data analysis. To do that I have understood that I need an understanding of Pandas and maybe NumPy. Since Pandas is build on NumPy I figuered using Pandas for the tabular data of a financial instrument would be a good start. 

I will also be able to learn some matplot to visually show the returns and what not. Therefor this type of project really check alot of the boxes I am looking to learn.

# The start of my project

I first want to learn some Pandas, so the first days was allocated to research and testing how to use the library. And also do some quick reasearch for simple tradingstrategies which I would be able to implement as code. I also need to find some data, preferably as a .csv file to use in my backtest.

In the end I ended up on one of the sinmplest strategies there is. A SMA crossover.

The reason: I'm not looking to make a profit, I just want to learn Pandas. 

## Starting to learn

I found a datafile I want to use. And I learned how to make a dataframe and print the head and a sample of the dataframe. I can see that there is no headers on the data so I want to make some.

I ended up using the name= argument in the .read method.    

## Calculating the SMA

SMA is short for simple moving average. And is really just the average price over a period choosen by the user. I want to use the close price of the dataframe to calculate my SMA's.

I would need two SMA's. One short and one long for this strategy. 

Calculating these I found the rolling method which is perfect for this usecase. 

## Entering and exiting the marked

I wanted to have a function for both enter long and exit long, as well for enter short and exit short. 
But even though I tried alot of different solutions, in the end the problem was to itterate over all rows in the dataframe. I found it best to have all positions in one function and to loop over with range(1, len(df)). That way I could use df.at[i, "column"] for all my positions tasks. 
This was the easies way to only enter price data in the dataframe at the exact row we entered or exited. 
The other solutions, even though I could split it into separate functions, wrote marked price on all rows for entries as long as i was in the marked. I was a mess. 

I also use the price of the open candle from first signal crossover, this I think makes the sens. But I need to think about that.

Next I need to calculate how much money the positions made or lost.

## Calculating PnL per trade

This was a little tricky since I wanted to option to both viualize the per trade PnL, total PnL, short PnL, long PnL and equity curve later. I knew I had to append it to a list of some sort.

The problems became evident when I appended my PnL for each loop no matter what I did in my code.

In the end I found out that the line:
    if short_entry and short_exit:
        xxx

was not the way to do it. 

I then implemented the currenct lines of:
    if long_entry is not None and long_exit is not None:

I now have access to all the PnL numbers I need. I think...

## Visualize

