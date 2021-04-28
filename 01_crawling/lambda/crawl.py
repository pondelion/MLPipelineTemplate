from datetime import datetime

import pandas as pd
import numpy as np


def crawl_s3_dummy_data():
    return pd.DataFrame({
        'datetime': [datetime.now()],
        'feat1': [np.random.rand()],
        'feat2': [np.random.rand()],
        'feat3': [np.random.rand()],
    })


def crawl_dynamodb_dummy_data(primary_key_str: str):
    return {
        'primary_key_str': primary_key_str,
        'sort_key_str': datetime.now().strftime('%Y-%m-%d'),
        'feat1': np.random.rand(),
        'feat2': np.random.rand(),
        'feat3': np.random.rand(),
    }




def crawl(event, context):

    return { 
        'message' : 'ok'
    }
