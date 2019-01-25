from modeles.data import DATA 
print("app/modeles/user.py", "from modeles.data import DATA", DATA)
from .data import DATA
print("app/modeles/user.py", "from .data import DATA", DATA)
from utils.truc import TRUC
print("app/modeles/user.py", "from utils.truc import TRUC", TRUC)
from run import RUN
print("app/modeles/user.py", "from run import RUN", RUN)