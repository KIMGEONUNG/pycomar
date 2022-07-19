import pickle


def get(obj, path):
    with open(path, 'wb') as f:
        pickle.dump(obj, f)
        # f.write(data)


def load(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
        return data

if __name__ == '__main__':
    import numpy as np
    a  = np.random.randn(10)
    get(a, "./here.pkl")
    b = load("./here.pkl")
    print(a)
    print(b)
