from ert.cwrap import CWrapper, CNamespace
from ert.enkf import ENKF_LIB


class ErtLog(object):
    cnamespace = None

    @staticmethod
    def log(log_level, message):
        ErtLog.cnamespace.write_log(log_level, message)

    @staticmethod
    def getFilename():
        """ @rtype: int """
        return ErtLog.cnamespace.get_filename()


ErtLog.cnamespace = CNamespace("ErtLog")

cwrapper = CWrapper(ENKF_LIB)

ErtLog.cnamespace.init = cwrapper.prototype("void ert_log_init_log(int, char*, char*, bool)")
ErtLog.cnamespace.write_log = cwrapper.prototype("void ert_log_add_message_py(int, char*)")
ErtLog.cnamespace.get_filename = cwrapper.prototype("char* ert_log_get_filename()")
