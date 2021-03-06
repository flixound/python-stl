'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_stencil_two_side'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_EXT_stencil_two_side',False)
_p.unpack_constants( """GL_STENCIL_TEST_TWO_SIDE_EXT 0x8910
GL_ACTIVE_STENCIL_FACE_EXT 0x8911""", globals())
glget.addGLGetConstant( GL_STENCIL_TEST_TWO_SIDE_EXT, (1,) )
glget.addGLGetConstant( GL_ACTIVE_STENCIL_FACE_EXT, (1,) )
@_f
@_p.types(None,_cs.GLenum)
def glActiveStencilFaceEXT( face ):pass


def glInitStencilTwoSideEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
