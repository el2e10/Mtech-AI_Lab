"" "The problem of cannibals and missionaries" ""


class Configuration:
    def __init__(self, list):
        self.lista = list

    def __repr__(self):
        return f"{self.lista}"

    def __eq__(self, other):
        return self.lista == other.lista

    def heuristic(self):
        # (Cannibali_est + Misionari_est) / locrui_in_barca
        return (self.lista [1] [0] + self.lista [1] [1]) / M


class Node:
    def __init__ (self, config):
        self.info = config
        self.h =  config.heuristic()

    def __str__ (self):
        return f"({}, h = {})". format (self.info, self.h)

    def __repr__ (self):
        return f"({self.info}, h = {self.h})"


class Problem:
    def __init__(self):
        self.nodes = [Node (initial_configuration)]
        self.nod_start = Node (initial_configuration)
        self.node_scope = Node (configuration_scope)

    def search_name_name (self, info):
        "" "Knowing only the" info "information of a node,
        you must return either the Node object that has that information,
        or None, if there is no node with that information. "" "
        # TO DO ... DONE
        for nod in self.noduri:
            if nod.info == info:
                return nod
        return None


"" "End of problem" ""


"" "Classes used in the A *" "" algorithm


class NodeBrowse:
    "" "A class that contains information associated with a node in open / closed lists
            Includes a reference to the node itself (from the graph)
            but it also has properties specific to the A * algorithm (f and g).
            It is assumed that h is the property of the node in the graph
    "" "

    problem = None # class attribute

    def __init __ (self, nod_graf, parent = None, g = 0, f = None):
        self.nod_graf = nod_graf # object of type Node
        self.parent = parent # object of type Node
        self.g = g # the cost of the road from the root to the current node
        if f is None:
            self.f = self.g + self.nod_graf.h
        else:
            self.f = f

    def drum_arbore (self):
        "" "
                Function that calculates the path associated with a node in the search tree.
                The function goes from parent to parent until it reaches the root
        "" "
        nod_c = self
        drum = [nod_c]
        while nod_c.parinte is not None:
            drum = [node_c.parent] + drum
            nod_c = nod_c.parent
        return road

    def contains_in_drum (self, nod):
        "" "
                Function that checks if the "node" is in the path between the root and the current node (self).
                The verification is done going from parent to parent to the root
                Compare only node information (info property)
                Return True or False.
                "node" is an object of type Node (has the attribute "nod.info")
                "self" is an object of type SearchNode (has "self.nod_graf.info")
        "" "
        # TO DO ... DONE
        nod_c = self
        while nod_c.parinte is not None:
            if nod.info == nod_c.nod_graf.info:
                return True
            nod_c = nod_c.parent
        return False

    # changes depending on the problem

    def expands (self):
        "" "For the current parent node, you must find all successors (sons)
        and return a list of tuples (son_node, son_muchie_cost_cost),
        or the empty list, if none exist.
        (Each tuple contains a Node object and a number.)
        "" "
        succ = []
        mal = self.nod_graf.info.lista [2]
        info = self.nod_graf.info.lista
        for m in range (min (info [mal] [0], M) + 1):

            if m == 0:
                c_max = M
            else:
                c_max = min (M - m, m, info [mal] [1])
            for c in range (c_max + 1):
                if m + c == 0:
                    continuity
                successor = [[], [], 1 - mal]
                successor [mal] = [info [mal] [0] - m, info [mal] [1] - c]
                successor [1 - mal] = [info [1 - mal]
                                     [0] + m, info [1 - mal] [1] + c]
                if (successor [0] [0]> = successor [0] [1]> = 0 or successor [0] [0] == 0) and (successor [1] [0]> = successor [1] [1 ]> = 0 or successor [1] [0] == 0):
                    configuration = Configuration (successor)
                    succ.append ((Node (configuration), 1))
        return succ

    def test_scop (self):
        return self.nod_graf.info == self.problema.nod_scop.info

    def __str __ (self):
        parinte = self.parinte if self.parinte is None else self.parinte.nod_graf.info
        return f "({self.nod_graf}, parent = {parent}, f = {self.f}, g = {self.g})"


"" "Algorithm A *" ""


def str_info_nodes (l):
    "" "
            a function used strictly in displays - can be modified depending on the problem
    "" "
    sir = "["
    for x in l:
        sir + = str (x) + "\ n"
    sir + = "] \ n"
    return sir


