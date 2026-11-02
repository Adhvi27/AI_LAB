import random

def conflicts(state):
    count = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                count += 1

    return count

def display(state):
    n = len(state)
    for i in range(n):
        print(" ".join("Q" if state[j] == i else "." for j in range(n)))
    print()

n = int(input("Enter number of queens: "))

if n < 1:
    print("Invalid input")
else:
    total_moves = 0

    while True:
        state = [random.randint(0, n - 1) for _ in range(n)]
        current = conflicts(state)

        print("\nInitial State:")
        display(state)
        print("Initial Conflicts:", current)

        while current != 0:
            best_state = state
            best = current

            for col in range(n):
                for row in range(n):
                    if row != state[col]:
                        temp = state.copy()
                        temp[col] = row
                        c = conflicts(temp)

                        if c < best:
                            best = c
                            best_state = temp

            if best == current:
                break

            state = best_state
            current = best
            total_moves += 1

            print("Move:", total_moves)
            display(state)
            print("Conflicts:", current)

        if current == 0:
            print("Solution Found!")
            print("Final State:")
            display(state)
            print("Total Moves:", total_moves)
            break
