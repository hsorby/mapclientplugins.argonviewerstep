Argon Viewer Step
=================

The **Argon Viewer Step** is part of the software that is used in the collection of tools used for mapping data to scaffolds.

.. note::

   This project is under active development.

Overview
--------

The **Argon Viewer Step** is a general purpose visualization tool that displays and manages `Zinc` scenes. 
It uses the `Zinc Widgets` library to provide graphical user interfaces for the underlying `Zinc` actions.

The input of **Argon Viewer Step** is a `Zinc library` compatible EX file, or an Argon file.
The output of this tool is an Argon file, which can be used to generate WebGL files for visualization.

This document describes how to set up and use the **Argon Viewer** user interface in mapping tools.
The reading and writing process of an argon document is managed by the underlying `argon library`, together with the `Zinc library` which handles model representation and computation.

Workflow Connections
--------------------

As shown in :numref:`fig-argon-viewer-step-workflow`, the **Argon Viewer Step** uses 1 input:

1. A **File Chooser** to read from a `Zinc library` compatible EX file or an Argon file.

It produces 1 output which may be piped to other workflow steps:

1. An argon structure JSON file, can be used to generate WebGL files for visualization.

.. _fig-argon-viewer-step-workflow:

.. figure:: _images/argon-viewer-step-workflow.png
   :figwidth: 40%
   :align: center

   **Argon Viewer** workflow connections.
   
Whether you use the output in a further workflow step or not, on completion of the workflow step the output is written to a file in the workflow folder under the same name as the step with extension "-backup-document.json".

Background
----------

This **Argon Viewer**  is a bundle of **Zinc Widgets**.

It includes:

1. Material Editor Widget;
2. Model Sources Widget;
3. Time Editor Widget;
4. Tessellation Editor Widget;
5. Spectrum Editor Widget;
6. Scene Editor Widget;
7. Sceneviewer Editor Widget;
8. Field Editor Widget;
9. Region Editor Widget;
10. Logger Editor Widget;
11. Console Editor Widget.

Detailed documentation on each of these widgets can be found at `Zinc Widgets Documentation <https://abi-mapping-tools.readthedocs.io/en/latest/cmlibs.widgets/docs/index.html>`_.

Install
-------

Requirements
^^^^^^^^^^^^

python >= 3.6

mapclient >= 0.18

cmlibs.zinc >= 3.99

cmlibs.widgets >= 2.3

cmlibs.argon >= 0.4

Usage
-----

To illustrate the use of *Argon Viewer Step* we will use the `multi view example workflow <https://github.com/mapclient-workflows/argon-viewer-docs-example>`_ (`download zip <https://github.com/mapclient-workflows/argon-viewer-docs-example/archive/refs/heads/main.zip>`_), which uses five meshes to illustrate how a mutliple viewing window can be used.
The main input file of Argon Viewer Step in this workflow is `multi_scene.argon`, with multiple model sources `sphere.exf`, `tube.exf`, `cube.exf`, `bifurcation.exf` and `heart.exfile`.
The output of the Argon Viewer Step is the `argon_viewer-backup-document.json`, which also is the input of *Argon Scene Expoter Step* after it.
This final output of this workflow are WebGL files in the `webGLOutput` folder.

Initial
^^^^^^^
:numref:`fig-argon-viewer-initial` shows the **Argon Viewer** user interface just after loading. 

.. _fig-argon-viewer-initial:

.. figure:: _images/argon-viewer-initial.png
   :align: center

   Initial **Argon Viewer** user interface after loading.

The widgets tabs at the top of the central widget, lists the available zinc widgets. 
In the middle of the user interface is the main widget where scene viewer widgets are shown.
Argon Viewer allows the user to create multiple scene viewers and each viewer can have a different number of sceneviewer widgets.
By clicking the `Add View` button in the middle (or the green plus button on the top right of the scene viewer widget), a *Scene Layout Chooser Dialog* will popup letting the user select a layout for the view.

:numref:`fig-scene-layout-chooser` shows the *Scene Layout Chooser Dialog*, which is used to select the type of scene viewer widget to add.

.. _fig-scene-layout-chooser:

.. figure:: _images/scene-layout-chooser.png
   :figwidth: 40%
   :align: center

   **Scene Layout Chooser Dialog** for selecting view layout.

There are two types of layout that an be selected.
One, a full layout with only one sceneviewer widget for single view, and two, a grid layout with four small sceneviewer widgets for multiple views.

Single View
^^^^^^^^^^^
:numref:`fig-argon-viewer-single-view` shows the **Argon Viewer Step** user interface with single sceneviewer.

.. _fig-argon-viewer-single-view:

.. figure:: _images/argon-viewer-single-view.png
   :align: center

   **Argon Viewer** user interface for single view.

The *Single View* is the standard view, it contains a single sceneviewer for viewing the scene.

Multi-Views
^^^^^^^^^^^

:numref:`fig-argon-viewer-multiviews` shows the **Argon Viewer Step** user interface with multiple views.

.. _fig-argon-viewer-multiviews:

.. figure:: _images/argon-viewer-multiviews.png
   :align: center

   **Argon Viewer** user interface for multiple Views.

*Multiple Views* allows the user to view multiple scenes at the same time.
A purple border highlights the currently active scene viewer.
The active scene viewer is the target for widgets such as the *Sceneviewer Editor*.
The *Sceneviewer Editor* shows the current status information of the currently active scene viewer. 
The content of the currently selected scene viewer can be edited by selecting regions in the *Sceneviewer Editor* widget, this allows the user to view scenes from different regions or view the scene from a different angle at the same time.

Clicking *Done* saves the current settings into an Argon file before moving to the next workflow step.
