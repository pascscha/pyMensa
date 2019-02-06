# pyMensa
A python package for accessing mensa menus at ETH and UZH Zürich

# Installation
`pip3 install pySBB`

# Usage
This package lets you access mensa menus at ETH and UZH Zürich. This package will only let you access menus at lunch time.

## Get Meals
It is very simple to get meals for a mensa:
```
import pyMensa

meals = pyMensa.get_meals("Polymensa")

for meal in meals:
    print(meal)
    print()
```
Example Output:
```
LOCAL (STUD:10.50 STAFF:11.50 EXTERN:15.50)
	Dieses Menu servieren wir Ihnen gerne bald wieder!
	

STREET (STUD:9.90 STAFF:11.90 EXTERN:15.90)
	The New York Burger
	Schweizer Rindfleisch
	oder Vegi-Grillburger
	Sesam Maxi-Bun, Cheddar,
	Eisberg, Tomaten, Gurken, 
	BBQ Relish und Chips

GARDEN (STUD:6.20 STAFF:9.30 EXTERN:12.70)
	Vegan Day
	Seitan mit Blumenkohl,
	Kichererbsen und Harissa-Sauce

etc ...
```

## Get Mensa
You can also just query for a Mensa Object:
```
import pyMensa

unimensa = pyMensa.get_mensa("uni")

print(unimensa.name)
print(unimensa.aliases)

meals = unimensa.get_meals()
for meal in meals:
    print(meal)
    print()
```
Example Output:
```
UZH Zentrum
['zentrum', 'uni', 'uzh zentrum', 'uzhzentrum']
einfach gut (STUD:5.40 STAFF:7.00 EXTERN:10.50)
	 Rindshackfleisch-Pilzragout
	mit hausgemachten Spätzli und Weisskabis
	Fleisch:Rind, CH
	

natürlich vegi (STUD:5.40 STAFF:7.00 EXTERN:10.50)
	 Gefüllte Aubergine mit Sojagehacktem Tomatensauce und Bratkartoffeln Menüsalat oder Apfelmus
```

# Objects
This is a descripition of all objects used by this package.

## Meal
This object describes a generic meal.

### Parameters:
| Name          | Type       | Description                                  |
| --------------|:----------:|:-------------------------------------------- |
| label         | str        | The label/name of that meal                  |
| price_student | str        | The price for students                       |
| price_staff   | str        | The price for staff                          |
| price_extern  | str        | The price for other guests                   |
| description   | str array  | A list of descriptions, usually ingredients. |

### Functions:
| Name      | Return Type  | Description                                         |
| ----------|:------------:|:----------------------------------------------------|
| __str__   | str          | Returns the string representation of the meal       |

## Mensa
This object describes a generic mensa.

### Parameters:
| Name     | Type       | Description                       |
| ---------|:----------:|:--------------------------------- |
| name     | str        | The name of the mensa             |
| aliases  | str array  | A list of alternative names that can be entered when searching |

### Functions:
| Name      | Return Type  | Description                                         |
| ----------|:------------:|:----------------------------------------------------|
| get_meals | Meal array   | Returns list of available Meals                     |
| has_alias | bool         | Checks if the given alias corresponds to that mensa |

## ETH Mensa
This object inherits from the generic Mensa object and implements the `get_meals` function for the [ETH Gastro API](https://www.webservices.ethz.ch/gastro/v1/RVRI/Q1E1/meals/de/2019-02-07/lunch)
### Parameters:
| Name     | Type       | Description                                 |
| ---------|:----------:|:--------------------------------------------|
| api_name | str        | The name of the mensa in the ETH Gastro API |

### Functions:
| Name      | Return Type  | Description                                         |
| ----------|:------------:|:----------------------------------------------------|
| get_meals | Meal array   | Fetches meals using the [ETH Gastro API](https://www.webservices.ethz.ch/gastro/v1/RVRI/Q1E1/meals/de/2019-02-07/lunch) |                     |

## UNI Mensa
This object inherits from the generic Mensa object and implements the `get_meals` function for the [UZH Mensa Website](https://www.mensa.uzh.ch/de/menueplaene.html) which is unfortunately much slower that working with the proper API ETH provides us with, but we have no choice.
### Parameters:
| Name     | Type       | Description                                    |
| ---------|:----------:|:-----------------------------------------------|
| api_name | str        | The name of the mensa on the UZH Mensa Website |

### Functions:
| Name      | Return Type  | Description                                         |
| ----------|:------------:|:----------------------------------------------------|
| get_meals | Meal array   | Fetches meals from the [UZH Mensa Website](https://www.mensa.uzh.ch/de/menueplaene.html) |

## Available Mensas
Here is a list of all available Mensas and their corresponding aliases:

| Name | Aliases |
|------|:--------|
Mensa Polyterrasse | poly, polymensa, polyterrasse, mensa polyterrasse
Food&Lab | foodlab, food lab, food&lab
Causiusbar | clausius, clausiusbar, lausiusbar, lausius
Polysnack | polysnack, snack
Trailerburger | foodtrailer, trailer, trailerburger
Alumni quattro Lounge | alumni, alumnilounge, alumni lounge
Bellavista | bellavista, bella vista
Fusion Meal | fusion, fusionmeal, fusion meal
G-ESSbar | gess, gessbar, g-essbar, essbar
Tannenbar | tanne, tannenbar, tannen bar
Dozentenfoyer | dozentenfoyer, dozenten, foyer, dozenten foyer
Plattenstrasse | platte, plattestross, plattenstrasse, plattestrass
Rämi 59 | rämi, raemi, rämi59, raemi59, rämi 59, raemi 59, raemistrasse, rämistrasse, rämistross
UZH Mercato | mercato
UZH Zentrum | zentrum, uni, uzh zentrum, uzhzentrum
UZH Lichthof | lichthof, rondell
UZH Irchel | irchel, irchel mensa, irchelmensa
UZH Irchel Atrium | irchel atrium, atrium
UZH Binzmühle | binzmühle, binzmuehle
UZH Cityport | cityport
UZH Zahnmedizin | zahnmedizin, zzm
UZH Tierspital | tierspital
UZH Botanischer Garten | botanischergarten, botanischer garten, garten, botgarten
