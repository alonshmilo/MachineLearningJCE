import numpy as np
import math
class TwoLayerNet():
    def __init__(self, input_size, hidden_size, output_size ):
        """:param input_size = how much pixels in img, hidden_size - how much perceptrons, output_size-how much classes-1"""
        std = 1*math.e-4;
        self.param = {'w1': np.random.rand(input_size,hidden_size),
                      'b1': np.zeros(hidden_size),
                      'w2': np.random.rand(hidden_size,output_size),
                      'b2': np.zeros(output_size)}

    def train(self, x, y, x_val, y_val):
        """x_val - the validated group (20%) that was left aside"""
        learning_rate = 1*math.e - 3
        batch_size = 20 #how much data we take every iteration in training
        num_iters = 100
        num_train = x.shape[0]
        iteration_per_epoch = num_train/batch_size

        for it in xrange(num_iters):
            indices = np.randon.choice(x.shape[0], size=batch_size)
            x_batch = x[indices]
            y_batch = y[indices]
            loss, grads = self.loss(x_batch, y_batch)
            for param_name in grads:
                self.param[param_name] -=learning_rate * grads[param_name]






    def loss(self,x,y):
        w1, b1 = self.param['w1'], self.param['b1']
        w2, b2 = self.param['w2'], self.param['b2']
        N,D = x.shape

        q1 = x.dot(w1) + b1
        q2 = np.maximum(0,q1)
        q3 = q2.dot(w2) + b2
        scores = q3

        exp_score = np.exp(scores)
        probabilities = exp_score/np.sum(exp_score,axis=1)
        log_sigmoid = -np.log(probabilities)
        loss = np.sum(log_sigmoid)
        lamda = 0.5
        loss += lamda * np.sum(w1*w1)

        grads = []
        dscores = probabilities

        dw2 = q2.T.dot(dscores)
        dw2 += lamda *w2
        db2 = np.sum(dscores)

        dhidden = scores.dot(w1.T)

        dw1 = x.T.dot(dhidden)
        dw1 += lamda *w1
        db1 = np.sum(dhidden,axis=0)

        grads['w1'] = dw1
        grads['b2'] = db2
        grads['w2'] = dw2
        grads['b1'] = db1

        return (loss, grads)