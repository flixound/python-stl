'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_AMD_sample_positions'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_AMD_sample_positions',False)
_p.unpack_constants( """GL_SUBSAMPLE_DISTANCE_AMD 0x883F""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLuint,arrays.GLfloatArray)
def glSetMultisamplefvAMD( pname,index,val ):pass


def glInitSamplePositionsAMD():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
