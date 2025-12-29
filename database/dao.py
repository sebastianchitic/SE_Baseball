from database.DB_connect import DBConnect
from model.Team import Team


class DAO:
    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            print("Connessione fallita")
            return result

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT year
         FROM team
         WHERE year >= 1980
         ORDER BY year DESC
         """

        cursor.execute(query)
        for row in cursor:
            result.append(row['year'])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getTeamsByYear(year):
        conn = DBConnect.get_connection()
        result = []
        if conn is None:
            print("Connessione fallita")
            return result

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT ID as id, year, team_code, name
        FROM Team
        WHERE year = %s"""

        cursor.execute(query, (year,))
        for row in cursor:
            team = Team(row['id'], row['year'], row['team_code'], row['name'])
            result.append(team)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getSalary(year):
        conn = DBConnect.get_connection()
        result = {}
        if conn is None:
            print("Connessione fallita")
            return result

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT team_code, SUM(salary) as totsalary
        FROM salary
        WHERE year = %s
        GROUP BY team_code"""

        cursor.execute(query, (year,))
        for row in cursor:
            result[row['team_code']] = row['totsalary']
        cursor.close()
        conn.close()
        return result