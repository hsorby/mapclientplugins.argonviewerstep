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
from opencmiss.zinc.streamscene import StreaminformationScene 
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
        self._location = os.path.join(location, identifier)
        self._identifier = identifier
        # self._initGraphicsModules()
        self._document = ArgonDocument()
        self._document.initialiseVisualisationContents()
        self._prefix = "Argon"
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

    def getDocument(self):
        return self._document
        
    def _initGraphicsModules(self):
        context = self.getContext()
        self._materialmodule = context.getMaterialmodule()

    def setSceneviewerState(self, view, state):
        view.readDescription(json.dumps(state))

    def getSceneviewerState(self, view):
        d = json.loads(view.writeDescription())
        return d

    def getOutputModelFileNameStem(self):
        return self._location

    def getOutputModelFileName(self):
        return self._location# + ".argon"

    def save(self):
        # make model sources relative to current location if possible
        # note that sources on different windows drives have absolute paths
        base_path = os.path.dirname(self._location)
        state = self._document.serialize(base_path)
        with open(self._location, 'w') as f:
            f.write(state)

    def done(self,view):
        print("create graphics")
        self.exportViewJson(view)
        self.exportWebGLJson()
        self.save()

    def getIdentifier(self):
        return self._identifier

    def _getVisibility(self, graphicsName):
        return self._settings[graphicsName]

    def _setVisibility(self, graphicsName, show):
        self._settings[graphicsName] = show
        graphics = self.getScene().findGraphicsByName(graphicsName)
        graphics.setVisibilityFlag(show)

    def createGraphics(self):
        print("create graphics",self._document.getRootRegion().getZincRegion().getScene())
        streaminformationScene = self.getScene().createStreaminformationScene()
        print("create graphics",streaminformationScene)

        streaminformationScene.setIOFormat(StreaminformationScene.IO_FORMAT_THREEJS)
        streaminformationScene.createStreamresourceFile("threejs.json")
        
        self.getScene().write(streaminformationScene)
        print(streaminformationScene)

    def getScene(self):
        print("create graphics scene")
        return self._document.getRootRegion().getZincRegion().getScene()
        
    def exportViewJson(self,view):
        '''Export sceneviewer parameters to JSON format'''
        sceneviewerState = self.getSceneviewerState(view)
        viewData = {}
        viewData['farPlane'] = sceneviewerState["FarClippingPlane"]
        viewData['nearPlane'] = sceneviewerState["NearClippingPlane"]
        viewData['eyePosition'] = sceneviewerState["EyePosition"]
        viewData['targetPosition'] = sceneviewerState["LookatPosition"]
        viewData['upVector'] = sceneviewerState["UpVector"]
        f = open(self._prefix + '_view' + '.json', 'w+')
        json.dump(viewData, f)
        f.close()

    def exportWebGLJson(self):
        '''
        Export graphics into JSON format, one json export represents one
        surface graphics.
        '''
        scene = self.getScene()
        sceneSR = scene.createStreaminformationScene()
        sceneSR.setIOFormat(sceneSR.IO_FORMAT_THREEJS)
        '''
        output frames of the deforming heart between time 0 to 1,
        this matches the number of frame we have read in previously
        '''
        # sceneSR.setNumberOfTimeSteps(self._numberOfTimeSteps)
        sceneSR.setNumberOfTimeSteps(10)
        sceneSR.setInitialTime(0.0)
        sceneSR.setFinishTime(1.0)
        ''' we want the geometries and colours change overtime '''
        sceneSR.setOutputTimeDependentVertices(1)
        sceneSR.setOutputTimeDependentColours(1)
        number = sceneSR.getNumberOfResourcesRequired()
        resources = []
        '''Write out each graphics into a json file which can be rendered with ZincJS'''
        for i in range(number):
            resources.append(sceneSR.createStreamresourceMemory())
        scene.write(sceneSR)
        '''Write out each resource into their own file'''
        for i in range(number):
            f = None
            if i == 0:
                f = open(self._prefix + '_' + 'metadata.json', 'w+')
            else:
                f = open(self._prefix + '_' + str(i) + '.json', 'w+')
            buffer = resources[i].getBuffer()[1].decode()
            
            if i == 0:
                for j in range(number-1):
                    '''
                    IMPORTANT: the replace name here is relative to your html page, so adjust it
                    accordingly.
                    '''
                    # viewData = "{\"Type\":\"View\", \n \"URL\" : %s}"%(self._prefix + '_view' + '.json')
                    # buffer += viewData
                    replaceName = '' + self._prefix + '_' + str(j+1) + '.json'
                    old_name = 'memory_resource'+ '_' + str(j+2)
                    print(buffer)
                    print(type(buffer))
                    buffer = buffer.replace(old_name, replaceName)
                viewObj =    {
	                "Type": "View",
	                "URL": self._prefix + '_view' + '.json'
                }
                obj = json.loads(buffer)
                obj.append(viewObj)
                buffer = json.dumps(obj)
            f.write(buffer)
            f.close()    