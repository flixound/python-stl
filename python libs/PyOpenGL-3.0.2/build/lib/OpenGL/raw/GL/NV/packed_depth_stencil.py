'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_NV_packed_depth_stencil'
_p.unpack_constants( """GL_DEPTH_STENCIL_NV 0x84F9
GL_UNSIGNED_INT_24_8_NV 0x84FA""", globals())


def glInitPackedDepthStencilNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )