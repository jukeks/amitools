import pytest
import logging
from amitools.vamos.log import log_libmgr
from amitools.vamos.libnative import ALibManager
from amitools.vamos.loader import SegmentLoader
from amitools.vamos.mem import MemoryAlloc
from amitools.vamos.machine import Machine
from amitools.vamos.atypes import ExecLibrary, Library


def setup():
  machine = Machine()
  mem = machine.get_mem()
  alloc = MemoryAlloc.for_machine(machine)
  sp = machine.get_ram_begin() - 4
  # setup exec
  exec_lib = ExecLibrary.alloc(alloc, "exec.library", "bla", 520*6)
  exec_lib.setup()
  exec_lib.fill_funcs()
  exec_base = exec_lib.get_addr()
  mem.w32(4, exec_base)
  machine.set_zero_mem(0, exec_base)
  return machine, alloc, sp, mem, exec_lib


def libnative_mgr_test(buildlibnix):
  if buildlibnix.flavor not in ('gcc', 'gcc-dbg'):
    pytest.skip("only single base lib supported")
  log_libmgr.setLevel(logging.INFO)
  machine, alloc, sp, mem, exec_lib = setup()
  # load
  lib_file = buildlibnix.make_lib('testnix')

  class PathMgrMock:
    def ami_to_sys_path(self, lock, ami_path, mustExist=True):
      if ami_path == 'LIBS:testnix.library':
        return lib_file

  pm = PathMgrMock()
  segload = SegmentLoader(alloc, pm)
  mgr = ALibManager(machine, alloc, segload)
  # open_lib
  lib_base = mgr.open_lib("testnix.library", run_sp=sp)
  assert lib_base > 0
  assert mgr.is_base_addr(lib_base)
  lib_info = mgr.get_lib_info_for_name("testnix.library")
  assert lib_info
  assert lib_info.is_base_addr(lib_base)
  # close lib
  seglist = mgr.close_lib(lib_base, run_sp=sp)
  assert seglist == 0
  lib_info = mgr.get_lib_info_for_name("testnix.library")
  assert lib_info
  assert not lib_info.is_base_addr(lib_base)
  # expunge lib
  left = mgr.shutdown(run_sp=sp)
  assert left == 0
  assert not mgr.is_base_addr(lib_base)
  lib_info = mgr.get_lib_info_for_name("testnix.library")
  assert not lib_info
  # we have to manually clean the lib here (as Exec FreeMem() does not work)
  lib = Library(mem, lib_base, alloc)
  lib.free()
  # cleanup
  exec_lib.free()
  assert alloc.is_all_free()


def libnative_mgr_fail_test():
  machine, alloc, sp, mem, exec_lib = setup()
  # load

  class PathMgrMock:
    def ami_to_sys_path(self, lock, ami_path, mustExist=True):
      return None

  pm = PathMgrMock()
  segload = SegmentLoader(alloc, pm)
  mgr = ALibManager(machine, alloc, segload)
  # open_lib
  lib_base = mgr.open_lib("testnix.library", run_sp=sp)
  assert lib_base == 0
  # close lib
  with pytest.raises(ValueError):
    mgr.close_lib(lib_base, run_sp=sp)
  # expunge lib
  with pytest.raises(ValueError):
    mgr.expunge_lib(lib_base, run_sp=sp)
  # expunge lib
  left = mgr.shutdown(run_sp=sp)
  assert left == 0
  # cleanup
  exec_lib.free()
  assert alloc.is_all_free()
