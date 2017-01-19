#Python 2.7.12 (default, Nov 19 2016, 06:48:10) 
#[GCC 5.4.0 20160609] on linux2
#Type "help", "copyright", "credits" or "license" for more information.
import tensorflow as tf
a=tf.constant([2])
b=tf.constant([3])
c=tf.add(a,b)
session=tf.Session()
#I tensorflow/core/common_runtime/local_device.cc:25] Local device intra op parallelism threads: 4
#I tensorflow/core/common_runtime/local_session.cc:45] Local session inter op parallelism threads: 4
result = session.run(c)
print(result)
#[5]
#########################################
#		Output			#
#########################################
session.close()
d=tf.constant([2,3,4])
e=tf.constant([4,3,2])
f=tf.add(d,e)
#result2 = session.run(f)
#########################################
#		Error			#
#########################################
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#  File "/home/textsum/.local/lib/python2.7/site-packages/tensorflow/python/client/session.py", line 282, in run
#    raise RuntimeError('Attempted to use a closed Session.')
#RuntimeError: Attempted to use a closed Session.
#with tf.Session() as sess
#  File "<stdin>", line 1
#    with tf.Session() as sess
#                            ^
#########################################
#		Error			#
#########################################
with tf.Session() as sess:
     result2 = sess.run(f)
     print(result2)
 
#[6 6 6]
#########################################
#		Output			#
#########################################
