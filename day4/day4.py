from pathlib import Path

with Path(Path(__file__).parent, 'input4').open() as file:
    input = file.read().split("\n\n")

drawn_numbers = input[0].split(',')
board_data = [line.split('\n') for line in input[1:]]

class Board:
    def __init__(self, board):
        self.max_columns = 0
        self.max_rows = 0
        self.unmarked_score = 0
        self.board = self.get_board(board)
        self.marked = set()
        self.final_score = 0
        
    def get_board(self, board):
        board_dic = {};
        for y, row in enumerate(board):
            self.max_rows = max(y + 1, self.max_rows)
            for x, num in enumerate(row.split()):
                self.max_columns = max(x+1, self.max_columns)
                board_dic[num] = (x, y)
                self.unmarked_score += int(num)
        return board_dic

    def check_win(self, drawn_number):
        win_possible = True
        for x in range(self.max_columns):
            if((x, self.board.get(drawn_number)[1]) not in self.marked):
                win_possible = False
        if(win_possible):
            return True

        win_possible = True
        for y in range(self.max_rows):
            if((self.board.get(drawn_number)[0], y) not in self.marked):
                win_possible = False
        if(win_possible):
            return True
        else:
            return False

    def mark_board(self, drawn_number):
        if(self.board.get(drawn_number) and self.final_score == 0):
            self.marked.add(self.board.get(drawn_number))
            self.unmarked_score -= int(drawn_number)
            if(self.check_win(drawn_number)):
                self.final_score = self.unmarked_score * int(drawn_number)
                return self.final_score


b = Board(board_data[0])
boards : list[Board] = []
winning_boards : list[(Board, int)] = []

for data in board_data:
    b = Board(data)
    boards.append(b)


for draw in drawn_numbers:
    for game_board in boards:
        if(int(game_board.mark_board(draw) or 0) > 0):
            winning_boards.append((game_board, game_board.final_score))


print("Part 1: ", winning_boards[0][1])
print("Part 2: ", winning_boards[-1][1])



