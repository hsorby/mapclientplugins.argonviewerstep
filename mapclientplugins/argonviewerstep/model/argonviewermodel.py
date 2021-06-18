"""
Geometric fit model adding visualisations to github.com/ABI-Software/scaffoldfitter
"""
import os
import json
from opencmiss.utils.maths.vectorops import add, axis_angle_to_rotation_matrix, euler_to_rotation_matrix, matrix_mult, rotation_matrix_to_euler
from opencmiss.utils.zinc.finiteelement import evaluateFieldNodesetRange
from opencmiss.utils.zinc.general import ChangeManager
from opencmiss.zinc.field import Field, FieldFindMeshLocation
from opencmiss.zinc.glyph import Glyph
from opencmiss.zinc.graphics import Graphics
from opencmiss.zinc.material import Material
from opencmiss.zinc.node import Node
from opencmiss.zinc.scenecoordinatesystem import SCENECOORDINATESYSTEM_NORMALISED_WINDOW_FIT_LEFT
from opencmiss.zinc.scenefilter import Scenefilter
from opencmiss.zinc.result import RESULT_OK
from opencmiss.argon.core.argondocument import ArgonDocument
from opencmiss.argon.core.argonlogger import ArgonLogger


class ArgonViewerModel(object):
    """
    Geometric fit model adding visualisations to github.com/ABI-Software/scaffoldfitter
    """

    def __init__(self, inputArgonDocFile, location, identifier):
        """
        :param location: Path to folder for mapclient step name.
        """
        # self._fitter = Fitter(inputZincModelFile, inputZincDataFile)
        self._location = os.path.join(location, identifier)
        self._identifier = identifier
        # self._initGraphicsModules()
        self._settings = {
            "displayAxes" : True,
            "displayMarkerDataPoints" : True,
            "displayMarkerDataNames" : False,
            "displayMarkerDataProjections" : True,
            "displayMarkerPoints" : True,
            "displayMarkerNames" : False,
            "displayDataPoints" : True,
            "displayDataProjections" : True,
            "displayDataProjectionPoints" : True,
            "displayNodePoints" : False,
            "displayNodeNumbers" : False,
            "displayNodeDerivatives" : False,
            # "displayNodeDerivativeLabels" : nodeDerivativeLabels[0:3],
            "displayElementNumbers" : False,
            "displayElementAxes" : False,
            "displayLines" : True,
            "displayLinesExterior" : False,
            "displaySurfaces" : True,
            "displaySurfacesExterior" : True,
            "displaySurfacesTranslucent" : True,
            "displaySurfacesWireframe" : False
        }
        # self._loadSettings()
        # self._fitter.load()
        self._document = ArgonDocument()
        self._document.initialiseVisualisationContents()
        self.load(inputArgonDocFile)

    def load(self, filename):
        """
        Loads the named Neon file and on success sets filename as the current location.
        Emits documentChange separately if new document loaded, including if existing document cleared due to load failure.
        :return  True on success, otherwise False.
        """
        model_changed = False
        try:
            with open(filename, 'r') as f:
                state = f.read()
                model_changed = True
                self._location = None
                if self._document is not None:
                    self._document.freeVisualisationContents()
                self._document = ArgonDocument()
                self._document.initialiseVisualisationContents()
                # set current directory to path from file, to support scripts and fieldml with external resources
                path = os.path.dirname(filename)
                os.chdir(path)
                self._document.deserialize(state)
                self._location = filename
                # self.documentChanged.emit()
                return True
        except (NeonError, IOError, ValueError) as e:
            ArgonLogger.getLogger().error("Failed to load Neon model " + filename + ": " + str(e))
        except:
            ArgonLogger.getLogger().error("Failed to load Neon model " + filename + ": Unknown error")
        if model_changed:
            self.new()  # in case document half constructed; emits documentChanged
        return False

    def getContext(self):
        if self._document:
            return self._document.getZincContext()
        return None

    def _initGraphicsModules(self):
        context = self.getContext()
        self._materialmodule = context.getMaterialmodule()

    def _getFitSettingsFileName(self):
        return self._location + "-settings.json"

    def _getDisplaySettingsFileName(self):
        return self._location + "-display-settings.json"

    def _saveSettings(self):
        with open(self._getFitSettingsFileName(), "w") as f:
            pass
        with open(self._getDisplaySettingsFileName(), "w") as f:
            f.write(json.dumps(self._settings, sort_keys=False, indent=4))

    def done(self):
        self._saveSettings()

    def getIdentifier(self):
        return self._identifier

    def _getVisibility(self, graphicsName):
        return self._settings[graphicsName]

    def _setVisibility(self, graphicsName, show):
        self._settings[graphicsName] = show
        graphics = self.getScene().findGraphicsByName(graphicsName)
        graphics.setVisibilityFlag(show)

    def createGraphics(self):
        pass

    def getScene(self):
        pass