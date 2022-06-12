#1 – Over the period covered by the dataset, which businesses appear to be more prosperous?
# Which appear to be struggling?
# Describe your rationale for your answers. Limit your response to 10 images and 500 words.
import pandas as pd
import glob
from os import listdir
from os.path import isfile, join


def importData():
    path = '/Users/franciscochoi/Downloads/VAST-Challenge-2022/Datasets/Journals'
    sample_path = 'media/Participants_sample.csv'
    sample = pd.read_csv(sample_path, index_col=None, header=0)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    #li = []
    for filename in onlyfiles:
        if filename != "Participants_sample.csv" and filename != "script.sh" and filename != ".DS_Store" and filename != 'SocialNetwork.csv':
            print(filename)
            df = pd.read_csv(path + '/' + filename, index_col=None, header=0)
            ds = pd.merge(df, sample, on="participantId", how="inner")
            ds.to_csv(filename)
            #li.append(ds)

def processFinantial():
    path = '/Users/franciscochoi/Downloads/VAST-Challenge-2022/Datasets/Journals/FinancialJournal.csv'
    sample_path = 'media/Participants_sample.csv'
    sample = pd.read_csv(sample_path, index_col=None, header=0)
    df = pd.read_csv(path, index_col=None, header=0)
    ds = pd.merge(df, sample, on="participantId", how="inner")
    #ds.sort_values(by=['timestamp','participants', ascending=True)
    ds.sort_index()
    ds.to_csv('FinancialJournal.csv')

def processFinantial():
    path = '/Users/franciscochoi/Downloads/VAST-Challenge-2022/Datasets/Attributes/Participants.csv'
    sample_path = 'media/Participants_sample.csv'
    sample = pd.read_csv(sample_path, index_col=None, header=0)
    df = pd.read_csv(path, index_col=None, header=0)
    ds = pd.merge(df, sample, on="participantId", how="inner")
    #ds.sort_values(by=['timestamp','participants', ascending=True)
    ds.sort_index()
    ds.to_csv('Participants.csv')

def importLogs():
    path = './PartLog.csv'
    df = pd.read_csv(path, index_col=None, header=0)
    return df


processFinantial()