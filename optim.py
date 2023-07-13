import numpy as np
import pandas as pd

rowsize = 31
colsize = 21

# Create the DataFrame
df = pd.DataFrame(np.ones((rowsize, colsize)))

# Add the 28th row which is the sum of each column
df.loc[rowsize, :] = df.sum()

minthresh = 1000
maxthresh = 1002
plusamt = 1
minusamt = 1
max_iter = 5000  
current_iter = 0
minval = 0

def adjust(df):
    for col in df.columns:
        if df.loc[rowsize, col] < minthresh:
            rand_index = np.random.randint(0, rowsize) 
            df.loc[rand_index, col] += plusamt
        elif df.loc[rowsize, col] > maxthresh:
            rand_index = np.random.randint(0, rowsize)
            while df.loc[rand_index, col] <= minval:  # prevents script from reducing a cell value below zero
                rand_index = np.random.randint(0, rowsize)  # Select a new random cell if the condition is not satisfied
            df.loc[rand_index, col] -= minusamt

    # Update the 28th row
    df.loc[rowsize, :] = df.loc[0:(rowsize-1), :].sum()  # calculate the sum over the first 27 rows only

# Iterate until all columns in the 27th row are within 21 and 23, or max iterations reached
while not df.loc[rowsize, :].between(minthresh, maxthresh).all() and current_iter < max_iter:
    adjust(df)
    print(f"Iteration: {current_iter}")
    print(df)
    current_iter += 1

# Print whether the loop stopped due to max_iter or because all conditions were satisfied.
if current_iter == max_iter:
    print("Reached maximum number of iterations")
else:
    print("All columns adjusted to be within target range.")
    print("total iterations:")
    print(current_iter)
