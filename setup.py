
from distutils.core import setup
import py2exe

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.1.0",
    description = "GenLogger utility",
    name = "GenLogger",

    # targets to build
    windows = [
                {
                  "script"         : "GenLogger",
                  # "icon_resources" : [ (0, "LabJackViewer.ico") ],
                }
              ]
    )
