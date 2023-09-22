from production import forward_chain, backward_chain
from rules import TOURIST_RULESET, Asian, British, Russian, Italian, American, Common

class Selector:
    def __init__(self):
        # Initialize the Selector class with necessary attributes
        self.var = "(?x)"
        self.drink_list = [Common.loves_tea, Common.loves_coffee, Common.loves_alcohol]
        self.food_list = [Common.loves_doner, Italian.loves_pasta,
                          American.loves_burgers, Asian.loves_noodles]
        self.conclusion_list = [Asian.conclusion, British.conclusion, Russian.conclusion,
                                Italian.conclusion, American.conclusion]
        self.selector = ""

    def selection_input(self, name):
        # Method to gather user preferences and perform forward chaining
        print(f"{name}, do you want to choose your preferences for drinks and food? (yes/no)\n")
        choice = input("Choose your answer: ").strip().lower()

        if choice == "no":
            self.simulate_answers(name)
            print(f"\nDo you wish to continue? \n")
        elif choice == "yes":
            # If user wants to choose preferences, prompt for drink and food choices
            print(f"{name}, pick from the list of your favorite drinks (ex: 1 2 3):\n")
            for index, drink in enumerate(self.drink_list, start=1):
                print(f"{index}: {drink.replace(self.var, name)}")

            drink_choice = input("\nChoose your favorite drink(s): ").strip().split()
            to_chain = [self.drink_list[int(index) - 1].replace(self.var, name) for index in drink_choice]

            print(f"\nNow, pick from the list of your favorite foods based on your drink choice (ex: 1 2 3):\n")
            for index, food in enumerate(self.food_list, start=1):
                print(f"{index}: {food.replace(self.var, name)}")

            food_choice = input("\nChoose your favorite food(s): ").strip().split()
            to_chain += [self.food_list[int(index) - 1].replace(self.var, name) for index in food_choice]

            # Perform forward chaining with user preferences
            forward = forward_chain(TOURIST_RULESET, to_chain)
            return self._suggestion(forward, name)

    def _suggestion(self, chained_data, name):
        # Method to suggest tourist group(s) based on forward chaining results
        suggestion_list = []
        for conclusion in self.conclusion_list:
            named_conclusion = conclusion.replace(self.var, name)
            if named_conclusion in chained_data:
                suggestion_list.append(named_conclusion)

        if len(suggestion_list) == 0:
            return f"{name} doesn't belong to any of the tourist groups. (write yes/no to proceed)"
        return f"Does {name} belong to the following tourist group(s): {', '.join(suggestion_list)}? (write yes/no to proceed)"

    def simulate_answers(self, name):
        # Method to simulate answers for demo purposes and perform forward chaining
        print(f"Simulating answers for {name}...\n")
        print(f"For DEMO purposes to show forward chain.\n")
        drink_choice = [1, 2]  
        food_choice = [2, 3] 

        to_chain = [self.drink_list[int(index) - 1].replace(self.var, name) for index in drink_choice]
        to_chain += [self.food_list[int(index) - 1].replace(self.var, name) for index in food_choice]
        
        forward = forward_chain(TOURIST_RULESET, to_chain)
        suggestion = self._suggestion(forward, name)
        # print(f"Forward chain: {forward}\n")
        print(f"Suggestion: {suggestion}")


if __name__ == '__main__':
    print("Welcome to the Expert System!\n")
    selector = Selector()

    while True:
        name = input("Please write your name: ")

        while True:
            chain_choice = input("Do you want to perform backward or forward chaining? (backward/forward): ").strip().lower()
            if chain_choice in ["backward", "forward"]:
                break
            else:
                print("Invalid input. Please choose 'backward' or 'forward'.")

        if chain_choice == "backward":
            # For backward chaining, provide a list of hypotheses to choose from
            print("You can choose from the following hypotheses:")
            for conclusion in selector.conclusion_list:
                named_conclusion = conclusion.replace(selector.var, name)
                print(named_conclusion)
            
            hypothesis_choice = input("Please enter the hypothesis you want to test: ").strip()
            backward = backward_chain(TOURIST_RULESET, hypothesis_choice)
            print(f"Backward chain: {backward}")
        elif chain_choice == "forward":
            # For forward chaining, use the selection_input method
            suggestion = selector.selection_input(name)
            print(suggestion)

        while True:
            suggestion_confirm = input("Write 'yes' or 'no': ").strip().lower()
            if suggestion_confirm in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please write 'yes' or 'no'.")

        if suggestion_confirm == "yes":
            print("We are glad to help you!")
        else:
            print("Better luck next time!")
