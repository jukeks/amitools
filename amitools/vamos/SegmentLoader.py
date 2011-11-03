import os.path

from amitools import Hunk
from amitools.HunkReader import HunkReader
from amitools.HunkRelocate import HunkRelocate
from AccessMemory import AccessMemory
from LabelRange import LabelRange

class Segment:
  def __init__(self,name, addr, size, label):
    self.name = name
    self.addr = addr
    self.start = addr + 4
    self.size = size
    self.end = addr + size
    self.label = label
  def __str__(self):
    return "[Seg:'%s':%06x-%06x]" % (self.name, self.addr, self.end)

class SegmentLoader:
  
  def __init__(self, mem, alloc, label_mgr):
    self.mem = mem
    self.alloc = alloc
    self.label_mgr = label_mgr
    self.error = None
    
  def load_seg(self, name):
    base_name = os.path.basename(name)
    hunk_file = HunkReader()
    
    # does file exist?
    if not os.path.isfile(name):
      self.error = "Can't find '%s'" % name
      return None
    
    # read hunk file
    fobj = file(name, "rb")
    result = hunk_file.read_file_obj(name,fobj,None)
    if result != Hunk.RESULT_OK:
      self.error = "Error loading '%s'" % name
      return None
      
    # build segments
    ok = hunk_file.build_segments()
    if not ok:
      self.error = "Error building segments for '%s'" % name
      return None
      
    # make sure its a loadseg()
    if hunk_file.type != Hunk.TYPE_LOADSEG:
      self.error = "File not loadSeg()able: '%s'" % name
      return None

    # create relocator
    relocator = HunkRelocate(hunk_file)
    
    # allocate segment memory
    sizes = relocator.get_sizes()
    names = relocator.get_type_names()
    seg_list = []
    addrs = []
    for i in xrange(len(sizes)):
      size = sizes[i]
      seg_addr = self.alloc.alloc_mem(size + 8) # add 4 bytes guard around segment
      # create label
      label = None
      name = "%s:%d:%s" % (base_name,i,names[i].replace("HUNK_","").lower())
      if self.alloc.label_mgr != None:
        label = LabelRange(name, seg_addr + 4, size)
        self.alloc.label_mgr.add_label(label)
      seg = Segment(name, seg_addr, size, label)
      seg_list.append(seg)
      addrs.append(seg.addr + 4)
    
    # relocate to addresses and return data
    datas = relocator.relocate(addrs)
    
    # write to allocated memory
    for i in xrange(len(sizes)):
      addr = addrs[i]
      self.mem.access.w_data(addr, datas[i])
    
    return seg_list