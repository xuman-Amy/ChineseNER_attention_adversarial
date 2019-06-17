import numpy as np
# import tensorflow as tf
# saver = tf.train.Saver()
# with tf.Session() as sess():
#     saver.restore(sess, './ckpt/lstm+crf-44' + '-' + str(k))
embedding = np.load('./data/weibo_cws_word.npy')
print(embedding)