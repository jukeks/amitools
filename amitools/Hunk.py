"""General definitions for the AmigaOS Hunk format"""

HUNK_UNIT       = 999
HUNK_NAME       = 1000
HUNK_CODE       = 1001
HUNK_DATA       = 1002
HUNK_BSS        = 1003
HUNK_ABSRELOC32 = 1004
HUNK_RELRELOC16 = 1005
HUNK_RELRELOC8  = 1006
HUNK_EXT        = 1007
HUNK_SYMBOL     = 1008
HUNK_DEBUG      = 1009
HUNK_END        = 1010
HUNK_HEADER     = 1011

HUNK_OVERLAY    = 1013
HUNK_BREAK      = 1014
HUNK_DREL32     = 1015
HUNK_DREL16     = 1016
HUNK_DREL8      = 1017
HUNK_LIB        = 1018
HUNK_INDEX      = 1019
HUNK_RELOC32SHORT = 1020
HUNK_RELRELOC32 = 1021
HUNK_ABSRELOC16 = 1022

HUNK_PPC_CODE   = 1257
HUNK_RELRELOC26 = 1260

hunk_names = {
HUNK_UNIT : "HUNK_UNIT",
HUNK_NAME : "HUNK_NAME",
HUNK_CODE : "HUNK_CODE",
HUNK_DATA : "HUNK_DATA",
HUNK_BSS : "HUNK_BSS",
HUNK_ABSRELOC32 : "HUNK_ABSRELOC32",
HUNK_RELRELOC16 : "HUNK_RELRELOC16",
HUNK_RELRELOC8 : "HUNK_RELRELOC8",
HUNK_EXT : "HUNK_EXT",
HUNK_SYMBOL : "HUNK_SYMBOL",
HUNK_DEBUG : "HUNK_DEBUG",
HUNK_END : "HUNK_END",
HUNK_HEADER : "HUNK_HEADER",
HUNK_OVERLAY : "HUNK_OVERLAY",
HUNK_BREAK : "HUNK_BREAK",
HUNK_DREL32 : "HUNK_DREL32",
HUNK_DREL16 : "HUNK_DREL16",
HUNK_DREL8 : "HUNK_DREL8",
HUNK_LIB : "HUNK_LIB",
HUNK_INDEX : "HUNK_INDEX",
HUNK_RELOC32SHORT : "HUNK_RELOC32SHORT",
HUNK_RELRELOC32 : "HUNK_RELRELOC32",
HUNK_ABSRELOC16 : "HUNK_ABSRELOC16",
HUNK_PPC_CODE : "HUNK_PPC_CODE",
HUNK_RELRELOC26 : "HUNK_RELRELOC26",
}

loadseg_valid_begin_hunks = [
HUNK_CODE,
HUNK_DATA,
HUNK_BSS,
HUNK_PPC_CODE
]
loadseg_valid_extra_hunks = [
HUNK_ABSRELOC32,
HUNK_DREL32,
HUNK_DEBUG,
HUNK_SYMBOL,
HUNK_NAME
]

unit_valid_main_hunks = [
HUNK_CODE,
HUNK_DATA,
HUNK_BSS,
HUNK_PPC_CODE
]
unit_valid_extra_hunks = [
HUNK_DEBUG,
HUNK_SYMBOL,
HUNK_NAME,
HUNK_EXT,
HUNK_ABSRELOC32,
HUNK_RELRELOC16,
HUNK_RELRELOC8,
HUNK_DREL32,
HUNK_DREL16,
HUNK_DREL8,
HUNK_RELOC32SHORT,
HUNK_RELRELOC32,
HUNK_ABSRELOC16,
HUNK_RELRELOC26,
]

reloc_hunks = [
HUNK_ABSRELOC32,
HUNK_RELRELOC16,
HUNK_RELRELOC8,
HUNK_DREL32,
HUNK_DREL16,
HUNK_DREL8,
HUNK_RELOC32SHORT,
HUNK_RELRELOC32,
HUNK_ABSRELOC16,
HUNK_RELRELOC26,
]

EXT_SYMB        = 0
EXT_DEF         = 1
EXT_ABS         = 2
EXT_RES         = 3
EXT_ABSREF32    = 129
EXT_ABSCOMMON   = 130
EXT_RELREF16    = 131
EXT_RELREF8     = 132
EXT_DEXT32      = 133
EXT_DEXT16      = 134
EXT_DEXT8       = 135
EXT_RELREF32    = 136
EXT_RELCOMMON   = 137
EXT_ABSREF16    = 138
EXT_ABSREF8     = 139
EXT_RELREF26    = 229

ext_names = {
EXT_SYMB        : 'EXT_SYMB',
EXT_DEF         : 'EXT_DEF',
EXT_ABS         : 'EXT_ABS',
EXT_RES         : 'EXT_RES',
EXT_ABSREF32    : 'EXT_ABSREF32',
EXT_ABSCOMMON   : 'EXT_ABSCOMMON',
EXT_RELREF16    : 'EXT_RELREF16',
EXT_RELREF8     : 'EXT_RELREF8',
EXT_DEXT32      : 'EXT_DEXT32',
EXT_DEXT16      : 'EXT_DEXT16',
EXT_DEXT8       : 'EXT_DEXT8',
EXT_RELREF32    : 'EXT_RELREF32',
EXT_RELCOMMON   : 'EXT_RELCOMMON',
EXT_ABSREF16    : 'EXT_ABSREF16',
EXT_ABSREF8     : 'EXT_ABSREF8',
EXT_RELREF26    : 'EXT_RELREF26'
}

EXT_TYPE_SHIFT = 24
EXT_TYPE_SIZE_MASK = 0xffffff

RESULT_OK = 0
RESULT_NO_HUNK_FILE = 1
RESULT_INVALID_HUNK_FILE = 2
RESULT_UNSUPPORTED_HUNKS = 3

result_names = {
RESULT_OK : "RESULT_OK",
RESULT_NO_HUNK_FILE : "RESULT_NO_HUNK_FILE",
RESULT_INVALID_HUNK_FILE : "RESULT_INVALID_HUNK_FILE",
RESULT_UNSUPPORTED_HUNKS : "RESULT_UNSUPPORTED_HUNKS"
}

HUNKF_ADVISORY = 1<<29
HUNKF_CHIP     = 1<<30
HUNKF_FAST     = 1<<31
HUNKF_ALL      = (HUNKF_ADVISORY | HUNKF_CHIP | HUNKF_FAST)

HUNK_TYPE_MASK = 0xffff
HUNK_FLAGS_MASK = 0xffff0000

TYPE_UNKNOWN    = 0
TYPE_LOADSEG    = 1
TYPE_UNIT       = 2
TYPE_LIB        = 3

type_names = {
  TYPE_UNKNOWN: 'TYPE_UNKNOWN',
  TYPE_LOADSEG: 'TYPE_LOADSEG',
  TYPE_UNIT: 'TYPE_UNIT',
  TYPE_LIB: 'TYPE_LIB'
}
