'''
rares - rare metals comps
comps - individual comp
assmat1
assmat2
assmat3
assmat4
assmat5

ralloy

pcmats
cmats
steel
'''

scrapCosts = {
  "scrap" : 1,
  "comps" : 0,
  "rares" : 0,
  "cmats" : 10,
  "pcmats" : 30,
  "assmat1" : 15,
  "assmat2" : 15,
  "assmat3" : 30,
  "assmat4" : 30,
  "assmat5" : 570,
  "steel" : 90,
  "ralloy" : 150,
}

compCosts = {
  "scrap" : 0,
  "comps" : 1,
  "rares" : 20,
  "cmats" : 0,
  "pcmats" : 20,
  "assmat1" : 0,
  "assmat2" : 0,
  "assmat3" : 0,
  "assmat4" : 20,
  "assmat5" : 180, 
  "steel" : 60,
  "ralloy" : 150,
}

rareCosts = {
  "scrap" : 0,
  "comps" : 0,
  "rares" : 0,
  "cmats" : 0,
  "pcmats" : 0,
  "assmat1" : 0,
  "assmat2" : 0,
  "assmat3" : 0,
  "assmat4" : 0,
  "assmat5" : 0, 
  "steel" : 0,
  "ralloy" : 20,
}

vicPrices = {
  #WARDEN AC
  "wObrien V110 (AC)" : {
    "cost" : {
      "rares" : 25
    }
  },
  "wObrien V113 Gravekeeper" : {
    "cost" : {
      "rares" : 25,
      "pcmats" : 10,
      "assmat1" : 10
    }
  },
  "wObrien V121 Highlander (TAC)" : {
    "cost" : {
      "rares" : 25,
      "cmats" : 5,
      "assmat1" : 5
    }
  },
  "wObrien V130 Wild Jack (F-TAC)" : {
    "cost" : {
      "rares" : 25,
      "cmats" : 10,
      "assmat1" : 10
    }
  },
  "wObrien V190 Knave (GAC)" : {
    "cost" : {
      "rares" : 40,
    }
  },
  "wObrien V101 Freeman (HAC)" : {
    "cost" : {
      "rares" : 40,
      "cmats" : 15,
      "assmat1": 15,
    }
  },
  "wObrien V200 Squire (RAC)" : {
    "cost" : {
      "rares" : 40,
      "cmats" : 35,
      "assmat1" : 10,
      "assmat3" : 8,
    }
  },
  #COLLIE AC
  "cT3 Xiphos (AC)" : {
    "cost" : {
      "rares" : 25,
    }
  },
  "cT5 Percutio (ATAC)" : {
    "cost" : {
      "rares" : 25,
      "cmats" : 10,
      "assmat1" : 10,
    }
  },
  "cT8 Gemini (RPGAC)" : {
    "cost" : {
      "rares" : 25,
      "cmats" : 10,
      "assmat1" : 10,
    }
  },
  #WARDEN HT
  "wHalf Track (Warden)" : {
    "cost" : {
      "rares" : 60,
    }
  },
  "wAT Half Track" : {
    "cost" : {
      "rares" : 60,
      "pcmats" : 5,
      "assmat2" : 10,
      "assmat4" : 3
    }
  },
  "wScar Twin Half Track" : {
    "cost" : {
      "rares" : 60,
      "pcmats" : 5,
      "assmat4" : 5
    }
  },
  "wSkycaller Rocket Half Track" : {
    "cost" : {
      "rares" : 60,
      "pcmats" : 10,
      "assmat3" : 8,
    }
  },
  #COLLIE HT
  "cHalf Track (Colonial)" : {
    "cost" : {
      "rares" : 55,
    }
  },
  "cHoplite Half Track" : {
    "cost" : {
      "rares" : 55,
      "pcmats" : 3,
      "assmat4" : 3,
    }
  },
  "cMortar Half Track" : {
    "cost" : {
      "rares" : 55,
      "pcmats" : 5,
      "assmat2" : 5,
      "assmat4" : 3
    }
  },
  #TANKETTES
  "cT12 Tankette" : {
    "cost" : {
      "rares" : 35
    }
  },
  "cT20 Ixion" : {
    "cost" : {
      "rares" : 35,
      "cmats" : 10,
      "assmat1" : 15
    }
  },
  "cT14 Vesta (Flame)" : {
    "cost" : {
      "rares" : 35,
      "pcmats" : 10,
      "assmat1" : 15,
    }
  },
  "cT13 Deioneus (Rocket)" : {
    "cost" : {
      "rares" : 35,
      "pcmats" : 20,
      "assmat1" : 15,
      "assmat3" : 3,
    }
  },
  #SCOUT TANKS
  "wKing Spire" : {
    "cost" : {
      "rares" : 70
    }
  },
  "wKing Gallant" : {
    "cost" : {
      "rares" : 70,
      "pcmats" : 5,
      "assmat3" : 5,
    }
  },
  "wKing Jester (Rocket)" : {
    "cost" : {
      "rares" : 70,
      "steel" : 5,
      "assmat1" : 15,
      "assmat3" : 3
    }
  },
  #COLLIE LIGHT TANK
 
}