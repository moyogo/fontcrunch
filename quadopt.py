# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_quadopt', [dirname(__file__)])
        except ImportError:
            import _quadopt
            return _quadopt
        if fp is not None:
            try:
                _mod = imp.load_module('_quadopt', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _quadopt = swig_import_helper()
    del swig_import_helper
else:
    import _quadopt
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class Point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Point, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _quadopt.new_Point(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["x"] = _quadopt.Point_x_set
    __swig_getmethods__["x"] = _quadopt.Point_x_get
    if _newclass:x = _swig_property(_quadopt.Point_x_get, _quadopt.Point_x_set)
    __swig_setmethods__["y"] = _quadopt.Point_y_set
    __swig_getmethods__["y"] = _quadopt.Point_y_get
    if _newclass:y = _swig_property(_quadopt.Point_y_get, _quadopt.Point_y_set)
    __swig_destroy__ = _quadopt.delete_Point
    __del__ = lambda self : None;
Point_swigregister = _quadopt.Point_swigregister
Point_swigregister(Point)

class Quad(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Quad, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Quad, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _quadopt.new_Quad(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["p"] = _quadopt.Quad_p_set
    __swig_getmethods__["p"] = _quadopt.Quad_p_get
    if _newclass:p = _swig_property(_quadopt.Quad_p_get, _quadopt.Quad_p_set)
    def arclen(self): return _quadopt.Quad_arclen(self)
    def eval(self, *args): return _quadopt.Quad_eval(self, *args)
    def isLine(self): return _quadopt.Quad_isLine(self)
    def _print(self, *args): return _quadopt.Quad__print(self, *args)
    __swig_destroy__ = _quadopt.delete_Quad
    __del__ = lambda self : None;
Quad_swigregister = _quadopt.Quad_swigregister
Quad_swigregister(Quad)

class Thetas(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Thetas, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Thetas, name)
    __repr__ = _swig_repr
    def init(self, *args): return _quadopt.Thetas_init(self, *args)
    def xy(self, *args): return _quadopt.Thetas_xy(self, *args)
    def dir(self, *args): return _quadopt.Thetas_dir(self, *args)
    __swig_setmethods__["arclen"] = _quadopt.Thetas_arclen_set
    __swig_getmethods__["arclen"] = _quadopt.Thetas_arclen_get
    if _newclass:arclen = _swig_property(_quadopt.Thetas_arclen_get, _quadopt.Thetas_arclen_set)
    def __init__(self): 
        this = _quadopt.new_Thetas()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _quadopt.delete_Thetas
    __del__ = lambda self : None;
Thetas_swigregister = _quadopt.Thetas_swigregister
Thetas_swigregister(Thetas)


def optimize(*args):
  return _quadopt.optimize(*args)
optimize = _quadopt.optimize
# This file is compatible with both classic and new-style classes.

