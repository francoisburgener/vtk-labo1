# VTK

## Example

These examples demonstrate some basic VTK concepts. They are organized in
increasing order of complexity. These examples are described in more detail
in the textbook "The Visualization Toolkit An Object-Oriented Approach to 3D
Graphics" Third Edition available for purchase from Kitware. The examples are
implemented in the programming languages C++, Tcl, Python, and Java. (Note:
in order to use Tcl, Python, and/or Java, you will need to compile with
wrapping on.)

- Step1 - A "Hello World" style example of a simple visualization pipeline
- Step2 - Adding observers to Step1 (i.e., processing events)
- Step3 - Rendering with multiple renderers
- Step4 - Modifying properties and transformations
- Step5 - Specifying a particular interaction style
- Step6 - Adding a 3D widget

Once you finish this mini-tutorial, you may wish to explore the other
VTK/Examples/ subdirectories. In particular, the VTK/Examples/Rendering
and VTK/Examples/VisualizationAlgorithms are worth exploring. The
subdirectory VTK/Examples/GUI has other 3D widget examples.

## Labo 1 - Bonhomme de neige

Le premier but de ce laboratoire est de vous familiariser avec VTK. Je vous demande d'en installer la version sous python, ce qui devrait être aussi simple que de taper "pip install vtk"

Une fois cette installation effectuée, je vous demande tout d'abord de 

- Regarder la video [Tiny Renderer en VTK](https://tinyurl.com/TinyRendererEnVTK) sur YouTube. Les codes qui y sont présentés sont disponibles sur [GitHub](https://github.com/VTK-HEIGVD/TinyRenderer-en-VTK). 
- Lire, exécuter et comprendre les codes coneN.py ci-dessous qui présentent une sorte de Hello World de VTK.

Le but de ce laboratoire est de vous familiariser avec les transformations appliquées aux acteurs et à la caméra de VTK. 

Vous devez ensuite écrire en python et vtk un programme qui affiche à l'écran l'équivalent de la video suivante. Utilisez des [vtkSphereSource](https://vtk.org/doc/nightly/html/classvtkSphereSource.html) pour les sphères et [vtkConeSource](https://vtk.org/doc/nightly/html/classvtkConeSource.html) pour le nez. Déplacez les morceaux du bonhomme de neige en manipulant les [vtkActor](https://vtk.org/doc/nightly/html/classvtkActor.html) de votre scène. Pour la fin de la video, déplacez la [vtkCamera](https://vtk.org/doc/nightly/html/classvtkCamera.html) et pas le bonhomme de neige. 