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


def rotate_camera(render, render_window, direction, axe, iteration):
    for _ in range(0, iteration):
        time.sleep(FRAMERATE/2)

        if axe == 'azimuth':
            render.GetActiveCamera().Roll(direction)
        elif axe == 'roll':
            render.GetActiveCamera().Azimuth(direction)
        elif axe == 'elevation':
            render.GetActiveCamera().Elevation(direction)
        render_window.Render()


# Start
# Declaration of Actors

headActor = sphere(radius=0.7, center=[-2.2, 0, 0], resolution=30, color=[1.0, 1.0, 1.0], position=[0, 0, 0])
bodyActor = sphere(radius=1, center=[0, 0, 0], resolution=30, color=[1.0, 1.0, 1.0], position=[0, 0, 0])

eyeActor = sphere(radius=0.125, center=[0, 0, 0], resolution=30, color=[0.0, 0.0, 0.0], position=[0.25, 1.6, 0.625])
eye2Actor = sphere(radius=0.125, center=[0, 0, 0], resolution=30, color=[0.0, 0.0, 0.0], position=[-0.25, 1.6, 0.625])

noseActor = cone(height=0.3, center=[0, 2.2, 0], radius=0.1, resolution=30, color=[1, 0.678, 0.121],
                 position=[0, 0, 0])  # Normalized decimal RGB

noseActor.RotateZ(-90)

# Camera

cam = vtk.vtkCamera()
cam.SetPosition(0, 0, 12)

ren = vtk.vtkRenderer()
ren.AddActor(headActor)
ren.AddActor(bodyActor)

ren.AddActor(noseActor)

ren.SetBackground(0.988, 0.843, 0.854)
ren.SetActiveCamera(cam)

# Setting up initial Azimuth
# ren.GetActiveCamera().Azimuth(90)

renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
renWin.SetSize(720, 720)

# Rotate 90 degrees Head
rotate_shape(shape_actor=headActor, render_object=renWin, axe='z', angle=90, direction=-1)

# Move head to body
translate_shape(shape_actor=headActor, render_object=renWin, vector=[0, -0.0175, 0], iteration=40)

# Rotate the nose in front of the body
rotate_shape(shape_actor=noseActor, render_object=renWin, axe='x', angle=90, direction=1)

# Sneaky move back the nose
translate_shape(shape_actor=noseActor, render_object=renWin, vector=[0, 0, -0.0175], iteration=50)

# Rotate nose to the head
rotate_shape(shape_actor=noseActor, render_object=renWin, axe='z', angle=90, direction=1)

# Place the nose to the head
translate_shape(shape_actor=noseActor, render_object=renWin, vector=[0, 0, 0.0175], iteration=100)

# Place eyes to the head
ren.AddActor(eyeActor)
ren.AddActor(eye2Actor)

renWin.Render()
# Rotation camera
rotate_camera(ren, renWin, 1, 'roll', 360)
rotate_camera(ren, renWin, 1, 'azimuth', 360)
rotate_camera(ren, renWin, 1, 'elevation', 60)
rotate_camera(ren, renWin, -1, 'elevation', 60)


# Move camera

for i in range(0, 1000):
    time.sleep(FRAMERATE)

# Setup eyes
