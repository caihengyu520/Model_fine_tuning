#加载原始模型
import tensorflow as tf
from _get_num_params import get_num_params
def load_model(sess1,test_x,test_y):
    """
        Loading the pre-trained model and parameters.
    """
    # global X_1, tst_1, yhat_1
    tf.reset_default_graph()
    with sess1.as_default():
        with sess1.graph.as_default():
            print("--------------------------------------validation_model--------------------------")
            modelpath = r'AE1/model/'
            saver = tf.train.import_meta_graph(modelpath + 'model.ckpt.meta')
            saver.restore(sess1, tf.train.latest_checkpoint(modelpath))
            graph = tf.get_default_graph()
            X_1 = graph.get_tensor_by_name("xs:0")
            tst_1 = graph.get_tensor_by_name("ys:0")
            yhat_1 = graph.get_tensor_by_name("cross_entropy:0")
            decoder2_1 = graph.get_tensor_by_name("decoder2:0")
            encoder_h1 = graph.get_tensor_by_name("encoder_h1:0")
            encoder_b1 = graph.get_tensor_by_name("encoder_b1:0")
            # result_=sess1.run(decoder2_1,feed_dict={X_1:test_x})
            # print("decoder2_1:", result_)
            print('Successfully load the model_1!')
            print("model parameters is:",get_num_params())
            print("-----------------------------------validation_model--------------------success")
            return decoder2_1,X_1,tst_1,yhat_1