class FiniteAutomata:
    def __init__(self, input_file):
        self.input_file = input_file
        self.states = []
        self.initial_state = ''
        self.out_states = []
        self.alphabet = []
        self.transitions = []
        self.read_data()

    def read_data(self):
        with open(self.input_file, 'r') as file:
            data = file.read()

        self.states = self.extract_data(data, 'states')
        self.initial_state = self.extract_single_value(data, 'initial_state')
        self.out_states = self.extract_data(data, 'out_states')
        self.alphabet = self.extract_data(data, 'alphabet')
        self.transitions = self.extract_transitions(data, 'transitions')

    def extract_data(self, data, key):
        start_index = data.find(f'{key}={{') + len(f'{key}={{')
        end_index = data.find('}', start_index)
        return data[start_index:end_index].split(', ')

    def extract_single_value(self, data, key):
        start_index = data.find(f'{key}=') + len(f'{key}=')
        end_index = data.find('\n', start_index)
        return data[start_index:end_index].strip()

    def extract_transitions(self, data, key):
        start_index = data.find(f'{key}={{') + len(f'{key}={{')
        end_index = data.find('}', start_index)
        transitions_data = data[start_index:end_index]
        transitions = [tuple(t.strip()[1:-1].split(', ')) for t in transitions_data.split('; ')]
        return transitions

    def is_dfa(self):
        for state in self.states:
            for symbol in self.alphabet:
                transitions = [t for t in self.transitions if t[1] == state and t[2] == symbol]
                if len(transitions) > 1:
                    return False
        return True

    def is_match(self, sequence):
        return self.__check_string(sequence, self.initial_state)

    def __check_string(self, string, state):
        if not string:
            return state in self.out_states
        for character in string:
            if character not in self.alphabet:
                return False
            valid_transitions = [t for t in self.transitions if t[0] == state and t[2] == character]
            if not valid_transitions:
                return False
            for transition in valid_transitions:
                if self.__check_string(string[string.find(character) + 1:], transition[1]):
                    return True
            return False

    def menu(self):
        while True:
            print("1. Print states")
            print("2. Print initial state")
            print("3. Print out states")
            print("4. Print alphabet")
            print("5. Print transitions")
            print("6. Quit")
            print("7. Check if a sequence matches")
            print("8. Check if it's a DFA")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.print_states()
            elif choice == '2':
                self.print_initial_state()
            elif choice == '3':
                self.print_out_states()
            elif choice == '4':
                self.print_alphabet()
            elif choice == '5':
                self.print_transitions()
            elif choice == '6':
                print("Exiting menu.")
                break
            elif choice == '7':
                print(self.is_match(input("Enter a sequence to check: ")))
            elif choice == '8':
                print(self.is_dfa())
            else:
                print("Invalid choice. Please enter a valid option.")

    def print_states(self):
        print("States:", self.states, "\n")

    def print_initial_state(self):
        print("Initial State:", self.initial_state, "\n")

    def print_out_states(self):
        print("Out States:", self.out_states, "\n")

    def print_alphabet(self):
        print("Alphabet:", self.alphabet, "\n")

    def print_transitions(self):
        print("Transitions:", self.transitions, "\n")

automaton = FiniteAutomata("id.in.txt")
automaton.menu()