from production import IF, AND, THEN, OR

# Define a class to represent different tourist types with their conditions and conclusions
class TouristType:
    def __init__(self, name, food_condition=None, drink_condition=None, other_condition=None, conclusion=None):
        self.name = name
        self.food_condition = food_condition
        self.drink_condition = drink_condition
        self.other_condition = other_condition
        self.conclusion = conclusion

# Define common conditions that are shared among multiple tourist types
class Common:
    loves_doner = "(?x) favorite food is doner"
    loves_alcohol = "(?x) favorite drink is alcohol"
    loves_coffee = "(?x) favorite drink is coffee"
    loves_tea = "(?x) favorite drink is tea"

# Define conditions and conclusions for the "Asian" tourist type
class Asian:
    loves_noodles = "(?x) favorite food is noodles"
    is_asian = "(?x) is from Asia"
    conclusion = "(?x) is an Asian tourist"

# Define conditions and conclusions for the "British" tourist type
class British:
    loves_tea = "(?x) favorite drink is tea"
    loves_doner = "(?x) favorite food is doner"
    is_english = "(?x) loves rainy weather"
    conclusion = "(?x) is a British tourist"

# Define conditions and conclusions for the "Russian" tourist type
class Russian:
    loves_doner = "(?x) favorite food is doner"
    loves_coffee = "(?x) favorite drink is coffee"
    is_tough = "(?x) is a tough guy"
    loves_alcohol = "(?x) favorite drink is alcohol"
    conclusion = "(?x) is a Russian tourist"

# Define conditions and conclusions for the "Italian" tourist type
class Italian:
    loves_coffee = "(?x) favorite drink is coffee"
    loves_pasta = "(?x) favorite food is pasta"
    mamma_mia = "(?x) loves to watch Mamma Mia"
    conclusion = "(?x) is an Italian tourist"

# Define conditions and conclusions for the "American" tourist type
class American:
    loves_burgers = "(?x) favorite food is burgers"
    loves_alcohol = "(?x) favorite drink is alcohol"
    needs_burgers = "(?x) really needs burgers"
    conclusion = "(?x) is an American tourist"

# Define instances of TouristType for each tourist type with their specific conditions and conclusions
asian = TouristType(
    name="Asian",
    food_condition=Asian.loves_noodles,
    drink_condition=Common.loves_tea,
    other_condition=Asian.is_asian,
    conclusion=Asian.conclusion
)

british = TouristType(
    name="British",
    food_condition=Common.loves_doner,
    drink_condition=Common.loves_tea,
    other_condition=British.is_english,
    conclusion=British.conclusion
)

russian = TouristType(
    name="Russian",
    food_condition=Common.loves_doner,
    drink_condition=Common.loves_coffee,
    other_condition=Russian.is_tough,
    conclusion=Russian.conclusion
)

italian = TouristType(
    name="Italian",
    food_condition=Italian.loves_pasta,
    drink_condition=Common.loves_coffee,
    other_condition=Italian.mamma_mia,
    conclusion=Italian.conclusion
)

american = TouristType(
    name="American",
    food_condition=American.loves_burgers,
    drink_condition=Common.loves_alcohol,
    other_condition=American.needs_burgers,
    conclusion=American.conclusion
)

# Define rules for each tourist type
asian_rules = (
    IF(asian.food_condition, THEN(asian.other_condition)),
    IF(AND(asian.other_condition, asian.drink_condition), THEN(asian.conclusion)),
)

british_rules = (
    IF(AND(Common.loves_tea, Common.loves_doner), THEN(british.other_condition)),
    IF(british.other_condition, THEN(british.conclusion)),
)

russian_rules = (
    IF(OR(Common.loves_coffee, Common.loves_alcohol), THEN(russian.other_condition)),
    IF(AND(russian.other_condition, Common.loves_doner), THEN(russian.conclusion)),
)

italian_rules = (
    IF(italian.food_condition, THEN(italian.other_condition)),
    IF(AND(italian.other_condition, Common.loves_coffee), THEN(italian.conclusion)),
)

american_rules = (
    IF(american.food_condition, THEN(american.other_condition)),
    IF(OR(american.other_condition, Common.loves_alcohol), THEN(american.conclusion)),
)

# Combine all the rules into a single rule set
TOURIST_RULESET = asian_rules + british_rules + russian_rules + italian_rules + american_rules

