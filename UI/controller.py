import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    """ Altri possibili metodi per gestire di dd_anno """""

    def popolaDropdown(self):
        years = self.model.get_all_years()
        self._view.dd_anno.options.clear()
        for year in years:
            self._view.dd_anno.options.append(ft.DropdownOption(year))
        self._view.page.update()

    def handle_crea_grafo(self, e):
        """ Handler per gestire creazione del grafo """""
        # TODO

    def handle_dettagli(self, e):
        """ Handler per gestire i dettagli """""
        # TODO

    def handle_percorso(self, e):
        """ Handler per gestire il problema ricorsivo di ricerca del percorso """""
        # TODO





