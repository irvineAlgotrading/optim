# optim

This script is for adjusting the values of a DataFrame such that the sum of each column falls within a specified range. If the sum of a column is outside of this range, the script makes random adjustments to values within that column until the sum is within the range. Here's a step-by-step explanation:

Setting up the DataFrame: The script starts by creating a DataFrame df of size rowsize x colsize, where rowsize = 31 creates 30 rows and colsize = 21 creates 20 columns. The DataFrame is initially filled with ones. It then adds an additional row (the 32nd row, indexed by rowsize), which contains the sum of each column.

Setting thresholds and iteration parameters: The script defines two threshold values minthresh = 1000 and maxthresh = 1005. The goal is to adjust the values in each column of the DataFrame so that the sum of each column is between these two thresholds. The plusamt and minusamt parameters specify by how much a value in the DataFrame will be increased or decreased. The script also sets a maximum number of iterations max_iter = 5000, a counter for the current iteration current_iter = 0, and a randperc value used to prevent the script from decreasing a value in the DataFrame below this percentage.

Defining the adjustment function: The adjust function iterates over each column in the DataFrame. If the sum of a column (stored in the last row) is less than minthresh, the function increases a random value in that column by plusamt. If the sum of a column is greater than maxthresh, the function decreases a random value in that column by minusamt, provided that the value is greater than randperc. After all columns have been adjusted, the function updates the last row with the new column sums.

Main loop: The script then enters a loop where it repeatedly calls the adjust function. It continues until either all column sums are within the range minthresh to maxthresh, or it reaches the maximum number of iterations. After each iteration, the script prints the current iteration number and the state of the DataFrame.

End of script: Finally, the script checks why it exited the loop. If it reached the maximum number of iterations, it prints a corresponding message. If all column sums were adjusted to be within the target range, it prints a success message and the total number of iterations.

This script could be used for example in simulations or optimization problems where you want the sum of values in each column to be within a certain range, and you want to reach this state by making random adjustments.
