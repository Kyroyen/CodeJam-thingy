
from util.cities import Database as db

class TimerFunction:

    speeds = {
        "car": {"speed": 80, "path": "road"},  # average highway speed
        "bus": {"speed": 60, "path": "road"},  # average city bus speed
        "commercial_plane": {"speed": 900, "path": "air"},
        "jet_plane": {"speed": 2400, "path": "air"},
        "helicopter": {"speed": 400, "path": "air"},
        "saturn_5": {"speed": 40000, "path": "air"},
        "starship sn15": {"speed": 27000, "path": "air"},
        "tesla": {"speed": 80, "path": "road"},  # average highway speed
        "walking": {"speed": 6, "path": "ground"},
        # average electric scooter speed
        "scooter": {"speed": 25, "path": "road"},
        "f1_car": {"speed": 370, "path": "road"},
        "light_in_vacuum": {"speed": 299792458, "path": "air"},
        "dragon": {"speed": 200, "path": "air"},
        "proton": {"speed": 299792457, "path": "air"},
        "drill": {"speed": 15, "path": "ground"}
    }

    @classmethod
    def findT(cls, c1, c2):
        time=[]
        for v in cls.speeds.values():
            print(v)
            path=v["path"]
            speed=v["speed"]
            dist=db.get_distance(c1,c2,path)
            time.append(dist/speed)
        vehicles=cls.speeds.keys()
        times=dict(zip(vehicles,time))
        return times
