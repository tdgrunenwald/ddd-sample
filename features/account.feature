Feature: Account

	Scenario: Calculate account balance
		Given an account
		When the following transactions are applied
			|  amount   |
			|  $1423.32 |
			| -$51.31   |
			| -$100.00  |
		Then the balance is $1272.01
