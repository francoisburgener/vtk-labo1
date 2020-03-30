import vtk
import time

FRAMERATE = 0.03


def sphere(radius, center, resolution, color, position):
    sphereSource = vtk.vtkSphereSource()
    sphereSource.SetCenter(center)
    sphereSource.SetRadius(radius)
    sphereSource.SetThetaResolution(resolution)

    sphereMapper = vtk.vtkPolyDataMapper()
    sphereMapper.SetInputConnection(sphereSource.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(color)

    sphereActor = vtk.vtkActor()
    sphereActor.SetMapper(sphereMapper)
    sphereActor.SetProperty(property);
    sphereActor.SetPosition(position)

    return sphereActor


def cone(height, center, radius, resolution, color, position):
    coneSource = vtk.vtkConeSource()
    coneSource.SetCenter(center)
    coneSource.SetHeight(height)
    coneSource.SetRadius(radius)
    coneSource.SetResolution(resolution)

    coneMapper = vtk.vtkPolyDataMapper()
    coneMapper.SetInputConnection(coneSource.GetOutputPort())

    property = vtk.vtkProperty()
    property.SetColor(color)

    coneActor = vtk.vtkActor()
    coneActor.SetMapper(coneMapper)
    coneActor.SetProperty(property);
    coneActor.SetPosition(position)

    return coneActor


def rotate_shape(shape_actor, render_object, axe, angle, direction):
    for _ in range(0, angle):
        time.sleep(FRAMERATE)

        if axe == 'z':
            shape_actor.RotateZ(direction)
        elif axe == 'x':
            shape_actor.RotateX(direction)
        elif axe == 'y':
            shape_actor.RotateY(direction)

        render_object.Render()


def translate_shape(shape_actor, render_object, vector, iteration):
    for _ in range(0, iteration):
        time.sleep(FRAMERATE)
        shape_actor.AddPosition(vector)
        render_object.Render()


# Start
# Declaration of Actors

headActor = sphere(0.7, [-2.2, 0, 0], 30, [1.0, 1.0, 1.0], [0, 0, 0])
bodyActor = sphere(1, [0, 0, 0], 30, [1.0, 1.0, 1.0], [0, 0, 0])

eyeActor = sphere(0.1, [0, 0, 0], 30,  [0.0, 0.0, 0.0], [0, 0, 0])
eye2Actor = sphere(0.1, [0, 0, 0],  30, [0.0, 0.0, 0.0],  [0, -2, 0])


noseActor = cone(0.3, [0, 2.2, 0], 0.1, 30, [1, 0.678, 0.121], [0, 0, 0])  # Normalized decimal RGB
noseActor.RotateZ(-90)

# Camera

cam = vtk.vtkCamera()
cam.SetPosition(0, 0, 12)

ren = vtk.vtkRenderer()
ren.AddActor(headActor)
ren.AddActor(bodyActor)

ren.AddActor(noseActor)


ren.AddActor(eyeActor)
ren.AddActor(eye2Actor)

ren.SetBackground(0.988, 0.843, 0.854)
ren.SetActiveCamera(cam)

ren.GetActiveCamera().Azimuth(90)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(720, 720)


# Rotate 90 degrees Head
rotate_shape(headActor, renWin, 'z', 90, -1)

# Move head to body
translate_shape(headActor, renWin, [0, -0.0175, 0], 40)

# Rotate the nose in front of the body
rotate_shape(noseActor, renWin, 'x', 90, 1)

# Sneaky move back the nose
translate_shape(noseActor, renWin, [0, 0, -0.0175], 50)

# Rotate nose to the head
rotate_shape(noseActor, renWin, 'z', 90, 1)

# Place the nose to the head
translate_shape(noseActor, renWin, [0, 0, 0.0175], 100)

# Place eyes to the head


for i in range (0,1000):
    time.sleep(FRAMERATE)



# Setup eyes
