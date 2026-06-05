

if request.Offset == 0x108:
    request.Value = 0x3<<4 #  set SIMOBUCKST to ACT
elif request.Offset == 0x0:
    request.Value = (0x1<<2)|(0x2<<3) # MCUPERFACK to valid