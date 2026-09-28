def vacuum_cleaner(room_a, room_b, position):

    actions = []

    # Vacuum starts at A
    if position == "A":

        if room_a == "DIRTY":
            actions.append("SUCK")
            room_a = "CLEAN"

        if room_b == "DIRTY":
            actions.append("MOVE RIGHT")
            position = "B"

            actions.append("SUCK")
            room_b = "CLEAN"

    # Vacuum starts at B
    elif position == "B":

        if room_b == "DIRTY":
            actions.append("SUCK")
            room_b = "CLEAN"

        if room_a == "DIRTY":
            actions.append("MOVE LEFT")
            position = "A"

            actions.append("SUCK")
            room_a = "CLEAN"

    if len(actions) == 0:
        actions.append("No cleaning required")

    return room_a, room_b, actions


# -----------------------------------------
# USER INPUT
# -----------------------------------------

room_a = input("Enter Room A status (DIRTY/CLEAN): ").upper()
room_b = input("Enter Room B status (DIRTY/CLEAN): ").upper()
position = input("Enter vacuum position (A/B): ").upper()


# -----------------------------------------
# RUN VACUUM CLEANER
# -----------------------------------------

final_a, final_b, actions = vacuum_cleaner(
    room_a,
    room_b,
    position
)


# -----------------------------------------
# DISPLAY RESULT
# -----------------------------------------

print("\n==============================")
print("Initial State")
print("==============================")

print("Room A =", room_a)
print("Room B =", room_b)
print("Vacuum Position =", position)

print("\nActions:")
print(" -> ".join(actions))

print("\n==============================")
print("Final State")
print("==============================")

print("Room A =", final_a)
print("Room B =", final_b)
