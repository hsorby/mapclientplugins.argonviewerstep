from PySide2 import QtCore, QtWidgets

from mapclientplugins.argonviewerstep.ui.ui_argonviewerwidget import Ui_ArgonViewerWidget
from opencmiss.zincwidgets.regioneditorwidget import RegionEditorWidget
from opencmiss.zincwidgets.modelsourceseditorwidget import ModelSourcesEditorWidget
from opencmiss.zincwidgets.sceneviewereditorwidget import SceneviewerEditorWidget
from opencmiss.zincwidgets.sceneviewerwidget import SceneviewerWidget
from opencmiss.zincwidgets.sceneeditorwidget import SceneEditorWidget
from opencmiss.zincwidgets.spectrumeditorwidget import SpectrumEditorWidget
from opencmiss.zincwidgets.tessellationeditorwidget import TessellationEditorWidget
from opencmiss.zincwidgets.timeeditorwidget import TimeEditorWidget
from opencmiss.zincwidgets.fieldlisteditorwidget import FieldListEditorWidget

class ArgonViewerWidget(QtWidgets.QMainWindow):

    def __init__(self, model, parent=None):
        super(ArgonViewerWidget, self).__init__(parent)
        self._ui = Ui_ArgonViewerWidget()
        self._ui.setupUi(self)

        self._visualisation_view_state_update_pending = False

        # List of possible views
        self._sceneviewerwidget = SceneviewerWidget(self)
        self._visualisation_view_ready = False

        self._view_states = {self._sceneviewerwidget: ''}
        # self._view_states[self._problem_view] = ''
        # self._view_states[self._simulation_view] = ''

        view_list = [self._sceneviewerwidget]

        self._location = None  # The last location/directory used by the application
        self._current_view = None


        self._sceneviewerwidget.setContext(model.getContext())
        self._model = model
        # self._scene = self._region.getScene()
        self._sceneviewerwidget.graphicsInitialized.connect(self._graphicsInitialized)

        self._toolbar = self._ui.toolBar

        # dockLayout = QtWidgets.QVBoxLayout()
        # dockLayout.setMenuBar(tb)
        # dockContent = QtWidgets.QWidget()
        # dockContent.setLayout(dockLayout)
        # view_list.append(dockContent)
        # self._ui.verticalLayout.addWidget(self._toolbar)

        # yourDockWidget.setWidget(dockContent);

        self._callback = None

        self._makeConnections()
        self._setupEditors()

        self._registerEditors()

        self._setupViews(view_list)
        # self._setupOtherWindows()

        # self._registerOtherWindows()

        # print(self.findMainWindow())
        self._addDockWidgets()

        # Set the undo redo stack state
        # self._undoRedoStack.push(CommandEmpty())
        # self._undoRedoStack.clear()

        # self._updateUi()

        # self._readSettings()

        self._dock_widgets = []

    def getName(self):
        return self._name

    def setZincContext(self, zincContext):
        raise NotImplementedError()

    def getDependentEditors(self):
        return self._dock_widgets

    def registerDependentEditor(self, editor):
        '''
        Add the given editor to the list of dependent editors for
        this view.
        '''
        self._dock_widgets.append(editor)

    def _graphicsInitialized(self):
        """
        Callback for when SceneviewerWidget is initialised
        """
        self._sceneChanged()
        sceneviewer = self._sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            sceneviewer.setTransparencyMode(sceneviewer.TRANSPARENCY_MODE_SLOW)
            # self._autoPerturbLines()
            sceneviewer.viewAll()

    def _sceneChanged(self):
        """
        Set custom scene from model.
        """
        sceneviewer = self._sceneviewerwidget.getSceneviewer()
        if sceneviewer is not None:
            self._model.createGraphics()
            # sceneviewer.setScene(self._model.getScene())
            # self._refreshGraphics()

    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)
        self._sceneviewerwidget.graphicsInitialized.connect(self._visualisationViewReady)        

    def _addDockWidgets(self):
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.LeftDockWidgetArea), self.dockWidgetTessellationEditor)
        self.tabifyDockWidget(self.dockWidgetTessellationEditor, self.dockWidgetSpectrumEditor)
        self.tabifyDockWidget(self.dockWidgetSpectrumEditor, self.dockWidgetSceneEditor)
        self.tabifyDockWidget(self.dockWidgetSceneEditor, self.dockWidgetModelSourcesEditor)
        self.tabifyDockWidget(self.dockWidgetModelSourcesEditor, self.dockWidgetRegionEditor)
        self.tabifyDockWidget(self.dockWidgetRegionEditor, self.dockWidgetSceneviewerEditor)
        self.tabifyDockWidget(self.dockWidgetSceneviewerEditor, self.dockWidgetFieldEditor)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(QtCore.Qt.BottomDockWidgetArea), self.dockWidgetTimeEditor)

    def _setupEditors(self):

        self.dockWidgetRegionEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetRegionEditor.setWindowTitle('Region Editor')
        self.dockWidgetRegionEditor.setObjectName("dockWidgetRegionEditor")
        self.dockWidgetContentsRegionEditor = RegionEditorWidget()
        self.dockWidgetContentsRegionEditor.setObjectName("dockWidgetContentsRegionEditor")
        self.dockWidgetRegionEditor.setWidget(self.dockWidgetContentsRegionEditor)
        self.dockWidgetRegionEditor.setHidden(True)

        self.dockWidgetModelSourcesEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetModelSourcesEditor.setWindowTitle('Model Sources Editor')
        self.dockWidgetModelSourcesEditor.setObjectName("dockWidgetModelSourcesEditor")
        self.dockWidgetContentsModelSourcesEditor = ModelSourcesEditorWidget()
        self.dockWidgetContentsModelSourcesEditor.setObjectName("dockWidgetContentsModelSourcesEditor")
        self.dockWidgetModelSourcesEditor.setWidget(self.dockWidgetContentsModelSourcesEditor)
        self.dockWidgetModelSourcesEditor.setHidden(True)

        self.dockWidgetSceneEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetSceneEditor.setWindowTitle('Scene Editor')
        self.dockWidgetSceneEditor.setObjectName("dockWidgetSceneEditor")
        self.dockWidgetContentsSceneEditor = SceneEditorWidget()
        self.dockWidgetContentsSceneEditor.setObjectName("dockWidgetContentsSceneEditor")
        self.dockWidgetSceneEditor.setWidget(self.dockWidgetContentsSceneEditor)
        self.dockWidgetSceneEditor.setHidden(True)
        
        self.dockWidgetSceneviewerEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetSceneviewerEditor.setWindowTitle('Sceneviewer Editor')
        self.dockWidgetSceneviewerEditor.setObjectName("dockWidgetSceneviewerEditor")
        self.dockWidgetContentsSceneviewerEditor = SceneviewerEditorWidget(self.dockWidgetSceneviewerEditor)
        self.dockWidgetContentsSceneviewerEditor.setObjectName("dockWidgetContentsSceneviewerEditor")
        self.dockWidgetSceneviewerEditor.setWidget(self.dockWidgetContentsSceneviewerEditor)
        self.dockWidgetSceneviewerEditor.setHidden(True)
        self.dockWidgetSceneviewerEditor.visibilityChanged.connect(self.dockWidgetContentsSceneviewerEditor.setEnableUpdates)

        self.dockWidgetSpectrumEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetSpectrumEditor.setWindowTitle('Spectrum Editor')
        self.dockWidgetSpectrumEditor.setObjectName("dockWidgetSpectrumEditor")
        self.dockWidgetContentsSpectrumEditor = SpectrumEditorWidget(self.dockWidgetSpectrumEditor)
        self.dockWidgetContentsSpectrumEditor.setObjectName("dockWidgetContentsSpectrumEditor")
        self.dockWidgetSpectrumEditor.setWidget(self.dockWidgetContentsSpectrumEditor)
        self.dockWidgetSpectrumEditor.setHidden(True)

        self.dockWidgetTessellationEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetTessellationEditor.setWindowTitle('Tessellation Editor')
        self.dockWidgetTessellationEditor.setObjectName("dockWidgetTessellationEditor")
        self.dockWidgetContentsTessellationEditor = TessellationEditorWidget()
        self.dockWidgetContentsTessellationEditor.setObjectName("dockWidgetContentsTessellationEditor")
        self.dockWidgetTessellationEditor.setWidget(self.dockWidgetContentsTessellationEditor)
        self.dockWidgetTessellationEditor.setHidden(True)

        self.dockWidgetTimeEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetTimeEditor.setWindowTitle('Time Editor')
        self.dockWidgetTimeEditor.setObjectName("dockWidgetTimeEditor")
        self.dockWidgetContentsTimeEditor = TimeEditorWidget()
        self.dockWidgetContentsTimeEditor.setObjectName("dockWidgetContentsTimeEditor")
        self.dockWidgetTimeEditor.setWidget(self.dockWidgetContentsTimeEditor)
        self.dockWidgetTimeEditor.setHidden(True)
        
        self.dockWidgetFieldEditor = QtWidgets.QDockWidget(self)
        self.dockWidgetFieldEditor.setWindowTitle('Field Editor')
        self.dockWidgetFieldEditor.setObjectName("dockWidgetFieldEditor")
        self.dockWidgetContentsFieldEditor = FieldListEditorWidget()
        self.dockWidgetContentsFieldEditor.setObjectName("dockWidgetContentsFieldEditor")
        self.dockWidgetFieldEditor.setWidget(self.dockWidgetContentsFieldEditor)
        self.dockWidgetFieldEditor.setHidden(True)

    def _registerEditors(self):
        self._registerEditor(self.dockWidgetRegionEditor)
        self._registerEditor(self.dockWidgetModelSourcesEditor)
        self._registerEditor(self.dockWidgetSceneEditor)
        self._registerEditor(self.dockWidgetSceneviewerEditor)
        self._registerEditor(self.dockWidgetSpectrumEditor)
        self._registerEditor(self.dockWidgetTessellationEditor)
        self._registerEditor(self.dockWidgetTimeEditor)
        self._registerEditor(self.dockWidgetFieldEditor)

        #self._toolbar.addSeparator()

    def _registerEditor(self, editor):
        self._toolbar.addAction(editor.toggleViewAction())
        # view.registerDependentEditor(editor)


    def _getEditorAction(self, action_name):
        action = None
        actions = self._toolbar.actions()
        existing_actions = [a for a in actions if a.text() == action_name]
        if existing_actions:
            action = existing_actions[0]
        return action

    def _setupViews(self, views):
        action_group = QtWidgets.QActionGroup(self)
        zincContext = self._model.getContext()
        print(zincContext)
        for v in views:
            self._ui.viewStackedWidget.addWidget(v)
            v.setContext(zincContext)

            # action_view = QtWidgets.QAction(v.getName(), self)
            # action_view.setData(v)
            # action_view.setCheckable(True)
            # action_view.setActionGroup(action_group)
            # action_view.triggered.connect(self._viewTriggered)
            # self._toolbar.addAction(action_view)

        self._toolbar.addSeparator()

    def _visualisationViewReady(self):
        self._visualisation_view_ready = True
        if self._visualisation_view_state_update_pending:
            self._restoreSceneviewerState()


    def _restoreSceneviewerState(self):
        # document = self._model.getDocument()
        # sceneviewer_state = document.getSceneviewer().serialize()
        # self._sceneviewerwidget.setSceneviewerState(sceneviewer_state)
        self.dockWidgetContentsSceneviewerEditor.setSceneviewer(self._sceneviewerwidget)
        self._visualisation_view_state_update_pending = False

    def _addSceneEditorButtonClicked(self):
        self.dockWidgetSceneEditor.setHidden(False)

    def _addSceneViewerEditorButtonClicked(self):
        self.dockWidgetSceneviewerEditor.setHidden(False)

    def _preChangeView(self):
        current_view = self._ui.viewStackedWidget.currentWidget()
        dependent_editors = current_view.getDependentEditors()
        view_state = self.saveState(VERSION_MAJOR)
        self._view_states[current_view] = view_state

        for ed in dependent_editors:
            ed.setHidden(True)

        action_name = getEditorMenuName(current_view)
        action = self._getEditorAction(action_name)
        if action is not None:
            menu = action.menu()
            menu.setEnabled(False)

    def _changeView(self, view):
        self._ui.viewStackedWidget.setCurrentWidget(view)

    def _postChangeView(self):
        current_view = self._ui.viewStackedWidget.currentWidget()
        view_state = self._view_states[current_view]
        # self.restoreState(view_state, VERSION_MAJOR)

        action_name = getEditorMenuName(current_view)
        action = self._getEditorAction(action_name)
        if action is not None:
            menu = action.menu()
            menu.setEnabled(True)

    def _viewTriggered(self):
        v = self.sender().data()
        self._preChangeView()
        self._changeView(v)
        self._postChangeView()

    def registerDoneExecution(self, callback):
        self._callback = callback

    def _doneButtonClicked(self):
        self._callback()
