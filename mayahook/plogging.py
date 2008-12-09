#import sys
#from version import Version
#from logging import basicConfig, getLevelName, root, info, debug, warning, error, critical
#from logging import *
#
##===============================================================================
## MAYA 8.5 BUG-FIX
##===============================================================================
#logStream = None
#if not hasattr( maya.Output, 'flush' ):
#    class mayaOutput(maya.Output):
#        def flush(*args,**kwargs):
#            pass
#    logStream = mayaOutput()
#
##===============================================================================
## DEFAULT FORMAT SETUP
##===============================================================================
#
#if sys.version_info[:2] >= (2,5):
#    # funcName is only available in python 2.5+
#    basicConfig(format='%(levelname)10s | %(name)-25s | %(funcName)s(): %(message)s ',stream=logStream)
#else:
#    basicConfig(format='%(levelname)10s | %(name)-25s:\t\t%(message)s ',stream=logStream)
#    
## keep as a list of tuples (and not a dictionary) so that we can keep the order
#logLevels = [(getLevelName(n),n) for n in range(0,CRITICAL+1,10)]
#
#rootHandler = root.handlers[0]
#
#  
#def nameToLevel(level):
#    return dict(logLevels).get(level, level)
#
#
##===============================================================================
## DECORATORS
##===============================================================================
#def timed(level=DEBUG):
#    import time
#    def timedWithLevel(func):
#        logger = getLogger(func.__module__)
#        def timedFunction(*arg, **kwargs):
#            t = time.time()
#            res = func(*arg, **kwargs)
#            t = time.time() - t # convert to seconds float
#            strSecs = time.strftime("%M:%S.", time.localtime(t)) + ("%.3f" % t).split(".")[-1]
#            logger.log(level, 'Function %s(...) - finished in %s seconds' % (func.func_name, strSecs))
#            return res
#        timedFunction.__doc__ = func.__doc__
#        timedFunction.func_name = func.func_name
#        return timedFunction
#    return timedWithLevel
#
#def stdOutsRedirected(func):
#    def stdOutsRedirectedFunction(*arg, **kwargs):
#        redirectStandardOutputs(root)
#        origs = (sys.stdout, sys.stderr)
#        try:
#            ret = func(*arg, **kwargs)
#        finally:
#            (sys.stdout, sys.stderr) = origs
#        return ret
#    stdOutsRedirectedFunction.__doc__ = func.__doc__
#    stdOutsRedirectedFunction.func_name = func.func_name
#    return stdOutsRedirectedFunction
#
#
#__issuedDeprecationWarnings = {}
#def deprecated(funcOrMessage):
#    def deprecated2(func):
#        info = dict(
#            name = func.__name__,
#            module = func.__module__)
#        def deprecationLoggedFunc(*args, **kwargs):
#            c = __issuedDeprecationWarnings.get(func.__name__,0)
#            if not c:
#                logger.warning(message % info)
#            __issuedDeprecationWarnings[func.__name__] = c+1
#            return func(*args, **kwargs)
#        deprecationLoggedFunc.__name__ = func.__name__
#        deprecationLoggedFunc.__module__ = func.__module__
#        deprecationLoggedFunc.__doc__ = func.__doc__
#        return deprecationLoggedFunc
#    if isinstance(funcOrMessage,basestring):
#        message = funcOrMessage
#        return deprecated2
#    else:
#        message = "The function '%s.%s' is deprecated and will be unavailable in future pymel versions" % (funcOrMessage.__module__, funcOrMessage.__name__)
#        return deprecated2(funcOrMessage)
#        
#            
##===============================================================================
## INIT TO USER'S PREFERENCE
##===============================================================================
#    
#_level = 20
#try:
#    import pymel
#    _level =  max(_level,int(nameToLevel(pymel.optionVar["logging.logLevel"])))
#except: 
#    pass
#rootHandler.setLevel(_level)
#root.setLevel(0)
#info("%s initialized, set to %s" % (__name__, getLevelName(_level)))
