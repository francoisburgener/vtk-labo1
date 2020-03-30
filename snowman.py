import vtk
import time


def sphere(radius, center, resolution, color, position):
    sphere = vtk.vtkSphereSource()
    sphere.SetCenter(center)
    sphere.SetRadius(radius)
    sphere.SetThetaResolution(resolution)

    sphereMapper = vtk.vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphere.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(color)
    # property.SetDiffuse(0.6)
    # property.SetSpecular(0.4)
    # property.SetSpecularPower(0.6)

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
    # property.SetDiffuse(0.7)
    # property.SetSpecular(0.4)
    # property.SetSpecularPower(20)

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.SetProperty(property);
    coneActor.SetPosition(position)

    return coneActor


headActor = sphere(0.7, [-2.2, 0, 0], 30, [1.0, 1.0, 1.0], [0, 0, 0])
bodyActor = sphere(1, [0, 0, 0], 30, [1.0, 1.0, 1.0], [0, 0, 0])

eyeActor = sphere(0.1, [0, 0, 0], 30,  [0.0, 0.0, 0.0], [0, 6, 0])
eye2Actor = sphere(0.1, [0, 0, 0],  30, [0.0, 0.0, 0.0],  [0, -2, 0])

noseActor = cone(0.3, 0.1, 30, [1, 0.678, 0.121], [2.2, 0, 0])  # Normalized decimal RGB
noseActor.RotateZ(-90)

cam = vtk.vtkCamera()
cam.SetFocalPoint(0, 0, 1.5)
cam.SetViewUp(0, 0, 0)
cam.SetPosition(0, 0, 12)
# cam.ParallelProjectionOn()
# cam.SetParallelScale(5)

ren = vtk.vtkRenderer()
ren.AddActor(headActor)
ren.AddActor(bodyActor)

ren.AddActor(noseActor)

ren.AddActor(eyeActor)
ren.AddActor(eye2Actor)

ren.SetBackground(0.988, 0.843, 0.854)
ren.SetActiveCamera(cam)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(720, 720)

# Rotate 90 degrees
for i in range(0, 90):
    time.sleep(0.03)

    headActor.RotateZ(-1)
    renWin.Render()

for i in range(0, 1400):
    time.sleep(0.03)

    renWin.Render()
    # ren.GetActiveCamera().Azimuth(1)
