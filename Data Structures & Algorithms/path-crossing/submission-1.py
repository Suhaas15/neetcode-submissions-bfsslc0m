class Solution:
    def isPathCrossing(self, path: str) -> bool:
        Xres, Yres = 0,0
        res={(0,0)}

        for char in path:
            if char=="N":
                Xres+=1
            elif char=="S":
                Xres-=1
            elif char=="E":
                Yres+=1
            else:
                Yres-=1

            if (Xres,Yres) in res:
                return True
            res.add((Xres,Yres))

        return False