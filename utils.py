from abc import ABC, abstractmethod


class BuyAble(ABC):
    @abstractmethod
    def buy(self, player, bank):
        pass


class FineAble(ABC):
    @abstractmethod
    def withdraw(self, player, bank):
        pass


class EarnAble(ABC):
    @abstractmethod
    def deposit(self, player, bank):
        pass


class Rentable(ABC):
    def pay_rent(self, player, owner):
        pass


class Upgradable(ABC):
    @abstractmethod
    def upgrade(self, player, bank, cell):
        pass

    @abstractmethod
    def upgrade_cell(self, cell):
        pass


class NotBuyable(BuyAble):
    def buy(self, player, bank):
        return False


class SilverBuyableHotel(BuyAble):
    value = 200

    def buy(self, player, bank):
        if player.has_required_balance(self.value):
            player.withdraw(self.value)
            bank.deposit(self.value)
            player.add_to_asset(200)
            return True
        return False


class LotteryEarning(EarnAble):
    amount = 200

    def deposit(self, player, bank):
        player.deposit(self.amount)
        bank.withdraw(self.amount)
        return True


class NoEarning(EarnAble):
    def deposit(self, player, bank):
        return False


class JailPenalty(FineAble):
    penalty = 150

    def withdraw(self, player, bank):
        player.deductMoney(self.penalty)
        bank.addMoney(self.penalty)
        return True


class NoPenalty(FineAble):
    def withdraw(self, player, bank):
        return False


class GoldRentableHotel(Rentable):
    rent = 150

    def pay_rent(self, player, owner):
        player.withdraw(self.rent)
        owner.deposit(self.rent)
        return True


class NotRentable(Rentable):
    def pay_rent(self, player, owner):
        return False


class PlatinumRentableHotel(Rentable):
    rent = 300

    def pay_rent(self, player, owner):
        player.withdraw(self.rent)
        owner.deposit(self.rent)
        return True


class SilverRentableHotel(Rentable):
    rent = 50

    def pay_rent(self, player, owner):
        player.withdraw(self.rent)
        player.deposit(self.rent)


class PlatinumUpgradableHotel(Upgradable):
    def upgrade_cell(self, cell):
        return False

    def upgrade(self, player, bank, cell):
        return False


class GoldUpgradableHotel(Upgradable):
    upgradeCost = 200

    def upgrade_cell(self, cell):
        cell.setUpgradable(PlatinumUpgradableHotel())
        return True

    def upgrade(self, player, bank, cell):
        if cell.getOwner() == player:
            player.withdraw(self.upgradeCost)
            bank.diposit(self.upgradeCost)
            player.add_to_asset(100)
            return self.upgrade_cell(cell)
        return False


class SilverUpgradeHotel(Upgradable):
    upgradeCost = 100

    def upgrade_cell(self, cell):
        cell.setUpgradable(GoldUpgradableHotel())
        return True

    def upgrade(self, player, bank, cell):
        if cell.getOwner() == player:
            player.withdraw(self.upgradeCost)
            bank.diposit(self.upgradeCost)
            player.add_to_asset(100)
            return self.upgrade_cell(cell)
        return False
