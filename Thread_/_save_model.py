#保存模型，保存修改过的模型
import tensorflow as tf
import shutil

def save_model(e1_value,e2_value,e3_value,e4_value,e5_value,e6_value,e7_value,e8_value):
    tf.reset_default_graph()
    graph=tf.Graph()
    sess=tf.Session(graph=graph)
    with sess.as_default():
        with sess.graph.as_default():
            print("------------------------------save_model--------------------------")
            modelpath = r'AE1/model/'
            saver = tf.train.import_meta_graph(modelpath + 'model.ckpt.meta')
            saver.restore(sess, tf.train.latest_checkpoint(modelpath))
            graph1 = tf.get_default_graph()
            encoder_h11 = graph1.get_tensor_by_name("encoder_h1:0")
            encoder_b11 = graph1.get_tensor_by_name("encoder_b1:0")
            encoder_h21 = graph1.get_tensor_by_name("encoder_h2:0")
            encoder_b21 = graph1.get_tensor_by_name("encoder_b2:0")
            decoder_h11 = graph1.get_tensor_by_name("decoder_h1:0")
            decoder_b11 = graph1.get_tensor_by_name("decoder_b1:0")
            decoder_h21 = graph1.get_tensor_by_name("decoder_h2:0")
            decoder_b21 = graph1.get_tensor_by_name("decoder_b2:0")
            e1 = tf.assign(encoder_h11, e1_value)
            e2 = tf.assign(encoder_h21, e2_value)
            e3 = tf.assign(encoder_b11, e3_value)
            e4 = tf.assign(encoder_b21, e4_value)
            e5 = tf.assign(decoder_h11, e5_value)
            e6 = tf.assign(decoder_h21, e6_value)
            e7 = tf.assign(decoder_b11, e7_value)
            e8 = tf.assign(decoder_b21, e8_value)
            saver1_ = tf.train.Saver()
            # sess.run(tf.global_variables_initializer())
            sess.run([e1, e2, e3, e4, e5, e6, e7, e8])
            shutil.rmtree("AE1/model/")
            saver1_.save(sess, "AE1/model/model.ckpt")
            print("--------------------------------------save_model-----------------------success")
            sess.close()