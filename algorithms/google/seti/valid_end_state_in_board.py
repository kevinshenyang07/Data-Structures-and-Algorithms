# given an array as a 1-dimensional board
# '_' being empty, 'B' being a black piece, 'W' being a white piece
# black pieces can only move left, white pieces can only move right
# give a start state and an end state, determine the end state is valid
# naive approach:
# both states have a queue with each element being (color, index), compare head one by one
# improvement:
# pointer on each state
# follow up:
# if black and white pieces take turn to move by one step, how would the result changes?
# solution:
# if black pieces start first, moves of black - moves of white <= 1
def valid_state(start_state, end_state):
    if len(start_state) != len(end_state):
        return False

    n = len(start_state)
    i = j = 0
    piece_i = piece_j = ''

    while i < n and j < n:
        while i < n and start_state[i] == '_':
            i += 1
        piece_i = start_state[i] if i < n else ''

        while j < n and end_state[j] == '_':
            j += 1
        piece_j = end_state[j] if j < n else ''

        if piece_i != piece_j:
            return False
        if piece_i == 'B' and i < j:
            return False
        if piece_i == 'W' and i > j:
            return False

        i += 1
        j += 1

    return not (piece_i or piece_j)

def test():
    print valid_state('_W__B_', '___WB_') # True
    print valid_state('_W__B_', '__BW__') # False
    print valid_state('_W__B_', '_WB___') # True
    print valid_state('_W__B_', 'W_B___')  # False
    print valid_state('_W__B_', 'W_B__B')  # False
    print valid_state('_W___B', '_WB__W')  # False
    print valid_state('_W___B', '_W____')  # False

    print valid_state('_W_W_BB_', '___WWBB_') # True
    print valid_state('_W_W_BB_', '__W_W_BB') # False
    # and other corner cases

if __name__ == '__main__':
    test()
