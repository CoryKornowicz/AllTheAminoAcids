
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout, QApplication
from PyQt6.QtGui import QPixmap, QFont
from PyQt6 import QtGui
from PyQt6 import QtCore
from PIL import Image
from .widget import Ui_Widget
from .ligand_expo import LigandExpoFetcher, LigandExpoResults

from rdkit import Chem
from rdkit.Chem import Draw

from operator import attrgetter
from collections import OrderedDict

EXAMPLE_DATA = LigandExpoResults("000", "Test", "CCCCC")


# Class to fetch, display, and swap amino acids with a currently selected amino acid
class AA_ResultWidget(QWidget):
        
    def __init__(self, parent, smiles, name):
        super().__init__(parent)
        
        self.smiles = smiles
        self.name = name
        self.toggled = False
        
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self)
        self.label.mousePressEvent = self._clicked
        self.name_label = QLabel(self)
        self.name_label.setText(name)
        self.name_label.setFont(QFont('Times', 10))
        self.name_label.setMaximumSize(125,20)
        self.name_label.setScaledContents(True)
        
        self.name_label.mousePressEvent = lambda _: self._copy2clip(self.name_label.text())
        
        try:
            self.mol = Chem.MolFromSmiles(smiles)
            mol_image = Draw.MolToImage(self.mol)
            self.label.setPixmap(self.pil2pixmap(mol_image))
            del mol_image
            self.label.setScaledContents(True)
            self.label.setMaximumSize(125,125)
            self.label.setMinimumSize(100,100)
        except Exception as e:
            print(e)
        
        self.layout().addWidget(self.label)
        self.layout().addWidget(self.name_label)
        # vbox.addStretch()
        
        
    #~Pixmap Magic~#
    #https://stackoverflow.com/questions/34697559/pil-image-to-qpixmap-conversion-issue
    def pil2pixmap(self, im):

        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif  im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        # Bild in RGBA konvertieren, falls nicht bereits passiert
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format.Format_ARGB32)
        return QtGui.QPixmap.fromImage(qim)
        
    def _clicked(self, event):
        self.toggled = not self.toggled
        if self.toggled: 
            # MARK: - Set Border Color
            self.label.setStyleSheet("border: 5px solid green;")
        else:
            self.label.setStyleSheet("")

    def _copy2clip(self, name_string):
        QApplication.clipboard().setText(name_string)
        


