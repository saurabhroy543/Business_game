from bank import Bank
from players import Player

players = [Player(), Player(), Player()]
bank = Bank()
cells = [JailCell(), HotelCell(), LotteryCell(), HotelCell(), EmptyCell(), LotteryCell(), HotelCell(), LotteryCell(),
         HotelCell(), JailCell()]
dice_outputs = [2, 2, 1, 4, 4, 2, 4, 4, 2, 2, 2, 1, 4, 4, 2, 4, 4, 2, 2, 2, 1]


def find_current_position(curr_player, move):
    if curr_player.get_total_step() >= len(cells):
        return curr_player.get_total_step() % len(cells)
    return curr_player.get_total_step()


def get_cell_at_player_position(pos):
    return cells[pos]


for d_output in range(0, len(dice_outputs)):
    current_player = players.pop()
    current_player.step(dice_outputs[d_output])
    players.insert(0, current_player)
    pos = find_current_position(current_player, dice_outputs[d_output])
    print(get_cell_at_player_position(pos))
