from grammar import Grammar


if __name__ == '__main__':
    # Read grammar from a file
    grammar1 = Grammar("g2.txt")
    grammar2 = Grammar("g2.txt")
    grammar1.print_s()
    grammar1.print_terminals()
    grammar1.print_productions()
    grammar1.print_nonterminals()
    grammar1.print_productions_for_nonterminal("A")
    grammar1.check_cfg()