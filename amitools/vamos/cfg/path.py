from amitools.vamos.cfgcore import *


class PathParser(Parser):
  def __init__(self):
    def_cfg = {
        "path": {
            "command": ValueList(str),
            "cwd": Value(str),
            "vols_base_dir": Value(str, "~/.vamos/volumes")
        },
        "assigns": ValueDict(ValueList(str, sep='+')),
        "volumes": ValueList(str)
    }
    arg_cfg = {
        "path": {
            "command": Argument('-p', '--path', action='append',
                                help="define command search ami path, e.g. c:,sc:c"),
            "cwd": Argument('--cwd', action='store',
                            help="set the current working directory"),
            "vols_base_dir": Argument("--vols-base-dir", action='store',
                                      help="set directory for local volumes")
        },
        "assigns": Argument('-a', '--assign', action='append',
                            help="add AmigaOS assign: name:/sys/path[+/more/path]"),
        "volumes": Argument('-V', '--volume', action='append',
                            help="define AmigaOS volume: name:/abs/sys/path")
    }

    def list_merge(main_key, in_list):
      """convert a list of key-val-pairs to list with "key:val" entries"""
      if in_list is None:
        return None
      res = []
      for key, val in in_list:
        res.append(key + ":" + val)
      return res

    ini_trafo = {
        "assigns": "assigns",
        "volumes": (list_merge, "volumes"),
        "path": {
            "command": ["path", "path"],
            "cwd": ["path", "cwd"]
        }
    }
    Parser.__init__(self, "path", def_cfg, arg_cfg,
                    "paths", "define volumes, assigns, and the search path",
                    ini_trafo,
                    ini_list_sections=['volumes'])
