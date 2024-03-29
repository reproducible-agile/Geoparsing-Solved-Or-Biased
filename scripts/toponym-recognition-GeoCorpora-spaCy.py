# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 19:33:29 2022
"""

import os
import pandas as pd
import numpy as np
import spacy

## load the English pipeline
nlp = spacy.load("en_core_web_lg")

## read GeoCorpora
dir_geocorpora = os.path.join(os.path.dirname(os.getcwd()), 'data', 'evaluation-corpora', 'original-datasets', 'geocorpora.tsv')
df_geocorpora = pd.read_csv(dir_geocorpora, sep = '\t', encoding ='ISO-8859-1')

## keep only useful columns and remove duplicate tweets
df_geocorpora_tweet = df_geocorpora[['tweet_id_str','tweet_text']]
df_geocorpora_tweet = df_geocorpora_tweet.drop_duplicates()

## extract annotated locations in GeoCorpora
df_geocorpora_poi = df_geocorpora[['geoNameId','toponym','longitude','latitude']]
df_geocorpora_poi = df_geocorpora_poi.dropna(subset=['longitude','latitude'])
df_geocorpora_poi = df_geocorpora_poi.drop_duplicates()

## toponym recognition
df_geocorpora_tweet['geotagged_result'] = df_geocorpora_tweet['tweet_text'].apply(lambda text:nlp(text))

## Recall Calculation for each annotated location
df_geocorpora_poi['recall'] = df_geocorpora_poi.apply(lambda row:[], axis = 1)
for i in range(len(df_geocorpora_tweet['geotagged_result'])):
    geotagged_result = list(df_geocorpora_tweet['geotagged_result'].iloc[i].ents)
    df_intersection = df_geocorpora[df_geocorpora['tweet_id_str'] == df_geocorpora_tweet['tweet_id_str'].iloc[i]]
    for i in range(len(df_intersection)):
        geoname_toponym = df_intersection['toponym'].iloc[i]
        geonameid = df_intersection['geoNameId'].iloc[i]
        if isinstance(geoname_toponym, str) == False:
            continue
        if (geotagged_result == ()):
            df_geocorpora_poi[(df_geocorpora_poi['toponym'] == geoname_toponym) & (df_geocorpora_poi['geoNameId'] == geonameid)]['recall'].iloc[0].append(0)
            continue
        found = False
        for result in geotagged_result:
            if (result.label_ in [u"GPE", u"FACILITY", u"LOC", u"FAC", u"LOCATION"]): 
                toponym = result.text
            else:
                continue
            if (toponym == geoname_toponym):
                found = True
                df_geocorpora_poi[(df_geocorpora_poi['toponym'] == geoname_toponym) & (df_geocorpora_poi['geoNameId'] == geonameid)]['recall'].iloc[0].append(1)
                geotagged_result.remove(result)
                break
        if found == False:
            df_geocorpora_poi[(df_geocorpora_poi['toponym'] == geoname_toponym) & (df_geocorpora_poi['geoNameId'] == geonameid)]['recall'].iloc[0].append(0)

for i in range(len(df_geocorpora_poi['recall'])):
    if df_geocorpora_poi['recall'].iloc[i] == []:
        df_geocorpora_poi['recall'].iloc[i] = None
    else:
        df_geocorpora_poi['recall'].iloc[i] = np.sum(df_geocorpora_poi['recall'].iloc[i])/len(df_geocorpora_poi['recall'].iloc[i])

## save toponym recognition results
dir_geocorpora_results = os.path.join(os.path.dirname(os.getcwd()), 'geoparsed-results-reproduced')
df_geocorpora_poi.to_csv(os.path.join(dir_geocorpora_results, 'geocorpora_geotagged_results_spaCy.csv'))
