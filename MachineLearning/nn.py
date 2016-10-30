import tensorflow as tf

#Read the data
fin = open('train.txt', 'r')
lines = fin.readlines()
data = [[int(number) for number in line.split()] for line in lines] 

fin.close()
fin = open('target.txt', 'r')
lines = fin.readlines()
target = [[(float(number) / 255 ) for number in line.split()] for line in lines] 

num_examples = 60000
data = data[:num_examples]
target = target[:num_examples]

#Learning Parameters 
learning_rate = 0.001
training_epochs = 50
batch_size = 100
display_step = 1

#Network Configuration
n_hidden_1 = 49
n_hidden_2 = 100
n_hidden_3 = 10
n_classes = 3
n_input = 49

#tf Graph input
x = tf.placeholder("float", [None, n_input])
y = tf.placeholder("float", [None, n_classes])

#Create model
def multilayer_perceptron(x, weights, biases):
    # Hidden layer with RELU activation
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)

    layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
    layer_2 = tf.nn.relu(layer_2)

    layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
    layer_3 = tf.nn.relu(layer_3)

    out_layer = tf.matmul(layer_3, weights['out']) + biases['out']
    return out_layer

#Set up layer weights and biases
weights = {
    'h1' : tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'h2' : tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'h3' : tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'out': tf.Variable(tf.random_normal([n_hidden_3, n_classes]))
}

biases = {
    'b1' : tf.Variable(tf.random_normal([n_hidden_1])),
    'b2' : tf.Variable(tf.random_normal([n_hidden_2])),
    'b3' : tf.Variable(tf.random_normal([n_hidden_3])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}    

#Construct model
pred = multilayer_perceptron(x, weights, biases)

#Define loss and optimizer
cost = tf.reduce_sum(tf.nn.l2_loss(tf.abs(tf.sub(pred, y))))
optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

#Init the variables
init = tf.initialize_all_variables()

#Start the training

with tf.Session() as sess:
    sess.run(init)

    #Training epoch 
    for epoch in range(training_epochs):
        avg_cost = 0.
        total_batch = int(num_examples/batch_size)

        for batch in range(total_batch):
            for start, end in zip(range(0, num_examples, batch_size), range(batch_size, num_examples + 1, batch_size)):
                batch_x = data[start : end]
                batch_y = target[start : end]

            #Run optimization
            _, c = sess.run([optimizer, cost], feed_dict={
                    x: batch_x,
                    y: batch_y
                })

            #Compute avg loss
            avg_cost += c / total_batch

        #Display logs per epoch step 
        if epoch % display_step == 0:
            print "Epoch:", '%04d' % (epoch + 1), "cost=", \
                "{:.9f}".format(avg_cost)

    print "Optimization finished!"
