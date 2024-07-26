
from .cities import Database as db

class TimerFunction:

    speeds = {
        "car": {"speed": 80, "path": "road"},  # average highway speed
        "bus": {"speed": 60, "path": "road"},  # average city bus speed
        # average electric scooter speed
        "scooter": {"speed": 25, "path": "road"},
        "walking": {"speed": 6, "path": "road"},
        "ninja":{"speed":6,"path":"air"},
        "commercial plane": {"speed": 900, "path": "air"},
        "jet plane": {"speed": 2400, "path": "air"},
        "helicopter": {"speed": 400, "path": "air"},
        "saturn 5": {"speed": 40000, "path": "air"},
        "starship sn15": {"speed": 27000, "path": "air"},
        "tesla": {"speed": 80, "path": "road"},  # average highway speed
        
        
        "f1 car": {"speed": 370, "path": "road"},
        "drill": {"speed": 15, "path": "ground"},
        "light in vacuum": {"speed": 299792458, "path": "air"},
        "dragon": {"speed": 200, "path": "air"},
        "proton": {"speed": 299792457, "path": "air"},
        "neutrino":{"speed":299792457,"path":"ground"}
        

    }

    @classmethod
    def findT(cls, c1, c2):
        time=[]
        for v in cls.speeds.values():
            path=v["path"]
            speed=v["speed"]
            dist=db.get_distance(c1,c2,path)
            time.append(truetime(dist/speed))
        vehicles=cls.speeds.keys()
        times=dict(zip(vehicles,time))

        
        return times
def truetime(hours):
    # Calculate hours, minutes, seconds
    hrs = int(hours)
    mins = int((hours - hrs) * 60)
    secs = int(((hours - hrs) * 60 - mins) * 60)
    ms = int((((hours - hrs) * 60 - mins) * 60 - secs) * 1000)
    us = int(((((hours - hrs) * 60 - mins) * 60 - secs) * 1000 - ms) * 1000)
    # Format the output string
    return f"{hrs}H {mins}m {secs}s {ms}ms {us}μs"
