import networkx as nx

from database.dao import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._nodes = []
        self._idMap = {}

    def get_all_years(self):
        return DAO.getAllYears()

    def getTeamsByYear(self, year):
        self._nodes = DAO.getTeamsByYear(year)
        # Creo mappa per recuperare velocemente le squadre
        self._idMap = {t.team_code: t for t in self._nodes}
        return self._nodes

    def buildGraph(self, year):
        self._grafo.clear()
        if not self._nodes:
            self.getTeamsByYear(year)

        self._grafo.add_nodes_from(self._nodes)

        # Recupero mappa salari
        salary_map = DAO.getSalary(year)

        # Doppio ciclo per creare archi
        for i in range(len(self._nodes)):
            for j in range(i + 1, len(self._nodes)):
                t1 = self._nodes[i]
                t2 = self._nodes[j]

                # Somma salari (gestisce caso salario mancante mettendo 0)
                s1 = salary_map.get(t1.team_code, 0)
                s2 = salary_map.get(t2.team_code, 0)

                self._grafo.add_edge(t1, t2, weight=(s1 + s2))

    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def getSortedNeighbors(self, team_code):
        # Cerco il nodo oggetto partendo dalla stringa
        team_node = self._idMap.get(team_code)
        if team_node is None:
            return []

        vicini = []
        for neighbor in self._grafo.neighbors(team_node):
            peso = self._grafo[team_node][neighbor]['weight']
            vicini.append((neighbor, peso))

        vicini.sort(key=lambda x: x[1], reverse=True)
        return vicini