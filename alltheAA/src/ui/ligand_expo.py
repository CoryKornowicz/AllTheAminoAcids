from collections import namedtuple
from PyQt6.QtWidgets import QWidget 
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtCore import Qt, QObject, pyqtSignal
import math
from bs4 import BeautifulSoup
import requests

from urllib.parse import quote_plus
import numpy as np

BASE_URL = "http://ligand-expo.rcsb.org/"

#[http://ligand-expo.rcsb.org/] [pyapps/ldHandler.py?formid=cc-browse-search] [&category=aa] [&target=CC%28C%29CC%28C%28%3DO%29O%29N] [&operation=fpsmi] # smiles
#           BASE_URL                            Browse/Search                    Category?                  SMILES                    Similarity (Smiles Patter, Chemical Fingerprint)

#[http://ligand-expo.rcsb.org/] [pyapps/ldHandler.py?formid=cc-index-search] [&target=Methionine] [&operation=name-close] # name-substring # name-exact

LigandExpoResults = namedtuple("LigandExpoResults", "tag name smiles")


class LigandExpoFetcher(QObject):
    
    _submitted = pyqtSignal(list)
    _progress_update = pyqtSignal(int)
    
    def __init__(self, parent):
        super().__init__(parent)
        self.results = []
        
        
    def _return_results(self):
        self._submitted.emit(self.results)
        self._progress_update.emit(100)

    
    def _make_call(self, pyapp, target, operation):
        
        try:
            assert target != ""
        except AssertionError:
            print("No target")
            self._progress_update.emit(100)
            return
        
        self._progress_update.emit(10)
        
        try:
            if pyapp == "browse":
                
                assert operation in ["fpsmi", "smiles"]
                
                url = "{}pyapps/ldHandler.py?formid=cc-browse-search&category=aa&target={}&operation={}".format(BASE_URL, quote_plus(target), operation)
            elif pyapp == "search":
                
                assert operation in ["name-substring", "name-close", "name-exact"]
                
                url = "{}pyapps/ldHandler.py?formid=cc-index-search&target={}&operation={}".format(BASE_URL, target, operation)
            else:
                print("Unsupported pyapp: {}".format(pyapp))
                self._progress_update.emit(100)
        except AssertionError:
            print("Unsupported operation: {}".format(operation))
            self._progress_update.emit(100)
            return
        
        self._progress_update.emit(20)
        
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find_all("tr", class_= lambda text: text in ["rs1-even", "rs1-odd"])
        
        self._progress_update.emit(50)
        
        self.results = []
        self._parse_soup_data(results)
    
    
    def _parse_soup_data(self, results):
        
        if len(results) == 0:
            self._return_results()
            self._progress_update.emit(100) 
        
        x = np.linspace(0, 30, len(results))
        
        for i, res in enumerate(results):
            parsed_data = [
                line.getText().strip().split()
                for line in res
                if line.getText() != "\n"
            ]

            parsed_dict = self._tablefy(parsed_data[-1])
            new_lig = LigandExpoResults(parsed_data[1][0], parsed_dict["name"], parsed_dict["smiles"])
            self.results.extend([new_lig])
            self._progress_update.emit(50 + int(math.floor(x[i])))
        
        if len(self.results) > 0:
            self._return_results()
        
    
    def _tablefy(self, data):
        ret_data = {}
        for i, name in enumerate(data):
            if name == "Name:":
                ret_data["name"] = data[i+1]
            elif name == "SMILES:":
                ret_data["smiles"] = data[i+1]
        return ret_data