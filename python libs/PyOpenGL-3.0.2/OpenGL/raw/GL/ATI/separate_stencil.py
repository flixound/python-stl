'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ATI_separate_stencil'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ATI_separate_stencil',False)
_p.unpack_constants( """GL_STENCIL_BACK_FUNC_ATI 0x8800
GL_STENCIL_BACK_FAIL_ATI 0x8801
GL_STENCIL_BACK_PASS_DEPTH_FAIL_ATI 0x8802
GL_STENCIL_BACK_PASS_DEPTH_PASS_ATI 0x8803""", globals())
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLenum,_cs.GLenum)
def glStencilOpSeparateATI( face,sfail,dpfail,dppass ):pass
@_f
@_p.types(None,_cs.GLenum,_cs.GLenum,_cs.GLint,_cs.GLuint)
def glStencilFuncSeparateATI( frontfunc,backfunc,ref,mask ):pass


def glInitSeparateStencilATI():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
