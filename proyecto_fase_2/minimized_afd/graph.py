import graphviz as gv

def draw(alfabeto, estados, inicio, trans, final):
    print("Afd leido...")
    print("graficando con graphviz!!!")
    # print("inicio:", str(inicio))
    g = gv.Digraph(format='svg')
    g.graph_attr['rankdir'] = 'LR'
    g.node('ini', shape="point")
    for e in estados:
        if e in final:
            g.node(e, shape="doublecircle")
        else:
            g.node(e)
        if e in inicio:
            g.edge('ini',e)

    for t in trans:
        if t[2] not in alfabeto:
            return 0
        g.edge(t[0], t[1], label=str(t[2]))
    g.render(view=True)

if __name__ == '__main__':
    # estados = ["A","B","C","E"]
    # trans = [("A","B", 0), ("A", "A", 1), ("B","C", 0), ("B", "A", 1), ("C", "D", 0), ("C", "A", 1), ("D", "E", 0), ("D", "A", 1), ("E", "E", 0), ("E", "A", 1)]
    # inicial = ["A"]
    # alf = [0,1]
    # terminal = ("C", "D", "E")

    estadosM = ["A","B","C"]
    transM = [("A","B", 0), ("A", "A", 1), ("B","C", 0), ("B", "A", 1),("C", "C", 0), ("C", "A", 1), ]
    inicialM = ["A"]
    terminalM = ("C")
    alf = [0,1]
    # draw(alf, estados, inicial, trans, terminal)
    draw(alf, estadosM, inicialM, transM, terminalM)