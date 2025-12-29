import networkx as nx

from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self.nodes = None
        self.edges = None

    def get_all_years(self):
        return DAO.getAllYears()

    def getTeamsByYear(self, anno):
        return DAO.getTeamsByYear(anno)

    def weighted_graph(self, year):
        self.G.clear()
        squadre = DAO.getTeamsByYear(year)
        years = DAO.getAllYears()
        salary_map = DAO.getSalary(year)

        self.G.add_nodes_from(squadre)
        self.id_map = {s.team_code: s for s in squadre}

        for i in range(len(squadre)):
            for j in range(i+1, len(squadre)):
                t1 = squadre[i]
                t2 = squadre[j]

                sal1 = salary_map.get(t1.team_code, 0)
                sal2 = salary_map.get(t2.team_code, 0)

                sal = sal1 + sal2
                self.G.add_edge(i, j, weight=sal)

    def details(self):
        return self.G.number_of_edges(), self.G.number_of_nodes()

    def get_SortedNeighbors(self, team_code):
        team_node = self.id_map.get(team_code)

        if team_node is None:
            return []
        result = []

        for neighbor in self.G.neighbors(team_node):
            peso = self.G[team_node][neighbor]['weight']
            result.append((neighbor, peso))

        result.sort(key=lambda x: x[1], reverse=True)
        return result















