Feature: Represent real currency

	Scenario Outline: Format currency value as text
		Given a currency item in <denomination>
		And value of <value>
		When the currency is stringified
		Then it matches <pattern>

		Examples: Positive values USD
			| denomination | value      | pattern        |
			| USD-cents    |  23        |  $0.23         |
			| USD-cents    |  100       |  $1.00         |
			| USD-cents    |  171       |  $1.71         |
			| USD-cents    |  1071      |  $10.71        |
			| USD-cents    |  10071     |  $100.71       |
			| USD-cents    |  110071    |  $1,100.71     |
			| USD-cents    |  500110071 |  $5,001,100.71 |

		Examples: Negative values USD
			| denomination | value      | pattern        |
			| USD-cents    | -500110071 | -$5,001,100.71 |
			| USD-cents    | -110071    | -$1,100.71     |
			| USD-cents    | -10071     | -$100.71       |
			| USD-cents    | -1071      | -$10.71        |
			| USD-cents    | -171       | -$1.71         |
			| USD-cents    | -100       | -$1.00         |
			| USD-cents    | -23        | -$0.23         |

	Scenario Outline: Parse text to currency
		Given currency text representation <repr>
		When currency text representation is parsed
		Then the resulting currency object has value <value>

		Examples: Positive values USD
			|    repr |    value |
			|   $1.00 |      100 |
			|    $1.0 |      100 |
			|     $1. |      100 |
			|      $1 |      100 |
			|     $.5 |       50 |
			|    $0.5 |       50 |
			|   $0.50 |       50 |
			|    $100 |    10000 |
			|   $1000 |   100000 |
			|  $1,000 |   100000 |

		Examples: Negative values USD
			|    repr  |    value  |
			|   -$1.00 |      -100 |
			|    -$1.0 |      -100 |
			|     -$1. |      -100 |
			|      -$1 |      -100 |
			|     -$.5 |       -50 |
			|    -$0.5 |       -50 |
			|   -$0.50 |       -50 |
			|    -$100 |    -10000 |
			|   -$1000 |   -100000 |
			|  -$1,000 |   -100000 |
