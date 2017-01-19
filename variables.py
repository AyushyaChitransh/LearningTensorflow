import tensorflow as tf
state = tf.Variable(0)
one = tf.constant(1)
counter = tf.add(state, one)
update = tf.assign(state, counter)

init_op = tf.initialize_all_variables()

with tf.Session() as session:
  session.run(init_op)	#do not forget
  print(session.run(state))
  for _ in range(3):
    session.run(update)
    print(session.run(state))

print
with tf.Session() as sess:
	sess.run(init_op)
	result = sess.run(counter)
	print "Counter Variable:"
	print(result)

	result = sess.run(update)
	result = sess.run(update)
	result = sess.run(update)
	print "Updated Counter:"
	print(sess.run(counter))
