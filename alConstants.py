
CONSTELLATIONS={'LIB': 'LIBRA', 'MIC': 'MICROSCOPIUM', 'BOO': 'BOOTES', 'DRA': 'DRACO', 'TAU': 'TAURUS', 'PAV': 'PAVO',
                'LYR': 'LYRA', 'PIC': 'PICTOR', 'UMI': 'URSA MINOR', 'LYN': 'LYNX', 'CHA': 'CHAMAELEON',
                'EQU': 'EQUULEUS', 'RET': 'RETICULUM', 'PYX': 'PYXIS', 'APS': 'APUS', 'PHE': 'PHOENIX',
                'LAC': 'LACERTA', 'VIR': 'VIRGO', 'CRV': 'CORVUS', 'CMI': 'CANIS MINOR', 'CRU': 'CRUX',
                'CMA': 'CANIS MAJOR', 'CRB': 'CORONA BOREALIS', 'CRA': 'CORONA AUSTRALIS', 'DEL': 'DELPHINUS',
                'OCT': 'OCTANS', 'SCL': 'SCULPTOR', 'SCO': 'SCORPIUS', 'CEN': 'CENTAURUS', 'CET': 'CETUS',
                'CEP': 'CEPHEUS', 'SCT': 'SCUTUM', 'GEM': 'GEMINI', 'TRI': 'TRIANGULUM', 'GRU': 'GRUS',
                'FOR': 'FORNAX', 'TRA': 'TRIANGULUM AUSTRALE', 'SER': 'SERPENS', 'AND': 'ANDROMEDA',
                'VOL': 'VOLANS', 'PSC': 'PISCES', 'PSA': 'PISCES AUSTRINUS', 'ANT': 'ANTLIA', 'MON': 'MONOCEROS',
                'IND': 'INDUS', 'OPH': 'OPHIUCHUS', 'NOR': 'NORMA', 'LUP': 'LUPUS', 'MUS': 'MUSCA', 'VUL': 'VULPECULA',
                'PER': 'PERSEUS', 'UMA': 'URSA MAJOR', 'DOR': 'DORADO', 'PEG': 'PEGASUS', 'COM': 'COMA BERENICES',
                'COL': 'COLUMBA', 'TEL': 'TELESCOPIUM', 'CRT': 'CRATER', 'SEX': 'SEXTANS', 'HYI': 'HYDRUS',
                'HER': 'HERCULES', 'AUR': 'AURIGA', 'VEL': 'VELA', 'MEN': 'MENSA', 'LEO': 'LEO', 'LEP': 'LEPUS',
                'LMI': 'LEO MINOR', 'ORI': 'ORION', 'TUC': 'TUCANA', 'PUP': 'PUPPIS', 'HYA': 'HYDRA',
                'CAS': 'CASSIOPEIA', 'CAR': 'CARINA', 'CAP': 'CAPRICORNUS', 'CVN': 'CANES VENATICI', 'CIR': 'CIRCINUS',
                'CAM': 'CAMELOPARDALIS', 'ERI': 'ERIDANUS', 'CAE': 'CAELUM', 'AQR': 'AQUARIUS', 'SGR': 'SAGITTARIUS',
                'CYG': 'CYGNUS', 'AQL': 'AQUILA', 'SGE': 'SAGITTA', 'HOR': 'HOROLOGIUM', 'CNC': 'CANCER', 'ARA': 'ARA',
                'ARI': 'ARIES'}

FILTER_TYPES={'Asterisms':['ASTER'],
              'Globulars':['GLOCL','GX+GC','SMCGC', 'LMCGC'],
              'Galaxies':['GALXY'],
              'Galaxy Clust':['GALCL'],
              'Bright Nebula':['BRTNB','GX+DN', 'LMCDN','SMCDN'],
              'Dark Nebula':['DRKNB'],
              'Planetary Neb':['PLNNB'],
              'Supernova Rem':['SNREM'],
              'Clusters':['CL+NB', 'GX+DN','LMCCN','LMCOC', 'OPNCL', 'SMCOC']
              }

GAMMA_LIST=[.5, .75, 1, 1.25, 1.5, 1.75]

OBJ_TYPES={"ASTER":"Asterism", "BRTNB":"Bright Nebula", "CL+NB":"Cluster with Nebulosity", "DRKNB":"Dark Nebula",
           "GALCL":"Galaxy cluster","GALXY":"Galaxy","GLOCL":"Globular Cluster",
           "GX+DN":"Diffuse Nebula in a Galaxy","GX+GC":"Globular Cluster in a Galaxy",
           "G+C+N":"Cluster with Nebulosity in a Galaxy","LMCCN":"Cluster with Nebulosity in the LMC",
           "LMCDN":"Diffuse Nebula in the LMC","LMCGC":"Globular Cluster in the LMC", "LMCOC":"Open cluster in the LMC",
           "NONEX":"Nonexistent","OPNCL":"Open Cluster","PLNNB":"Planetary Nebula",
           "SMCCN":"Cluster with Nebulosity in the SMC","SMCDN":"Diffuse Nebula in the SMC",
           "SMCGC":"Globular Cluster in the SMC","SMCOC":"Open cluster in the SMC","SNREM":"Supernova Remnant",
           "QUASR":"Quasar"}

NGC_CODES={'!!': 'very remarkable object', 'sp': 'south preceding', 'P w': 'paired with', 'inv': 'involved',
           'am': 'among', 'susp': 'suspected', 'st': 'star or stellar', 'Ri': 'rich', 'er': 'easily resolved',
           '!': 'remarkable object', 'diam': 'diameter', 'rr': 'partially resolved', 'irr': 'irregular',
           'neb': 'nebula, nebulosity', 's': 'south', 'nf': 'north following', 'rrr': 'well resolved',
           'var': 'variable', 'iF': 'irregular figure', 'C': 'compressed', 'B': 'bright', 'E': 'elongated',
           'D': 'double', 'F': 'faint', '11m': '11th magnitude', 'M': 'middle', 'L': 'large', 'N': 'nucleus',
           'P': 'poor', 'S': 'small', 'R': 'round', 'mag': 'magnitude', 'np': 'north preceding', 'c': 'considerably',
           'b': 'brighter', 'e': 'extremely', 'g': 'gradually', 'Cl': 'cluster', 'dif': 'diffuse', 'f': 'following',
           'm': 'much', 'l': 'little', 'n': 'north', 'p': 'preceding', 'att': 'attached', 'r': 'not well resolved',
           'bet': 'between', 'v': 'very', 'sc': 'scattered', 'sf': 'south following', 'def': 'defined',
           'deg': 'degrees'}

MAIN_PREFIXES=['IC', 'M', 'Mel', 'NGC']