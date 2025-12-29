import flet as ft
from UI.view import View
from model.model import Model


class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def popolaDropdown(self):
        """
        Questo metodo va chiamato DAL MAIN dopo view.load_interface().
        Carica solo gli anni.
        """
        years = self._model.get_all_years()
        self._view.dd_anno.options.clear()

        for year in years:
            self._view.dd_anno.options.append(ft.dropdown.Option(str(year)))

        self._view.update_page()

    def read_anno(self, e):
        """
        Questo metodo è collegato all'evento on_change della tendina Anno.
        Carica le squadre e aggiorna il testo.
        """
        anno = self._view.dd_anno.value
        if anno is None:
            return


        squadre = self._model.getTeamsByYear(anno)


        self._view.dd_squadra.options.clear()
        for s in squadre:
            self._view.dd_squadra.options.append(ft.dropdown.Option(key=s.teamCode, text=s.name))

        self._view.txt_out_squadre.controls.clear()

        self._view.txt_out_squadre.controls.append(ft.Text(f"Trovate {len(squadre)} squadre nel {anno}:"))

        for s in squadre:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{s.name} ({s.teamCode})"))

        self._view.update_page()

    def handle_crea_grafo(self, e):
        pass

    def handle_dettagli(self, e):
        pass

    def handle_percorso(self, e):
        pass