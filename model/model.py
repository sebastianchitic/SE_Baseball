from database.dao import DAO
class Model:
    def __init__(self):
        pass

    def get_all_years(self):
        return DAO.getAllYears()



