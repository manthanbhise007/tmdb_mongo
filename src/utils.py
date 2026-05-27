import pickle

def load_file(file_name,obj):
    with open(file_name,"wb") as f:
        pickle.dump(obj,f)

    """
    "wb" is called the file mode.
    "w" → open the file in write mode
    "b" → open the file in binary mode
    """
    
def read_file(file_name):
    with open(file_name,"rb") as f:
        return pickle.load(f)
    
    """
    "r":Read text file
    """

def save_object(file_name,obj):
    with open(file_name,"wb")as f:
        pickle.dump(obj,f)