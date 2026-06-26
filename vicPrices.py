#Contains objects for vehicle in the game and its associated cost input 

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
  "ralloy" : 100,
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
#COLONIAL LIGHT TANKS
    "cHatchet" : {
        "cost" : {
          "rares" : 115
        }
    },
    "cPelekys (LTD)" : {
        "cost" : {
          "rares" : 115,
          "pcmats" : 8,
          "assmat2" : 20,
          "assmat3" : 5
        }
    },
    "cFlame Hatchet" : {
        "cost" : {
          "rares" : 115,
          "pcmats" : 8,
          "assmat2" : 20,
          "assmat3" : 5
        }
    },
    "cKranesca" : {
        "cost" : {
          "rares" : 115,
          "pcmats" : 5,
          "assmat1" : 20,
          "assmat4" : 5
        }
    },
    "cHA-1 Sagaris (AA)" : {
        "cost" : {
          "rares" : 125
        }
    },
    #WARDEN LIGHT TANKS
    "wDevitt" : {
        "cost" : {
          "rares" : 120
        }
    },
    "wDevitt Ironhide" : {
        "cost" : {
          "rares" : 120,
          "pcmats" : 8,
          "assmat2" : 20,
          "assmat3" : 5
        }
    },
    "wDevitt Caine Mortar" : {
        "cost" : {
          "rares" : 125,
          "pcmats" : 3,
          "assmat1" : 20,
          "assmat4" : 3
        }
    },
    "wSharkey Devitt Birdeater (AA)" : {
        "cost" : {
          "rares" : 125
        }
    },

    #WARDEN ASSAULT
    "wSilverHand" : {
        "cost" : {
          "rares" : 160
        }
    },
    "wChieftan" : {
        "cost" : {
          "rares" : 160,
          "pcmats" : 5,
          "assmat1" : 10,
          "assmat4" : 8
        }
    },
    "wLordScar" : {
        "cost" : {
          "rares" : 160,
          "steel" : 15,
          "assmat2" : 25,
          "assmat3" : 25
        }
    },
    #COLONIAL ASSAULT
    "cFalchion" : {
        "cost" : {
          "rares" : 135 #Should probably use mpf for this
        }
    },
    "cSpatha" : {
        "cost" : {
          "rares" : 135,
          "pcmats" : 12,
          "assmat1" : 10,
          "assmat4" : 8
        }
    },
    "cTalos" : {
        "cost" : {
          "rares" : 135,
          "steel" : 3,
          "assmat1" : 10,
          "assmat3" : 15,
          "assmat4" : 15
        }
    },
    "cBardiche" : {
        "cost" : {
          "rares" : 165 
        }
    },
    "cRanseur (Quadiche)" : { #CHANGED
        "cost" : {
          "rares" : 165,
          "pcmats" : 10,
          "assmat2" : 10,
          "assmat3" : 10,
        }
    },
    "cNemesis" : {
        "cost" : {
          "rares" : 150
        }
    },
    #WARDEN CRUISER
    "wBrigand" : {
        "cost" : {
          "rares" : 150
        }
    },
    "wHighwayman" : {
        "cost" : {
          "rares" : 150,
          "pcmats" : 5,
          "assmat2" : 10,
          "assmat3" : 5
        }
    },
    "wOutlaw" : {
        "cost" : {
          "rares" : 150,
          "pcmats" : 10,
          "assmat1" : 10,
          "assmat4" : 10,
        }
    },
    "wThornfall" : {
        "cost" : {
          "rares" : 150,
          "pcmats" : 60,
          "assmat1" : 10,
          "assmat3" : 15,
          "assmat4" : 15,
        }
    },
    #COLLIE IST
    "cScorpion" : {
        "cost" : {
          "rares" : 100
        }
    },
    "cBallista" : {
        "cost" : {
          "rares" : 100,
          "pcmats" : 15,
          "assmat2" : 15
        }
    },

    #WARDEN TD
    "wWidow" : {
        "cost" : {
          "rares" : 160
        }
    },
    "wFirebrand" : {
        "cost" : {
          "rares" : 160,
          "pcmats" : 10,
          "assmat2" : 10,
          "assmat3" : 15
        }
    },

    #WARDEN BT / SPECIAL
    "wFlood (BT)" : { #CHANGED
        "cost" : {
          "steel" : 50,
          "assmat3" : 30,
          "assmat4" : 60,
          "assmat5" : 35
        }
    },
    "wJuggernaut (BT)" : { #CHANGED
        "cost" : {
          "steel" : 40,
          "assmat3" : 65,
          "assmat4" : 30,
          "assmat5" : 45
        }
    },
    "wStain (SPG)" : { #CHANGED
        "cost" : {
          "steel" : 150,
          "assmat3" : 65,
          "assmat4" : 40,
          "assmat5" : 85
        }
    },
    "cLance (BT)" : { #CHANGED
        "cost" : {
          "steel" : 50,
          "assmat3" : 30,
          "assmat4" : 60,
          "assmat5" : 35
        }
    },
    "cHasta (BTD)" : { #CHANGED
        "cost" : {
          "steel" : 60,
          "assmat3" : 65,
          "assmat4" : 45,
          "assmat5" : 65
        }
    },
    "cSarissa (SPG)" : { #CHANGED
        "cost" : {
          "steel" : 150,
          "assmat3" : 65,
          "assmat4" : 40,
          "assmat5" : 85
        }
    },
    #SUPERS
    "cAres" : {
        "cost" : {
          "steel" : 275,
          "assmat3" : 105,
          "assmat4" : 95,
          "assmat5" : 105,
          "ralloy" : 3,
        }
    },
    "wCullen Predator" : {
        "cost" : {
          "steel" : 275,
          "assmat3" : 105,
          "assmat4" : 95,
          "assmat5" : 105,
          "ralloy" : 3,
        }
    },


}