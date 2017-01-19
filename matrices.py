import tensorflow as tf
Matrix_one = tf.constant([[1,2,3],[2,3,4],[3,4,5]])
Matrix_two = tf.constant([[2,2,2],[2,2,2],[2,2,2]])

first_add = tf.add(Matrix_one, Matrix_two)
second_add = Matrix_one + Matrix_two

first_mul = tf.mul(Matrix_one, Matrix_two)
second_mul = Matrix_one * Matrix_two

with tf.Session() as session:
    result = session.run(Matrix_one)
    print "Matrix one entries:"
    print(result)

    result = session.run(Matrix_two)
    print "Matrix two entries :"
    print(result)

    result = session.run(first_add)
    print "Add using tensorflow function :"
    print(result)

    result = session.run(second_add)
    print "Add using normal expressions :"
    print(result)

    result = session.run(first_mul)
    print "Multiply using tensorflow function :"
    print(result)

    result = session.run(second_mul)
    print "mul using normal expressions :"
    print(result)
