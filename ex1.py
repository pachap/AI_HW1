import search
import math 

ids=["ID1", "ID2"] #Feel your IDs

class BombermanProblem(search.Problem):
    """This class implements a Bomberman problem"""
    def __init__(self, initial):
        """ Constructor only needs the initial state.
        Don't forget to set the goal or implement the goal test"""
        search.Problem.__init__(self, initial)
        # Add as needed
        
    def successor(self, state):
        """Given a state, return a sequence of (action, state) pairs reachable
        from this state. If there are many successors, consider an iterator
        that yields the successors one at a time, rather than building them
        all at once. Iterators will work fine within the framework."""
        return None
    
    def h(self, node):
        """ This is the heuristic. It get a node (not a state)
        and returns a goal distance estimate"""
        state = node.state
        return None

def create_bomberman_problem(game):
    print "<<create_bomberman_problem"
    """ Create a bomberman problem, based on the description.
    game - matrix as it was described in the pdf file"""
    print "PROBLEM: "
    for row in game:
        for c in row:
            print c,
        print
    return BombermanProblem(game)
