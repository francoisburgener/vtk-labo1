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

    sphereActor = vtk.vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.SetProperty(property);
    sphereActor.SetPosition(position)

    return sphereActor


def cone(height, center, radius, resolution, color, position):
    cone = vtk.vtkConeSource()
    cone.SetCenter(center)
    cone.SetHeight(height)
    cone.SetRadius(radius)
    cone.SetResolution(resolution)

    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(cone.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(color)

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.SetProperty(property);
    coneActor.SetPosition(position)

    return coneActor


headActor = sphere(0.7, [-2.2, 0, 0], 30, [1.0, 1.0, 1.0], [0, 0, 0])
bodyActor = sphere(1, [0, 0, 0], 30, [1.0, 1.0, 1.0], [0, 0, 0])

eyeActor = sphere(0.1, [0, 0, 0], 30,  [0.0, 0.0, 0.0], [0, 6, 0])
eye2Actor = sphere(0.1, [0, 0, 0],  30, [0.0, 0.0, 0.0],  [0, -2, 0])

noseActor = cone(0.3, [0, 1.4, 0], 0.1, 30, [1, 0.678, 0.121], [0, 0, 0])  # Normalized decimal RGB
noseActor.RotateZ(-90)

cam = vtk.vtkCamera()
cam.SetFocalPoint(0, 0, 1.5)
cam.SetViewUp(0, 0, 0)
cam.SetPosition(0, 0, 12)

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

# Move head to body
for i in range(0, 40):
    time.sleep(0.03)
    j = (i * 0.0175) * -1;
    headActor.SetPosition(0, j, 0)
    renWin.Render()


# Move the nove and place to the head
for i in range(0, 90):
    time.sleep(0.03)
    noseActor.RotateX(1)
    renWin.Render()

for i in range(0, 90):
    time.sleep(0.03)
    noseActor.RotateZ(1)
    renWin.Render()

for i in range(0, 90):
    time.sleep(0.03)
    j = (i * 0.0175) * -1;
    noseActor.SetPosition(0, 0, 0.8)
    renWin.Render()

# Setup eyes
