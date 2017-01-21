import tensorflow as tf
f = [tf.constant(1),tf.constant(1)]

for i in range(2,10):
    temp = f[i-1] + f[i-2]
    f.append(temp)

with tf.Session() as sess:
    result = sess.run(f)
    print result


a = tf.Variable(1)	#give a initial value to variable
b = tf.Variable(1)
c = tf.Variable(1)
tmp = tf.Variable(1)
changeA = tf.assign(a,b)
changeB = tf.assign(b,c)
tmp = tf.add(a,b)
changeC = tf.assign(c, tmp)
init_op = tf.initialize_all_variables()

print "Remodeled code:"
with tf.Session() as sess:
	sess.run(init_op)
	for _ in range(4):
		result = sess.run(changeC)
		print result
		sess.run(changeA)
		sess.run(changeB)
