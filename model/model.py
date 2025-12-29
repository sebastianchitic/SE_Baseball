from database.dao import DAO
class Model:
    def __init__(self):
        pass

    def get_all_years(self):
        return DAO.getAllYears()

    def getTeamsByYear(anno):
        return DAO.getTeamsByYear(anno)



