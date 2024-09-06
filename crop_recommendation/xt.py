import pickle
try:
    with open('venv/model.pkl', 'rb') as f:
        data = pickle.load(f)
except FileNotFoundError:
    print("File not found!")
except Exception as e:
    print("An error occurred:", e)
