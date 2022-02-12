# vim: set expandtab shiftwidth=4 softtabstop=4:

from PyQt6.QtWidgets import QWidget, QApplication

import sys

try:
    from chimerax.core.toolshed import BundleAPI
    from .ui import AA_Widget
    # Subclass from chimerax.core.toolshed.BundleAPI and
    # override the method for registering commands,
    # inheriting all other methods from the base class.
    class _AllTheAminoAcids(BundleAPI):

        api_version = 1     # start_tool called with BundleInfo and
                            # ToolInfo instance (vs. BundleInfo and
                            # tool name when api_version==0 [the default])

        # Override method
        @staticmethod
        def start_tool(session, bi, ti):
            # session is an instance of chimerax.core.session.Session
            # bi is an instance of chimerax.core.toolshed.BundleInfo
            # ti is an instance of chimerax.core.toolshed.ToolInfo

            # This method is called once for each time the tool is invoked.

            # We check the name of the tool, which should match one of the
            # ones listed in bundle_info.xml (without the leading and
            # trailing whitespace), and create and return an instance of the
            # appropriate class from the ``tool`` module.
            if ti.name == "AllTheAminoAcids":
                from . import tool
                return tool.AllTheAATool(session, ti.name)
            raise ValueError("trying to start unknown tool: %s" % ti.name)

        @staticmethod
        def get_class(class_name):
            # class_name will be a string
            if class_name == "AllTheAminoAcids":
                from . import tool
                return tool.AllTheAATool
            raise ValueError("Unknown class name '%s'" % class_name)

    # Create the ``bundle_api`` object that ChimeraX expects.
    bundle_api = _AllTheAminoAcids()
except ImportError:
    from ui import AA_Widget


if __name__ == "__main__":
    application = QApplication([])
    widget = AA_Widget()
    widget.show()
    sys.exit(application.exec())
    # from PyQt6.QtWidgets import *
    # app = QApplication([])

    # scroll = QScrollArea()
    # scroll.setWidgetResizable(True) # CRITICAL

    # inner = QFrame(scroll)
    # inner.setLayout(QVBoxLayout())

    # scroll.setWidget(inner)  # CRITICAL


    # def on_remove_widget(button):
    #     button.deleteLater()


    # def populate():
    #     for i in range(40):
    #         b = QPushButton(inner)
    #         b.setText(str(i))
    #         b.clicked.connect(b.deleteLater)
    #         inner.layout().addWidget(b)

    # b = QPushButton(inner)
    # b.setText("Populate")
    # b.clicked.connect(populate)
    # inner.layout().addWidget(b)

    # scroll.show()
    # app.exec()