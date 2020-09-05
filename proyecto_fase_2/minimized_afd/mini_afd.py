class node:
    #propiedad nombre de nodos
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return("NODE_"+self.name)

    def __eq__(self, other):
        return(str(self) == str(other))

    def __hash__(self):
        return(str(self).__hash__())


class edge:
    #direccion de los nodos
    def __init__(self, leftNode, rightNode, name="", directed=False):
        self.directed = directed
        self.leftNode = leftNode
        self.rightNode = rightNode
        self.name = name
        
    def __str__(self):
        if self.directed:
            return("EDGE_{}_({})->({})".format(self.name,
                                               self.leftNode.name,
                                               self.rightNode.name))
        else:
            return("EDGE_{}_({})--({})".format(self.name,
                                               self.leftNode.name,
                                               self.rightNode.name))

    def getNodes(self):
        return([self.leftNode, self.rightNode])

    def isDirected(self):
        return(self.directed)

class graph:
    #retornamos las sub graphs de cada nodo con su direccion
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.make()
        
    def getNodes(self, f):
        returningNodes = []
        for node in self.nodes:
            if f(node):
                returningNodes.append(node)
        return(returningNodes)

    def getEdges(self, f):
        returningEdges = []
        for edge in self.edges:
            if f(edge):
                returningEdges.append(edge)
        return(returningEdges)

    def make(self):
        #returnamos los nodos y edges entro de una lista

        self.graphDict = dict()
        for node in self.nodes:
            self.graphDict[node] = []
        for edge in self.edges:
            leftNode, rightNode = edge.getNodes()
            if edge.isDirected():
                self.graphDict[leftNode].append((edge, rightNode))
            else:
                self.graphDict[leftNode].append((edge, rightNode))
                self.graphDict[rightNode].append((edge, leftNode))
    
    def getSubGraph(self, node, depth=1):
        def collapsed(lst):
            temp = []

            def collapseList(l):
                for ele in l:
                    if isinstance(ele, list):
                        collapseList(ele)
                    else:
                        temp.append(ele)

            collapseList(lst)
            return(temp)
            #seguimiento de las direcciones returnando la conexion con las sup graph
        nodesOfSG = [[node]]
        edgesOfSG = []
        for i in range(depth):
            localNodes = []
            localEdges = []
            for node in collapsed(nodesOfSG[-1]):
                l = self.graphDict[node]
                if len(l) > 0:
                    localNodes.append(list(map(lambda x: x[1], l)))
                    localEdges.append(list(map(lambda x: x[0], l)))
            if len(localNodes) == 0:
                break
            nodesOfSG.append(localNodes)
            edgesOfSG.append(localEdges)
        
        return graph(collapsed(nodesOfSG), collapsed(edgesOfSG))


class state(node):
    #manejo de los estados
    def __init__(self, name, isInitState=False, isFinalState=False):
        super().__init__(name)
        self.isInitState = isInitState
        self.isFinalState = isFinalState

    def setInitState(self, isInitState):
        self.isInitState = isInitState

    def setFinalState(self, isFinalState):
        self.isFinalState = isFinalState

    def __str__(self):
        return("State_"+self.name
               + "_i-"+str(self.isInitState)
               + "_f-"+str(self.isFinalState))

    def __eq__(self, other):
        return(self.name == other.name
               and self.isInitState == other.isInitState
               and self.isFinalState == other.isFinalState)

    def __hash__(self):
        return(str(self).__hash__())


class transition(edge):
    def __init__(self, leftState, rightState, symbol, name=""):
        super().__init__(leftState, rightState, "", True)
        self.symbol = symbol


