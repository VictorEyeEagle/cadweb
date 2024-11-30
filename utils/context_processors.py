# utils/context_processors.py
from datetime import datetime

def data_atual(request):
    return {
        'data_atual': datetime.now()
    }
    