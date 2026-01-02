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
        self._idMap = {t.team_code: t for t in self._nodes}
        return self._nodes

    def buildGraph(self, year):
        self._grafo.clear()
        if not self._nodes:
            self.getTeamsByYear(year)

        self._grafo.add_nodes_from(self._nodes)

        salary_map = DAO.getSalary(year)

        for i in range(len(self._nodes)):
            for j in range(i + 1, len(self._nodes)):
                t1 = self._nodes[i]
                t2 = self._nodes[j]

                s1 = salary_map.get(t1.team_code, 0)
                s2 = salary_map.get(t2.team_code, 0)

                self._grafo.add_edge(t1, t2, weight=(s1 + s2))

    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def getSortedNeighbors(self, team_node):
        if team_node is None:
            return []

        vicini = []
        for neighbor in self._grafo.neighbors(team_node):
            peso = self._grafo[team_node][neighbor]['weight']
            vicini.append((neighbor, peso))

        vicini.sort(key=lambda x: x[1], reverse=True)
        return vicini

    def getPercorsoMax(self, team_code):
        source_node = self._idMap.get(team_code)
        if source_node is None:
            return [], 0

        self.percorsoMax = []
        self.peso_Max = 0

        parziale = [source_node]
        self.ricorsione(parziale, 0, float('inf'))

        return self.percorsoMax, self.peso_Max


    def ricorsione(self, parziale, peso_totale, ultimo_peso):
        if peso_totale > self.peso_Max:
            self.peso_Max = peso_totale
            self.percorsoMax = list(parziale)

        last_node = parziale[-1]
        vicini = self.getSortedNeighbors(last_node)

        vicini_ammissibili = [v for v in vicini if v[1] < ultimo_peso and v[0] not in parziale]

        K = 2
        vicini_k = vicini_ammissibili[:K]

        for vicino, peso_arco in vicini_k:
            parziale.append(vicino)
            self.ricorsione(parziale, peso_totale + peso_arco, peso_arco)
            parziale.pop()















