from players import Player
from utils import Upgradable, Rentable, BuyAble, EarnAble, FineAble, SilverRentableHotel, SilverUpgradeHotel, NoPenalty, \
    NoEarning, NotBuyable, NotRentable, SilverBuyableHotel, JailPenalty, LotteryEarning
from abc import ABC


class Cell():
    penalizable = FineAble()
    earnable = EarnAble()
    buyable = BuyAble()
    rentable = Rentable()
    upgradable = Upgradable()
    owner = Player()

    def __init__(self):
        pass

    def penalize(self, player, bank):
        return self.penalizable.withdraw(player, bank)

    def earn(self, player, bank):
        return self.earnable.deposit(player, bank)

    def buy(self, player, bank):
        bought = False
        if self.owner is None:
            bought = self.buyable.buy(player, bank)
        if bought:
            self.setOwner(player)
            self.rentable = SilverRentableHotel()
            self.upgradable = SilverUpgradeHotel()
            return True
        return bought

    def payRent(self, player, bank):
        if self.owner is not None and not self.owner == player:
            return self.rentable.payRent(player, self.owner)
        return False

    def upgrade(self, player, bank, cell):
        return self.upgradable.upgrade(player, bank, cell)

    def setUpgradable(self, upgradable):
        self.upgradable = upgradable

    def setOwner(self, owner):
        self.owner = owner

    def getOwner(self):
        return self.owner


class NotUpgradable:
    pass


class EmptyCell(Cell):
    def __init__(self):
        super(EmptyCell, self).__init__()
        penalizable = NoPenalty()
        earnable = NoEarning()
        buyable = NotBuyable()
        rentable = NotRentable()
        upgradable = NotUpgradable()
        owner = None


class HotelCell(Cell):

    def __init__(self):
        super(HotelCell, self).__init__()
        penalizable = NoPenalty()
        earnable = NoEarning()
        buyable = SilverBuyableHotel()
        rentable = NotRentable()
        upgradable = NotUpgradable()
        owner = None


class JailCell(Cell):
    def __init__(self):
        super(JailCell, self).__init__()
        penalizable = JailPenalty()
        earnable = NoEarning()
        buyable = NotBuyable()
        rentable = NotRentable()
        upgradable = NotUpgradable()
        owner = None


class LotteryCell(Cell):
    def __init__(self):
        super(LotteryCell, self).__init__()
        penalizable = NoPenalty()
        earnable = LotteryEarning()
        buyable = NotBuyable()
        rentable = NotRentable()
        upgradable = NotUpgradable()
        owner = None
