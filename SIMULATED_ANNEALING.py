
import random
import math

N = 8
def conflicts(board):
    count = 0

    for i in range(N):
        for j in range(i + 1, N):

            if board[i] == board[j]:
                count += 1

            elif abs(board[i] - board[j]) == abs(i - j):
                count += 1

    return count

def get_neighbor(board):
    new_board = board.copy()

    col = random.randint(0, N - 1)
    new_row = random.choice(
        [r for r in range(N) if r != new_board[col]]
    )

    new_board[col] = new_row

    return new_board


def simulated_annealing():

    while True:

        board = [random.randint(0, N - 1)
                 for _ in range(N)]

        temperature = 10
        cooling_rate = 0.995
        min_temperature = 0.001

        while temperature > min_temperature:

            current_conflicts = conflicts(board)

            if current_conflicts == 0:
                return board

            neighbor = get_neighbor(board)

            new_conflicts = conflicts(neighbor)

            delta = new_conflicts - current_conflicts

            if delta < 0:
                board = neighbor

            else:
                probability = math.exp(-delta / temperature)

                if random.random() < probability:
                    board = neighbor

            temperature *= cooling_rate



solution = simulated_annealing()

print("Solution:", solution)
print("Conflicts:", conflicts(solution))

for row in range(N):
    for col in range(N):
        if solution[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()
