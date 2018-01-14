class Player(self):

	def __init__(self, bankroll=100):
		self.bankroll=bankroll

	def add_bankroll(self, winnings):
		self.bankroll += winnings

	def sub_bankroll(self, bet_amount):
		self.bankroll -= bet_amount

	def make_bet(self, bet=5):
		print("Current Bankroll: $", self.bankroll)
		self.proposed_bet = input("Place your bet\n$5 Minimum")

		 
		if validate_bet(self.proposed_bet):
			self.bet = self.propposed_bet
		else:

