'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_S3_s3tc'
_p.unpack_constants( """GL_RGB_S3TC 0x83A0
GL_RGB4_S3TC 0x83A1
GL_RGBA_S3TC 0x83A2
GL_RGBA4_S3TC 0x83A3
GL_RGBA_DXT5_S3TC 0x83A4
GL_RGBA4_DXT5_S3TC 0x83A5""", globals())


def glInitS3TcS3():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )