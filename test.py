import numpy as np
import pandas as pd
from gensim.models.word2vec import Word2Vec
import pprint

def recommendation(recommendation):

    # load model
    keyword = 'BASKET_SUM_COMM'

    from gensim.models.word2vec import Word2Vec
    word2vec_sg = Word2Vec.load('./%sw2v_model_all.md.sg' % (keyword))
    return word2vec_sg.wv.most_similar(recommendation,topn=6)



# load model


keyword = 'BASKET_SUM_COMM'
word2vec_sg = Word2Vec.load('./%sw2v_model_all.md.sg' % (keyword))


def recommendation_products(vector, n=6):
    ms = word2vec_sg.wv.similar_by_vector(vector, topn=n)
    return ms

def aggregate_vectors(products_list):
    product_vec = []
    for i in products_list:
        try:
            product_vec.append(word2vec_sg.wv[str(i)])
        except KeyError:
            continue
    return np.mean(product_vec, axis=0)

def prouduct_history_per_cid(CID):
    temp_df = pd.read_csv(
        'data_processed-cid_SUB_COMM/SUB_COMM_CID_%s.csv' % CID)
    temp_list = temp_df['words'].apply(
        lambda x: x.replace('[', '').replace(']', '').replace("'", '').split(',')).tolist()
    products_list = []
    for i in temp_list:
        for j in i:
            k = j.lstrip()
            products_list.append(k)
    return products_list

def recommend_you(CID):
    recommendation = recommendation_products(aggregate_vectors(prouduct_history_per_cid(CID)))
    return recommendation

def others_also_like_by_product(SUB_COMM, n=6):
    ms = word2vec_sg.wv.most_similar(SUB_COMM, topn=n)
    return ms

# recommend_you(2434)
#
# others_also_like_by_product('REFRIGERATED KOSHER PRODUCTS')

if __name__ == '__main__':
    pprint.pprint(recommend_you(2345))
    # pprint.pprint(others_also_like_by_product('MEAT-MISC-RW-ALL'))