class AA_Widget(QWidget, Ui_Widget):
    
    def __init__(self):
        super().__init__()
        
        self.AMINO_ACIDS = sorted([
            LigandExpoResults("MET", "l-methionine", "CSCC[C@@H](C(=O)O)N"),
            LigandExpoResults("PHE", "l-phenylalanine", "c1ccc(cc1)C[C@@H](C(=O)O)N"),
            LigandExpoResults("LEU", "l-leucine", "CC(C)C[C@@H](C(=O)O)N"),
            LigandExpoResults("SER", "l-serine", "C([C@@H](C(=O)O)N)O"),
            LigandExpoResults("TYR", "l-tyrosine", "c1cc(ccc1C[C@@H](C(=O)O)N)O"),
            LigandExpoResults("CYS", "l-cysteine", "C([C@@H](C(=O)O)N)S"),
            LigandExpoResults("TRP", "l-tryptophan", "c1ccc2c(c1)c(c[nH]2)C[C@@H](C(=O)O)N"),
            LigandExpoResults("VAL", "l-valine", "CC(C)[C@@H](C(=O)O)N"),
            LigandExpoResults("PRO", "l-proline", "C1C[C@H](NC1)C(=O)O"),
            LigandExpoResults("ALA", "l-alanine", "CC(C(=O)O)N"),
            LigandExpoResults("ILE", "l-isoleucine", "CC[C@H](C)[C@@H](C(=O)O)N"),
            LigandExpoResults("HIS", "l-histidine", "c1c([nH+]c[nH]1)C[C@@H](C(=O)O)N"),
            LigandExpoResults("GLN", "l-glutamine", "C(CC(=O)N)[C@@H](C(=O)O)N"),
            LigandExpoResults("ASN", "l-asparagine", "C([C@@H](C(=O)O)N)C(=O)N"),
            LigandExpoResults("GLY", "l-glycine", "C(C(=O)O)N"),
            LigandExpoResults("THR", "l-threonine", "C[C@H]([C@@H](C(=O)O)N)O"),
            LigandExpoResults("ASP", "l-aspartic acid", "C([C@@H](C(=O)O)N)C(=O)O"),
            LigandExpoResults("GLU", "l-glutamic acid", "C(CC(=O)O)[C@@H](C(=O)O)N"),
            LigandExpoResults("LYS", "l-lysine", "C(CC[NH3+])C[C@@H](C(=O)O)N"),
            LigandExpoResults("ARG", "l-arginine", "C(C[C@@H](C(=O)O)N)CNC(=[NH2+])N")
            ], key=attrgetter('name'))  

        # Build UI

        self.setupUi(self)
        self.aminoAcidComboBox.addItems(list(map(lambda x: x.name, self.AMINO_ACIDS)))
        self.ligandImageArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents.setLayout(QGridLayout())
        self.scrollAreaWidgetContents.layout().setSpacing(5)

        self.store_results = OrderedDict()
        self._rendered_widgets = {}
        
        self._reload_scrollarea()

        #Connect And Setup Classes

        # Build Pagify
        self.pageBox.valueChanged.connect(self._adjust_counter_label)
        self._items_per_page = 20
        
        self.ligandSearchButton.clicked.connect(self._search_ligand_expo)
        self.browseSimilarButton.clicked.connect(self._browse_ligand_by_amino)
        self.resetNormalAAButton.clicked.connect(self._reset_pushButton_action)
        
        self.explorer = LigandExpoFetcher(self)
        self.explorer._submitted.connect(self._recieve_amino_acid_results)
        self.explorer._progress_update.connect(self._progress_update)
        
    
    @QtCore.pyqtSlot(int)
    def _progress_update(self, num):
        
        num = int(num)
        
        self.ligExpoProgressBar.setValue(num)
        
        if num == 100:
            self.ligExpoProgressBar.setValue(0)
            
    
    
    # Clear Scroll Area to deafault amino acids 
    def _clear_scroll_area(self):
        self.store_results = OrderedDict()
        self._rendered_widgets = {}
        
        #reset progess bar
        self.ligExpoProgressBar.setValue(0)
        
        layout = self.scrollAreaWidgetContents.layout()
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().setParent(None)
    
    # Preload/Reload the scrollarea to the default amino acids
    def _reload_scrollarea(self):
        
        if len(self.AMINO_ACIDS) == 0 and len(self.store_results) == 0: return
        
        if len(self.store_results) > 0:
            if self.pageBox.value() > (len(self.store_results) // self._items_per_page) and len(self.store_results) > self._items_per_page:
                print("Page Number too high")
                return 
            
            page_start = (self.pageBox.value()-1) * self._items_per_page
            page_end = (self.pageBox.value()) * self._items_per_page
            
            layout = self.scrollAreaWidgetContents.layout()
            for i in reversed(range(layout.count())): 
                layout.itemAt(i).widget().setVisible(False)
                
            for i, amino in enumerate(list(self.store_results.values())[page_start:page_end]):
                
                row = i // 2
                col = i % 2
                
                if amino.tag in self._rendered_widgets:
                    render = self._rendered_widgets[amino.tag]
                    render.show()
                else:
                    render = self.render_amino_to_widget(amino.smiles, amino.name)
                    self._rendered_widgets[amino.tag] = render
                    self.scrollAreaWidgetContents.layout().addWidget(render, row, col)
        else:
            for i, amino in enumerate(self.AMINO_ACIDS):
                
                row = i // 2
                col = i % 2
                
                if amino.tag in self._rendered_widgets:
                    render = self._rendered_widgets[amino.tag]
                else:
                    render = self.render_amino_to_widget(amino.smiles, amino.name)
                    self._rendered_widgets[amino.tag] = render
                    
                self.scrollAreaWidgetContents.layout().addWidget(render, row, col)
            

    # callback to update the counter label
    def _adjust_counter_label(self, num):
        
        if len(self.store_results) > 0:
            self.pageLabel.setText("Page: {} of {}".format(num, len(self.store_results) // self._items_per_page))
            self.ligandTotalLabel.setText("Total: {}".format(len(self.store_results)))
            self._reload_scrollarea()
        else:
            self.pageLabel.setText("Page: {}".format(num))
            self.ligandTotalLabel.setText("Total: {}".format(len(self.AMINO_ACIDS)))
    
    
    # Method to construct amino acid widget with smiles and name 
    def render_amino_to_widget(self, smiles, name):
        return AA_ResultWidget(self.scrollAreaWidgetContents, smiles, name)
    
    
    # Method to browse ligand expo for a given standard amino acid
    def _browse_ligand_by_amino(self):
        smiles = self.AMINO_ACIDS[self.aminoAcidComboBox.currentIndex()].smiles
        similarity = self.browseOperationBox.currentText()
        
        self.explorer._make_call("browse", smiles, similarity)
        
    
    # Method to search ligand expo by similar amino acids
    def _search_ligand_expo(self):
        print(self.ligandSearchText.text())
        
        target = self.ligandSearchText.text()
        similarity = self.searchOperationBox.currentText()
        
        self.explorer._make_call("search", target, similarity)
        
             
    @QtCore.pyqtSlot(list)
    def _recieve_amino_acid_results(self, amino_acids):
        if len(amino_acids) > 0:
            self._clear_scroll_area()
            for amino in amino_acids:
                self.store_results[amino.tag] = amino
            self.pageBox.setValue(1)
            self.pageLabel.setText("Page: {} of {}".format(1, len(self.store_results) // self._items_per_page))
            self.ligandTotalLabel.setText("Total: {}".format(len(self.store_results)))
            self._reload_scrollarea()
        else:
            print("No results")
    
    
    def _reset_pushButton_action(self):
        self._clear_scroll_area()
        self._reload_scrollarea()
        self._adjust_counter_label(1)
    
    
        
    
        
        