def cost_successors_low (l):
    "" "
            a function used strictly in displays - can be modified depending on the problem
    "" "
    sir = ""
    for (x, cost) in l:
        sir + = "\ nnod:" + str (x) + ", cost arc:" + str (cost)
    return sir


def_list (l, node):
    "" "
            list "l" contains objects of type NodePrush
            "node" is of type Node
    "" "
    for i in range (len (l)):
        if l [i] .nod_graf.info == nod.info:
            return l [i]
    return None


def a_star ():
    "" "
        The function that implements the A-star algorithm
    "" "

    nod_curent = None

    rad_arbore = NodParcurgere (NodParcurgere.problema.nod_start)
    open = [rad_tree] # open will contain elements of type NodePetrugere
    closed = [] # closed will contain elements of type NodePetrurgere

    while len (open)> 0:
        print (str_info_noduri (open)) # display open list
        nod_curent = open.pop (0) # remove the first item from the open list
        closed.append (current_node) # and add it to the end of the closed list

        # test if the node extracted from the open list is a purpose node (and if so, I exit the while loop)
        if nod_curent.test_scop ():
            break

        l_successors = current_node.expand () # contains tuples of type (Node, number)
        for (nod_succesor, cost_succesor) in l_succesori:
            # "current_node" is the father, "successor_node" is the current son

            # if the son is not in the path between the root and his father (ie no circuit is created)
            if not nod_curent.contine_in_drum (successor_node):

                nod_nou = None

                # calculate g and f values ​​for "successor_node" (son)
                # father's g + edge cost (father, son)
                g_succesor = nod_curent.g + cost_succesor
                f_succesor = g_succesor + nod_succesor.h # g-ul fiului + h-ul fiului

                # check if "successor_node" is closed
                # (and delete it, returning the deleted node to old_parcg_node
                old_parcg_node = in_list (closed, successor_node)

                if nod_parcg_vechi is not None: # "nod_succesor" e in closed
                    # if the g calculated for the current path is better (smaller) than
                    # g for the previously found path (g of the node in the closed list)
                    # then I update the parent, g and f
                    # and then I will add "new_node" to the open list
                    if g_succesor <nod_parcg_vechi.g:
                        # remove the node from the closed list
                        closed.remove (nod_parcg_vechi)
                        old_parcg_node.parent = current_node # updating parent
                        nod_parcg_vechi.g = g_successor # update g
                        nod_parcg_vechi.f = f_successor # update f
                        new_node = old_parcg_node # set "new_node", which will then be added in open

                else:
                    # if not closed, check if "successor_node" is open
                    old_parcg_node = in_list (open, successor_node)

                    if nod_parcg_vechi is not None: # "nod_succesor" e in open
                        # if the f calculated for the current path is better (smaller) than
                        # f for the previously found path (f of the node in the open list)
                        # then remove the node from the open list
                        # (because changing the f and g values ​​will ruin the sorting of the open list)
                        # I update the parent, g and f
                        # and then I will add "new_node" in the open list (at the new correct position in sorting)
                        if f_succesor <nod_parcg_vechi.f:
                            open.remove (nod_parcg_vechi)
                            old_parcg_node.parent = current_node
                            nod_parcg_vechi.g = g_succesor
                            nod_parcg_vechi.f = f_succesor
                            new_node = old_parcg_node

                    else: # when "successor_node" is neither closed nor open
                        new_node = BrowseNode (
                            nod_graf = nod_successor, parent = nod_current, g = g_successor)
                        # is calculated automatically in the constructor

                if node_new:
                    # insertion in the list sorted ascending after f
                    # (and for equal fs descending after g)
                    i = 0
                    while i <len (open):
                        if open [i] .f <nod_nou.f:
                            i + = 1
                        else:
                            while i <len (open) and open [i] .f == nod_nou.f and open [i] .g> nod_nou.g:
                                i + = 1
                            break

                    open.insert (i, node_new)

                    print ("\ n ------------------ Conclusion -----------------------")
     if len (open) == 0:
         print ("The open list is empty, we have no way from the start node to the destination node")
     else:
         print ("Minimum cost path:" + str_info_nodes (current_node.tree_path ()))


# Input
N = 3 # number of missionaries or cannibals, in total 2N
M = 2 # number of seats in the boat
initial_configuration = Configuration ([[0, 0], [3, 3], 1])
purpose_configuration = Configuration ([[3, 3], [0, 0], 0])

if __name__ == "__main__":
     problem = Problem ()
     NodParcurgere.problema = problem
     a_star ()