class AFD(graph):
    #clase AFD
    def __init__(self, states, transitions):
        super().__init__(states, transitions)
        self.initState = [s for s in states if s.isInitState][0]
        self.finalStates = [f for f in states if f.isFinalState]

    def run(self, s):
        currentState = self.initState
        for symbol in s:
            sub = self.getSubGraph(currentState)
            trans = sub.getEdges(lambda x: x.symbol == symbol)[0]
            currentState = trans.getNodes()[1]
        return(currentState in self.finalStates)
    # metodo minimizar
    def minimize(self):
        import copy as cp
        dupl = cp.deepcopy(self)
        pairs = []
        pedges = []
        for i in range(len(self.nodes)):
            for j in range(i,len(self.nodes)):
                pairs.append(node(str(i)+" "+str(j)))
        for p in pairs:
            n1 = dupl.nodes[int(p.name.split()[0])]
            n2 = dupl.nodes[int(p.name.split()[1])]
            n1sg = dupl.getSubGraph(n1)
            n2sg = dupl.getSubGraph(n2)
            n1on0 = n1sg.getEdges(lambda e: e.symbol == '0')[0].rightNode
            n1on1 = n1sg.getEdges(lambda e: e.symbol == '1')[0].rightNode
            n2on0 = n2sg.getEdges(lambda e: e.symbol == '0')[0].rightNode
            n2on1 = n2sg.getEdges(lambda e: e.symbol == '1')[0].rightNode
            n1on0index = self.nodes.index(n1on0)
            n2on0index = self.nodes.index(n2on0)
            n1on1index = self.nodes.index(n1on1)
            n2on1index = self.nodes.index(n2on1)
            if n1on0index > n2on0index:
                n1on0index, n2on0index = n2on0index, n1on0index
            if n1on1index > n2on1index:
                n1on1index, n2on1index = n2on1index, n1on1index
            pairIndexon0 = n1on0index*len(self.nodes)-int((n1on0index)*(n1on0index-1)/2)+n2on0index-n1on0index
            pairIndexon1 = n1on1index*len(self.nodes)-int((n1on1index)*(n1on1index-1)/2)+n2on1index-n1on1index
            pedges.append(edge(pairs[pairIndexon0], p, "", True))
            pedges.append(edge(pairs[pairIndexon1], p, "", True))
        pairGraph = graph(pairs, pedges)
        distinguished = []
        for p in pairGraph.getNodes(lambda x: x):
            ln = dupl.nodes[int(p.name.split()[0])]
            rn = dupl.nodes[int(p.name.split()[1])]
            if not (ln.isFinalState == rn.isFinalState):
                sg = pairGraph.getSubGraph(p, len(pedges))
                for n in sg.getNodes(lambda x: x):
                    distinguished.append(n)
        indistinguishables = [n for n in pairs if not (n in distinguished)]
        nodestobeDeleted = []
        edgestobeDeleted = []
        for i in indistinguishables:
            n1 = dupl.nodes[int(i.name.split()[0])]
            n2 = dupl.nodes[int(i.name.split()[1])]
            if n1 == n2:
                continue
            edgeston2 = dupl.getEdges(lambda e: e.rightNode == n2)
            for e in edgeston2:
                e.rightNode = n1
            nodestobeDeleted.append(n2)
            edgestobeDeleted.append(dupl.getSubGraph(n2,1).getEdges(lambda x: x)[0])
            edgestobeDeleted.append(dupl.getSubGraph(n2,1).getEdges(lambda x: x)[1])
        for nd in nodestobeDeleted:
            if nd in dupl.nodes:
                dupl.nodes.remove(nd)
        for ed in edgestobeDeleted:
            if ed in dupl.edges:
                dupl.edges.remove(ed)
        dupl.finalStates = [f for f in dupl.nodes if f.isFinalState]
        dupl.make()
        return(dupl)
