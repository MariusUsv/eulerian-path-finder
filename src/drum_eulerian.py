import networkx as nx
import matplotlib.pyplot as plt

def citeste_graf(fisier):
    graf = {}
    with open(fisier) as f:
        for linie in f:
            a, b = map(int, linie.split())
            graf.setdefault(a, set()).add(b)
            graf.setdefault(b, set()).add(a)
    return graf

def eulerian(graf):
    impare = [n for n in graf if len(graf[n]) % 2 == 1]
    return len(impare) in [0, 2], impare

def hierholzer(graf):
    g = {n: set(v) for n, v in graf.items()}
    nod, stiva, drum = next(iter(g)), [], []
    while stiva or g[nod]:
        if not g[nod]:
            drum.append(nod)
            nod = stiva.pop()
        else:
            stiva.append(nod)
            v = g[nod].pop()
            g[v].remove(nod)
            nod = v
    drum.append(nod)
    return drum

def deseneaza(graf, drum):
    G = nx.Graph()
    for u in graf:
        for v in graf[u]:
            G.add_edge(u, v)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray',
            node_size=1500, font_size=12)
    plt.title("Drum Eulerian")
    plt.show()

if __name__ == "__main__":
    print("=== DRUM EULERIAN ===")
    fisier = input("Introduceți numele fișierului .txt (ex: graf_mare.txt): ")
    try:
        graf = citeste_graf(fisier)
        este, impare = eulerian(graf)
        if este:
            drum = hierholzer(graf)
            print("Drumul Eulerian este:")
            print(" → ".join(map(str, drum)))
            deseneaza(graf, drum)
        else:
            print("NU există drum Eulerian.")
            print("Noduri impare:", impare)
    except Exception as e:
        print("Eroare:", e)

    input("\nApasă ENTER pentru a închide...")
