'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_SGI_depth_pass_instrument'
_p.unpack_constants( """GL_DEPTH_PASS_INSTRUMENT_SGIX 0x8310
GL_DEPTH_PASS_INSTRUMENT_COUNTERS_SGIX 0x8311
GL_DEPTH_PASS_INSTRUMENT_MAX_SGIX 0x8312""", globals())


def glInitDepthPassInstrumentSGI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )