import pickle
from hw14_1 import Employee

if __name__ == "__main__":
    with open('myfile', 'rb') as handle:
        emp1 = pickle.load(handle)
    print("FROM FILE:")
    emp1.get_params()

