import vtk
import time


def sphere(radius, resolution, color, position):
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter([3.0, 3.0, 3.0])
    sphere.SetRadius(radius)
    sphere.SetThetaResolution(resolution)

    sphereMapper = vtk.vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphere.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(color)
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)

    sphereActor = vtk.vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.SetProperty(property);
    sphereActor.SetPosition(position)

    return sphereActor


def cone(height, radius, resolution, color, position):
    cone = vtk.vtkConeSource()
    cone.SetHeight(height)
    cone.SetRadius(radius)
    cone.SetResolution(resolution)

    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(color)
    property.SetDiffuse(0.7)
    property.SetSpecular(0.4)
    property.SetSpecularPower(20)

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.SetProperty(property);
    coneActor.SetPosition(position)

    return coneActor


sphereActor1 = sphere(1, 30, [1.0, 0.3882, 0.2784], [0, 0, 0])
sphereActor2 = sphere(1.5, 30, [0.2, 0.63, 0.79], [0, 3, 0])
coneActor = cone(1.0, 0.2, 10, [0.2, 0.63, 0.79], [0, 10, 0])

ren1 = vtk.vtkRenderer()
ren1.AddActor(sphereActor1)
ren1.AddActor(sphereActor2)
ren1.AddActor(coneActor)
ren1.SetBackground(0.1, 0.2, 0.4)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren1)
renWin.SetSize(800, 800)

for i in range(0, 360):
    time.sleep(0.03)

    renWin.Render()
    ren1.GetActiveCamera().Azimuth(1)
