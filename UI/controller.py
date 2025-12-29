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

        self._view.update()

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
            self._view.dd_squadra.options.append(ft.dropdown.Option(key=s.team_code, text=s.name))

        self._view.txt_out_squadre.controls.clear()

        self._view.txt_out_squadre.controls.append(ft.Text(f"Trovate {len(squadre)} squadre nel {anno}:"))

        for s in squadre:
            self._view.txt_out_squadre.controls.append(ft.Text(f"{s.name} ({s.team_code})"))

        self._view.update()

    def handle_crea_grafo(self, e):
        try:
            if self._view.dd_anno.value is None:
                self._view.show_alert("Seleziona un anno!")
                return
            anno = int(self._view.dd_anno.value)
        except ValueError:
            self._view.show_alert("Inserire un numero valido")
            return

        self._model.buildGraph(anno)

        n_nodi, n_archi = self._model.getGraphDetails()

        self._view.txt_risultato.controls.clear()

        self._view.txt_risultato.controls.append(ft.Text("Grafo creato correttamente!"))
        self._view.txt_risultato.controls.append(ft.Text(f"Numero di vertici: {n_nodi}"))
        self._view.txt_risultato.controls.append(ft.Text(f"Numero di archi: {n_archi}"))

        self._view.update()

    def handle_dettagli(self, e):
        squadra_code = self._view.dd_squadra.value

        if squadra_code is None:
            self._view.show_alert("Seleziona una squadra dalla tendina!")
            return

        vicini = self._model.getSortedNeighbors(squadra_code)

        # 3. Stampa dei risultati
        self._view.txt_risultato.controls.clear()
        self._view.txt_risultato.controls.append(ft.Text(f"Adiacenti alla squadra {squadra_code}:"))

        for vicino, peso in vicini:
            self._view.txt_risultato.controls.append(ft.Text(f"{vicino.name} - {round(peso)} $"))

        self._view.update()

    def handle_percorso(self, e):
        pass