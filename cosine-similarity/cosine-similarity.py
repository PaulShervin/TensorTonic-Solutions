import numpy as np

def cosine_similarity(a, b):
    np_a=np.array(a)
    np_b=np.array(b)
    dot_pro=np.dot(a,b)
    norm_a=np.linalg.norm(np_a)
    norm_b=np.linalg.norm(np_b)
    if (norm_a==0.0 or norm_b==0.0):
        return 0
    answer=dot_pro/(norm_a*norm_b)
    return float(answer)