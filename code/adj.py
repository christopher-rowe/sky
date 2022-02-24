def get_adj_p(p):
    if p==6:
        return [7, 21, 22, 23]
    elif p==7:
        return [6, 8, 20, 21, 22]
    elif p==8:
        return [7, 9, 19, 20, 21]
    elif p==9:
        return [8, 10, 18, 19, 20]
    elif p==10:
        return [9, 11, 17, 18, 19]
    elif p==11:
        return [10, 12, 16, 17, 18]
    elif p==12:
        return [11, 13, 15, 16, 17]
    elif p==13:
        return [12, 14, 15, 16]
    elif p==14:
        return [15, 13, 34, 33]
    elif p==15:
        return [16, 12, 13, 14, 33, 32]
    elif p==16:
        return [17, 11, 12, 13, 15, 32, 31]
    elif p==17:
        return [18, 10, 11, 12, 16, 31, 30]
    elif p==18:
        return [19, 9, 10, 11, 17, 30, 29]
    elif p==19:
        return [20, 8, 9, 10, 18, 29, 28]
    elif p==20:
        return [21, 7, 8, 9, 19, 28, 27]
    elif p==21:
        return [22, 6, 7, 8, 20, 27, 26]
    elif p==22:
        return [23, 6, 7, 21, 26, 25]
    elif p==23:
        return [6, 22, 25, 24]
    elif p==24:
        return [23, 25, 45, 46]
    elif p==25:
        return [24, 23, 22, 26, 44, 45]
    elif p==26:
        return [25, 22, 21, 27, 43, 44]
    elif p==27:
        return [26, 21, 20, 28, 42, 43]
    elif p==28:
        return [27, 20, 19, 29, 41, 42]
    elif p==29:
        return [28, 19, 18, 30, 40, 41]
    elif p==30:
        return [29, 18, 17, 31, 39, 40]
    elif p==31:
        return [30, 17, 16, 32, 38, 39]
    elif p==32:
        return [31, 16, 15, 33, 37, 38]
    elif p==33:
        return [32, 15, 14, 34, 36, 37]
    elif p==34:
        return [33, 14, 35, 36]
    elif p==35:
        return [36, 34, 59, 58]
    elif p==36:
        return [37, 33, 34, 35, 58, 57]
    elif p==37:
        return [38, 32, 33, 36, 57, 56]
    elif p==38:
        return [39, 31, 32, 37, 56, 55]
    elif p==39:
        return [40, 30, 31, 38, 55, 54]
    elif p==40:
        return [41, 29, 30, 39, 54, 53]
    elif p==41:
        return [42, 28, 29, 40, 53, 52]
    elif p==42:
        return [43, 27, 28, 41, 52, 51]
    elif p==43:
        return [44, 26, 27, 42, 51, 50]
    elif p==44:
        return [45, 25, 26, 43, 50, 49]
    elif p==45:
        return [46, 24, 25, 44, 49, 48]
    elif p==46:
        return [24, 45, 48, 47]
    elif p==47:
        return [46, 48, 71, 72]
    elif p==48:
        return [47, 46, 45, 49, 70, 71, 72]
    elif p==49:
        return [48, 45, 44, 50, 69, 70, 71]
    elif p==50:
        return [49, 44, 43, 51, 68, 69, 70]
    elif p==51:
        return [50, 43, 42, 52, 67, 68, 69]
    elif p==52:
        return [51, 42, 41, 53, 66, 67, 68]
    elif p==53:
        return [52, 41, 40, 54, 65, 66, 67]
    elif p==54:
        return [53, 40, 39, 55, 64, 65, 66]
    elif p==55:
        return [54, 39, 38, 56, 63, 64, 65]
    elif p==56:
        return [55, 38, 37, 57, 62, 63, 64]
    elif p==57:
        return [56, 37, 36, 58, 61, 62, 63]
    elif p==58:
        return [57, 36, 35, 59, 60, 61, 62]
    elif p==59:
        return [58, 35, 60, 61]
    elif p==60:
        return [61, 58, 59, 85, 84]
    elif p==61:
        return [62, 57, 58, 59, 60, 85, 84, 83]
    elif p==62:
        return [63, 56, 57, 58, 61, 84, 83, 82]
    elif p==63:
        return [64, 55, 56, 57, 62, 83, 82, 81]
    elif p==64:
        return [65, 54, 55, 56, 63, 82, 81, 80]
    elif p==65:
        return [66, 53, 54, 55, 64, 81, 80, 79]
    elif p==66:
        return [67, 52, 53, 54, 65, 80, 79, 78]
    elif p==67:
        return [68, 51, 52, 53, 66, 79, 78, 77]
    elif p==68:
        return [69, 50, 51, 52, 67, 78, 77, 76]
    elif p==69:
        return [70, 49, 50, 51, 68, 77, 76, 75]
    elif p==70:
        return [71, 48, 49, 50, 69, 76, 75, 74]
    elif p==71:
        return [72, 47, 48, 49, 70, 75, 74, 73]
    elif p==72:
        return [47, 48, 71, 74, 73]
    elif p==73:
        return [72, 71, 74, 97]
    elif p==74:
        return [73, 72, 71, 70, 75, 96, 97]
    elif p==75:
        return [74, 73, 70, 69, 76, 95, 96]
    elif p==76:
        return [75, 74, 69, 68, 77, 94, 95]
    elif p==77:
        return [76, 75, 68, 67, 78, 93, 94]
    elif p==78:
        return [77, 76, 67, 66, 79, 92, 93]
    elif p==79:
        return [78, 77, 66, 65, 80, 91, 92]
    elif p==80:
        return [79, 78, 65, 64, 81, 90, 91]
    elif p==81:
        return [80, 79, 64, 63, 82, 89, 90]
    elif p==82:
        return [81, 80, 63, 62, 83, 88, 89]
    elif p==83:
        return [82, 81, 62, 61, 84, 87, 88]
    elif p==84:
        return [83, 82, 61, 60, 85, 86, 87]
    elif p==85:
        return [84, 61, 60, 86, 87]
    elif p==86:
        return [87, 84, 85, 108]
    elif p==87:
        return [88, 83, 84, 86, 108, 107]
    elif p==88:
        return [89, 82, 83, 87, 107, 106]
    elif p==89:
        return [90, 81, 82, 85, 106, 105]
    elif p==90:
        return [91, 80, 81, 84, 105, 104]
    elif p==91:
        return [92, 79, 80, 83, 104, 103]
    elif p==92:
        return [93, 78, 79, 82, 103, 102]
    elif p==93:
        return [94, 77, 78, 81, 102, 101]
    elif p==94:
        return [95, 76, 77, 80, 101, 100]
    elif p==95:
        return [96, 75, 76, 79, 100, 99]
    elif p==96:
        return [97, 74, 75, 78, 99, 98]
    elif p==97:
        return [73, 74, 96, 98]
    elif p==98:
        return [97, 96, 99, 118]
    elif p==99:
        return [98, 96, 95, 100, 117, 118]
    elif p==100:
        return [99, 95, 94, 101, 116, 117]
    elif p==101:
        return [100, 94, 93, 102, 115, 116]
    elif p==102:
        return [101, 93, 92, 103, 114, 115]
    elif p==103:
        return [102, 92, 91, 104, 113, 114]
    elif p==104:
        return [103, 91, 90, 105, 112, 113]
    elif p==105:
        return [104, 90, 89, 106, 111, 112]
    elif p==106:
        return [105, 89, 88, 107, 110, 111]
    elif p==107:
        return [106, 88, 87, 108, 109, 110]
    elif p==108:
        return [107, 87, 86, 109]
    elif p==109:
        return [110, 107, 108, 126]
    elif p==110:
        return [111, 106, 107, 109, 126, 125]
    elif p==111:
        return [112, 105, 106, 110, 126, 125, 124]
    elif p==112:
        return [113, 104, 105, 111, 125, 124, 123]
    elif p==113:
        return [114, 103, 104, 112, 124, 123, 122]
    elif p==114:
        return [115, 102, 103, 113, 123, 122, 121]
    elif p==115:
        return [116, 101, 102, 114, 122, 121, 120]
    elif p==116:
        return [117, 100, 101, 115, 121, 120, 119]
    elif p==117:
        return [118, 99, 100, 116, 120, 119]
    elif p==118:
        return [98, 99, 117, 119]
    elif p==119:
        return [118, 117, 116, 120]
    elif p==120:
        return [119, 117, 116, 115, 121]
    elif p==121:
        return [120, 116, 115, 114, 122]
    elif p==122:
        return [121, 115, 114, 113, 123]
    elif p==123:
        return [122, 114, 113, 112, 124]
    elif p==124:
        return [123, 113, 112, 111, 125]
    elif p==125:
        return [124, 112, 111, 110, 126]
    elif p==126:
        return [125, 111, 110, 109]