# display con matplotlib
    def display(self):
        import matplotlib.pyplot as plt
        import math
        import random
        import numpy as np
        
        ns = len(self.nodes)    # numero de estados
        rs = math.pi/(2*ns) 

        colors = [(random.random(), random.random(), random.random())
                  for state in self.nodes]
        theta = 0
        for state in self.nodes:
            cxpos = 1*math.cos(math.radians(theta))
            cypos = 1*math.sin(math.radians(theta))
            txpos = (1+(2*rs))*math.cos(math.radians(theta))
            typos = (1+(2*rs))*math.sin(math.radians(theta))
            stateColor = colors[self.nodes.index(state)]
            invStateColor = tuple([1-x for x in stateColor])
            c = plt.Circle((cxpos, cypos), rs, color=stateColor)
            t = plt.Text(txpos,
                         typos,
                         state.name,
                         horizontalalignment='center',
                         fontsize=15,
                         verticalalignment='top')
            plt.gcf().gca().add_artist(c)
            plt.gcf().gca().add_artist(t)
            if state.isFinalState:
                finalIndicatorCircle = plt.Circle((cxpos, cypos),
                                                  rs-rs/10,
                                                  fill=False,
                                                  color=invStateColor)
                plt.gcf().gca().add_artist(finalIndicatorCircle)
            theta = theta + (360/ns)
            
        for transition in self.edges:
            fromState, toState = transition.getNodes()
            fromTheta = self.nodes.index(fromState)*(360/ns)
            toTheta = self.nodes.index(toState)*(360/ns)
            fromx, fromy = (math.cos(math.radians(fromTheta)),
                            math.sin(math.radians(fromTheta)))
            tox, toy = (math.cos(math.radians(toTheta)),
                        math.sin(math.radians(toTheta)))
            
            if transition.symbol == '1':
                l = plt.Line2D([fromx-rs/4, tox-rs/4],
                               [fromy-rs/4, toy-rs/4],
                               5,
                               color=colors[self.nodes.index(fromState)])
                plt.gcf().gca().add_artist(l)
            else:
                l = plt.Line2D([fromx+rs/4, tox+rs/4],
                               [fromy+rs/4, toy+rs/4],
                               5,
                               linestyle='dashed',
                               color=colors[self.nodes.index(fromState)])
                plt.gcf().gca().add_artist(l)
        plt.axis('off')
        plt.show()
    # cargar archivo
    def fromFile(path):
        stateNames = []
        initIndex = 0
        finalIndices = []
        transitionsIndices = []
        with open(path, 'r') as f:
            for line in f:
                line = line.strip()
                if line.startswith('\n'):
                    continue
                line = line.strip('\n')
                if line.startswith('#'):
                    continue
                elif line.startswith('states:'):
                    stateNames = line.split(" ")[1:]
                elif line.startswith('init:'):
                    initIndex = stateNames.index(line.split(" ")[1])
                elif line.startswith('final:'):
                    for final_st in line.split(' ')[1:]:
                        finalIndices.append(stateNames.index(final_st))
                else:
                    fromState, toState, symbol = line.split(" ")
                    transitionsIndices.append((stateNames.index(fromState),
                                               stateNames.index(toState),
                                               symbol))
        states = [state(name) for name in stateNames]
        states[initIndex].setInitState(True)
        for f in finalIndices:
            states[f].setFinalState(True)
        transitions = [transition(states[t[0]],
                                  states[t[1]],
                                  t[2])
                       for t in transitionsIndices]
        return AFD(states, transitions)
    # escribir a un archivo
    def toFile(self, path, comment=''):
        with open(path, 'w') as f:
            f.write('# '+comment+'\n')
            states = [x.name for x in self.nodes]
            f.write('states: ')
            for s in states:
                f.write(s+' ')
            f.write('\n')
            f.write('init: '+self.initState.name+'\n')
            fstates = [x.name for x in self.finalStates]
            f.write('final: ')
            for fs in fstates:
                f.write(fs+' ')
            f.write('\n')
            for fromnode in self.nodes:
                for edge, tonode in self.graphDict[fromnode]:
                    f.write(fromnode.name+' '+tonode.name+' '+edge.symbol+'\n')      

# afd = AFD.fromFile("AFD.txt")

# mini_afd = afd.minimize()

# # afd.display()

# mini_afd.display()

# mini_afd.toFile("min.txt")
