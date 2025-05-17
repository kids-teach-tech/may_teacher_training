low = 1
high = 100


while low <= high:
    guess = (low + high) // 2  # Calculate the midpoint for the guess
    print("My guess is: " + str(guess))

    feedback = input("Type 'high' or 'low': ")

    if feedback == 'high':
        high = guess - 1 # Adjust the high boundary
    elif feedback == 'low':
        low = guess + 1  # Adjust the low boundary
    else:
        print("I guessed it!")
        break  # Exit the loop if the guess is correct
