#2 – How does the financial health of the residents change over the period covered by the dataset?
# How do wages compare to the overall cost of living in Engagement?
# Are there groups that appear to exhibit similar patterns?
# Describe your rationale for your answers. Limit your response to 10 images and 500 words.

import pandas as pd

def tables():
    a = '/Users/julian/Library/Mobile Documents/com~apple~CloudDocs/Cryptonate/infovis/tpVast/media/Participants.csv'
    b = '/Users/julian/Library/Mobile Documents/com~apple~CloudDocs/Cryptonate/infovis/tpVast/media/PartLog.csv'
    a_csv = pd.read_csv(a, index_col=None, header=0)
    b_csv = pd.read_csv(b, index_col=None, header=0)
    ds = pd.merge(a_csv, b_csv, on="participantId", how="inner")
    #ds.sort_values(by=['timestamp','participants', ascending=True)
    #ds.sort_index()
    ds.to_csv('Merged.csv')

tables()