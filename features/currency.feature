Feature: Represent real currency

	Scenario Outline: Format currency value as text
		Given a currency item in <denomination>
		And value of <value>
		When the currency is stringified
		Then it matches <pattern>

		Examples: USD
			| denomination | value      | pattern       |
			| USD-cents    | 23         | $0.23         |
			| USD-cents    | 100        | $1.00         |
			| USD-cents    | 171        | $1.71         |
			| USD-cents    | 1071       | $10.71        |
			| USD-cents    | 10071      | $100.71       |
			| USD-cents    | 110071     | $1,100.71     |
			| USD-cents    | 500110071  | $5,001,100.71 |
