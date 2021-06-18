from PySide2 import QtWidgets

from mapclientplugins.argonviewerstep.ui.ui_argonviewerwidget import Ui_ArgonViewerWidget
from opencmiss.zincwidgets.regioneditorwidget import RegionEditorWidget
from opencmiss.zincwidgets.modelsourceseditorwidget import ModelSourcesEditorWidget
from opencmiss.zincwidgets.sceneviewereditorwidget import SceneviewerEditorWidget
from opencmiss.zincwidgets.sceneeditorwidget import SceneEditorWidget
from opencmiss.zincwidgets.spectrumeditorwidget import SpectrumEditorWidget
from opencmiss.zincwidgets.tessellationeditorwidget import TessellationEditorWidget
from opencmiss.zincwidgets.timeeditorwidget import TimeEditorWidget
from opencmiss.zincwidgets.fieldlisteditorwidget import FieldListEditorWidget

class ArgonViewerWidget(QtWidgets.QWidget):

    def __init__(self, model, parent=None):
        super(ArgonViewerWidget, self).__init__(parent)
        self._ui = Ui_ArgonViewerWidget()
        self._ui.setupUi(self)

        self._ui.sceneviewerwidget.setContext(model.getContext())
        self._model = model
        # self._scene = self._region.getScene()
        self._ui.sceneviewerwidget.graphicsInitialized.connect(self._graphicsInitialized)

        self._callback = None

        self._makeConnections()

    def _graphicsInitialized(self):
        """
        Callback for when SceneviewerWidget is initialised
        """
        self._sceneChanged()
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setTransparencyMode(sceneviewer.TRANSPARENCY_MODE_SLOW)
            # self._autoPerturbLines()
            sceneviewer.viewAll()

    def _sceneChanged(self):
        """
        Set custom scene from model.
        """
        sceneviewer = self._ui.sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            self._model.createGraphics()
            # sceneviewer.setScene(self._model.getScene())
            # self._refreshGraphics()

    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        self._callback()

