#计算原始模型准确率
import tensorflow as tf
from sklearn.metrics import confusion_matrix
import numpy as np

def compute_accuracy(v_xs,v_ys,sess3,X_1,tst_1,yhat_1,decoder2_11):
    #prediction 变为全剧变量
    with sess3.as_default():
        with sess3.graph.as_default():
            # y_pre = sess3.run(decoder2_1,feed_dict={X_1:v_xs})
            #预测值每行是10列，tf.argmax(数据，axis），相等为1，不想等为0
            # print(sess.run(ys,feed_dict={ys:v_ys}))
            # print(sess.run(prediction,feed_dict={xs:v_xs,keep_prob:1}))
            correct_prediction = tf.equal(tf.argmax(decoder2_11,1),tf.argmax(v_ys,1))
            # 计算平均值，即计算准确率
            # print(sess3.run(tst_1,feed_dict={tst_1:v_ys}))
            # print(sess3.run(decoder2_1,feed_dict={X_1:v_xs}))
            #引入混淆矩阵为了计算各个类别的预测准确度
            confusion_matrix1 = confusion_matrix(tf.argmax(sess3.run(tst_1,feed_dict={tst_1:v_ys}),1).eval(), tf.argmax(sess3.run(decoder2_11,feed_dict={X_1:v_xs}),1).eval())
            # print(confusion_matrix1)
            line=np.zeros(10)
            precision=np.zeros(10)
            for i in range(10):
                for j in range(10):
                    line[i] += confusion_matrix1[i][j]
            for i in range(10):
                precision[i] = float(confusion_matrix1[i][i]) / line[i]
            print('precision:',precision)
            # print('W_fc2:',W_fc2.eval())
            accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
            # 运行我们的accuracy这一步
            result = sess3.run(accuracy,feed_dict={X_1:v_xs,tst_1:v_ys})
            return result,precision