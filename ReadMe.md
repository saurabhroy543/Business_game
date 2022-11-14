This is a board game which requires a minimum two players. Player uses a random number between
1-12 and moves on the board accordingly. Each player has some amount at the start. Below image
represents a game board.


![Screenshot from 2022-11-14 19-51-58](https://user-images.githubusercontent.com/71812923/201683976-8041ec82-346d-4fd5-8451-46fe675ea4a4.png)

(Picture is for representation purposes only, it is not the actual input.)



Board will have a central Bank, which will have a initial money, e.g: Rs. 5000. Every player has to pay to
bank whenever they land on jail and similarly bank will pay to players if they land on lottery cell. The
board cell may be one of the following types.
➢ Jail: When the user lands on it, a defined amount, for e.g. Rs 150, will be deducted from user's
money and send to bank.
➢ Lottery: When the user lands on it, a defined amount, for e.g. Rs 200, will be added to user's
money and deducted from bank.
➢ Hotel: This is a special type of entity.
a. It has three types.
i. Silver -> Value = 200, Rent = 50
ii. Gold -> Value = 300, Rent = 150
iii. Platinum -> Value = 500, Rent = 300
b. When the user lands on it and has required money, he has to buy it by paying the bank

the required money to buy a silver hotel.
c. If the user lands on it’s pre-owned hotel and has required money, the user needs to
upgrade hotel by paying required delta value.
Silver to Gold -> 100
Gold to Platinum -> 200
d. If any other user lands on a pre-owned hotel, the user needs to pay rent as per hotel
state (Silver, Gold, Platinum) to hotel owner.

How To Play :
1. Two+ users will start from starting point with initial money.
2. Dice output will be according to the given input.
3. Every move has to follow cell type rules defined above.
4. Maximum ten chances will be awarded to each player.
5. After ten chances, player with maximum money, will be declared as the winner.
Inputs :
You can hard code below values in code, no need to parse them.
Initial money in bank : 5000
Initial money for each player : 1000
Hotels :
● Silver -> Value = 200, Rent = 50
● Gold -> Value = 300, Rent = 150
● Platinum -> Value = 500, Rent = 300
Jail Fine: 150 & Lottery Value: 200
J- Jail, H- Hotel, L- Lottery, E- Empty Cell
● Input set one:

Cells (10 cells only): "J,H,L,H,E,L,H,L,H,J"
Dice Output : "2,2,1, 4,4,2, 4,4,2, 2,2,1, 4,4,2, 4,4,2, 2,2,1"
Player : 3
Result :
Player-1 has total money 1100 and asset of amount : 500
Player-2 has total money 600 and asset of amount : 0
Player-3 has total money 1150 and asset of amount : 0
Balance at Bank : 5150

● Input set two:

Cells (10 cells only): "J,H,L,H,E,L,H,L,H,J"
Dice Output : "2,2,1, 4,2,3, 4,1,3, 2,2,7, 4,7,2, 4,4,2, 2,2,2"
Player : 3
Result :
Player-1 has total money 650 and asset of amount : 500
Player-2 has total money 750 and asset of amount : 300
Player-3 has total money 850 and asset of amount : 200
Balance at Bank : 5750
