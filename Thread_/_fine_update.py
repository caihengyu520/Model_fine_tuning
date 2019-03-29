#获取更新时每个批次的数据
import numpy as np
def fine_update(train_data,train_label,update_size,total_size,index):
    #if update_index+update_size>total_size:
    update_index=(index+update_size-1)%total_size
    index = (index + update_size) % total_size
    batch_x=np.array(train_data.iloc[update_index,:]).reshape([update_size,784])
    batch_label=np.array(train_label.iloc[update_index]).reshape([update_size,10])
    return index,batch_x,batch_label