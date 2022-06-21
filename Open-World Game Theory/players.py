"""
1 -> cooperate/stay silent.
0 -> defect/betray.
"""


class Bank:
    def __init__(self, bank_balance) -> None:
        self.bank_balance = bank_balance


class Agent:
    name, prev_move, curr_move = None, None, None

    def __init__(self, balance) -> None:
        self.balance = balance

    # apply payoff matrix to balance of Agents and Bank after transaction
    def __payoff__(self, other) -> list:
        # return list of changes to balances

        if self.curr_move == 1 and other.curr_move == 1:
            return [1, 1, -2]

        elif self.curr_move == 0 and other.curr_move == 0:
            # self.balance += -2
            # other.balance += -2
            # bank_balance += 4
            return [-2, -2, 4]

        elif self.curr_move == 1 and other.curr_move == 0:
            # self.balance += -3
            # other.balance += 3
            # bank_balance += 0
            return [-3, 3, 0]

        elif self.curr_move == 0 and other.curr_move == 1:
            # self.balance += 3
            # other.balance += -3
            # bank_balance += 0
            return [3, -3, 0]

    def __transact__(self, other) -> None:
        # record previous move for next iteration before continuing transaction
        self.prev_move = self.curr_move
        other.prev_move = other.curr_move

        # if any Agent in transaction is TitForTat, check opposing Agent prev_move to determine curr_move
        if self is TitForTat and other.prev_move != None:
            self.curr_move = other.prev_move

        if other is TitForTat and self.prev_move != None:
            other.curr_move = self.prev_move

        change_balance = self.__payoff__(other)

        self.balance += change_balance[0]
        other.balance += change_balance[1]
        bank.bank_balance += change_balance[2]


class Defector(Agent):
    name = "Defector"
    prev_move, curr_move = 0, 0  # prev_move and curr_move will always be 0 for Defector


class Cooperator(Agent):
    name = "Cooperator"
    prev_move, curr_move = 1, 1  # prev_move and curr_move will always be 1 for Cooperator


class TitForTat(Agent):
    name = "TitforTat"

    # prev_move and curr_move for TitForTat is dynamic; changes during each transaction involving TitForTat
    prev_move = 0

    def opp_prev_move(self, other):
        return other.prev_move


def main():
    bank = Bank(10000)

    c1 = Cooperator(100)
    c2 = Cooperator(100)

    for i in range(10):
        c1.__transact__(c2)
        print("{} 1's balance: {}".format(c1.name, c1.balance))
        print("{} 2's balance: {}".format(c2.name, c2.balance))


if __name__ == "__main__":
    main()
