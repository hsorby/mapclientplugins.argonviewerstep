"""
Geometric fit model adding visualisations to github.com/ABI-Software/scaffoldfitter
"""
import os
import json

from cmlibs.argon.argondocument import ArgonDocument
from cmlibs.argon.argonlogger import ArgonLogger
from cmlibs.zinc.result import RESULT_OK
from mapclientplugins.argonviewerstep.model.utilities import is_argon_file, is_exf_file


class ArgonViewerModel(object):
    """
    Geometric fit model adding visualisations to github.com/ABI-Software/scaffoldfitter
    """

    def __init__(self):
        """
        """
        self._document = None
        self._file_sources = []

    def setSources(self, sources):
        self._file_sources = sources

    def getSources(self):
        return self._file_sources

    def load(self, filename):
        """
        Loads the named Neon file and on success sets filename as the current location.
        Emits documentChange separately if new document loaded, including if existing document cleared due to load failure.
        :return  True on success, otherwise False.
        """
        argon_file = None
        exf_file = None
        if is_argon_file(filename):
            argon_file = filename
        elif is_exf_file(filename):
            exf_file = filename
        else:
            return False

        if exf_file is not None:
            return self._load_exf(exf_file)

        return self._load_argon(argon_file)

    def _load_exf(self, filename):
        self.new()
        context = self._document.getZincContext()
        region = context.getDefaultRegion()
        return region.readFile(filename) == RESULT_OK

    def _load_argon(self, filename):
        self.new()
        with open(filename) as f:
            state = f.read()

        current_dir = os.getcwd()
        file_dir = os.path.dirname(filename)
        os.chdir(file_dir)
        self._document.deserialize(state)
        os.chdir(current_dir)

        ArgonLogger.getLogger()
        return True

    def new(self):
        self._document = ArgonDocument()
        self._document.initialiseVisualisationContents()
        # self._document.

    def getContext(self):
        if self._document:
            return self._document.getZincContext()
        return None

    def getDocument(self):
        return self._document

    def _initGraphicsModules(self):
        context = self.getContext()
        self._materialmodule = context.getMaterialmodule()

    def setSceneviewerState(self, view, state):
        view.readDescription(json.dumps(state))

    def _getVisibility(self, graphicsName):
        return self._settings[graphicsName]

    def _setVisibility(self, graphicsName, show):
        self._settings[graphicsName] = show
        graphics = self.getScene().findGraphicsByName(graphicsName)
        graphics.setVisibilityFlag(show)

    def getScene(self):
        return self._document.getRootRegion().getZincRegion().getScene()
