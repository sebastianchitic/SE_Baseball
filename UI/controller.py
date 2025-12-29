import flet as ft
from UI.view import View
from model.model import Model
from database.dao import DAO

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model
        self._DAO = DAO


    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""


    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""


    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""


    def popolaDropdown(self):
        years = self._model.get_all_years()
        self._view.dd_anno.options.clear()
        for year in years:
            self._view.dd_anno.options.append(ft.DropdownOption(str(year)))
        self._view.page.update()

        squadre = self._DAO.getTeamsByYear(year)
        self._view.dd_squadra.options.clear()
        for s in squadre:
            self._view.dd_squadra.options.append(ft.dropdown.Option(key=s.teamCode, text=s.name))
        self._view.txt_out_squadre.clear()
        self._view.txt_out_squadre.controls.append(ft.Text(f"Trovate {len(squadre)} squadre nel {year}:"))
        for s in squadre:
            self._view.dd_squadra.controls.append(ft.dropdown.Option(key=s.teamCode, text=s.name))
        self._view.page.update()





