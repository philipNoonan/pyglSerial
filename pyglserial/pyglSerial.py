import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy as np
import imgui
from imgui.integrations.glfw import GlfwRenderer
from pathlib import Path
import time
import serial



def main():

    ser = serial.Serial('COM4', 9600)  # open serial port

    # initialize glfw
    if not glfw.init():
        return
    #glfw.window_hint(glfw.VISIBLE, False)    
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    #creating the window
    window = glfw.create_window(640, 480, "PyGLFlow", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)

    imgui.create_context()
    impl = GlfwRenderer(window)
    #           positions        colors          texture coords
    quad = [   -1.0, -1.0, 0.0,  1.0, 0.0, 0.0,  0.0, 0.0,
                1.0, -1.0, 0.0,  0.0, 1.0, 0.0,  1.0, 0.0,
                1.0,  1.0, 0.0,  0.0, 0.0, 1.0,  1.0, 1.0,
               -1.0,  1.0, 0.0,  1.0, 1.0, 1.0,  0.0, 1.0]

    quad = np.array(quad, dtype = np.float32)

    indices = [0, 1, 2,
               2, 3, 0]

    indices = np.array(indices, dtype= np.uint32)

    vertex_shader = (Path(__file__).parent / 'shaders/screenQuad.vert').read_text()

    fragment_shader = (Path(__file__).parent / 'shaders/screenQuad.frag').read_text()

    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    # set up VAO and VBO for full screen quad drawing calls
    VAO = glGenVertexArrays(1)
    glBindVertexArray(VAO)

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 128, quad, GL_STATIC_DRAW)

    EBO = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, EBO)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, 24, indices, GL_STATIC_DRAW)

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(12))
    glEnableVertexAttribArray(1)
    glVertexAttribPointer(2, 2, GL_FLOAT, GL_FALSE, 32, ctypes.c_void_p(24))
    glEnableVertexAttribArray(2)

    # make some default background color
    glClearColor(0.2, 0.3, 0.2, 1.0)



    while not glfw.window_should_close(window):

        w, h = glfw.get_framebuffer_size(window)
        glfw.poll_events()
        impl.process_inputs()
        imgui.new_frame()

        # set the active drawing viewport within the current GLFW window (i.e. we are spliiting it up in 3 cols)
        xpos = 0
        ypos = 0
        xwidth = float(w)
        glViewport(int(xpos), int(ypos), int(xwidth), h)
        glClear(GL_COLOR_BUFFER_BIT)
        glUseProgram(shader)

        # GUI TIME
        imgui.begin("Menu", True)

        if imgui.button("Turn ON", 160, 80):
            print("ON")
            ser.write(b'H')

        if imgui.button("Turn OFF", 160, 80):
            ser.write(b'L')
            print("OFF")



        imgui.end()

        imgui.render()

        impl.render(imgui.get_draw_data())


        glfw.swap_buffers(window)

    glfw.terminate()
    ser.close()
  

if __name__ == "__main__":
    main()
