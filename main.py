# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.pardir)
import numpy as np
from mnist import load_mnist
from layers import *
from gradient import *
from collections import OrderedDict
import yaml
import matplotlib.pyplot as plt
import time

class NetWork:
    def __init__(self, weight_init_std = 0.01):
        
        f = open("learning_driver.yml", "r+", encoding='utf-8')
        data = yaml.load(f)
        self.layer_number = int(data['layer number'])
        self.activator = data['activator']
        self.activator_number = data['activator number']
        self.input_size = int(data['input data size'])
        self.hidden_size = int(data['hidden size'])
        self.output_size = int(data['output size'])
        
        self.params = {}
        
        self.params['W1'] = weight_init_std * np.random.randn(self.input_size, self.hidden_size)
        self.params['b1'] = np.zeros(self.hidden_size)
        for i in range(self.layer_number-2):
            self.params['W{}'.format(str(i+2))] = weight_init_std * np.random.randn(self.hidden_size, self.hidden_size)
            self.params['b{}'.format(str(i+2))] = np.zeros(self.hidden_size)
        
        self.params['W{}'.format(str(self.layer_number))] = weight_init_std * np.random.randn(self.hidden_size, self.output_size)
        self.params['b{}'.format(str(self.layer_number))] = np.zeros(self.output_size)
        
        self.activator_list = [ReLu, sigmoid]
        self.layers = OrderedDict()
        for i in range(self.layer_number):
            self.layers['Affine{}'.format(str(i+1))] = Affine(self.params['W{}'.format(str(i+1))], self.params['b{}'.format(str(i+1))])
            if i == (self.layer_number-1):
                break
            self.layers['Relu{}'.format(str(i+1))] = self.activator_list[self.activator_number]()
  
        self.lastlayer = SoftmaxWithLoss()
        
        f.close()
        
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)
            
        return x
    
    def loss(self, x, t):
        y = self.predict(x)
        return self.lastlayer.forward(y, t)
    
    def accuracy(self, x, t):
        y = self.predict(x)
        y = np.argmax(y, axis=1)
        if t.ndim != 1:
            t = np.argmax(t, axis=1)
            
        accuracy = np.sum(y==t) / float(x.shape[0])
        return accuracy
    
    def numerical_gradient(self, x, t):
        loss_W = lambda W: self.loss(x, t)
        
        grads = {}
        for i in range(self.layer_number):
            grads['W{}'.format(str(i+1))] = numerical_gradient(loss_W, self.params['W{}'.format(str(i+1))])
            grads['b{}'.format(str(i+1))] = numerical_gradient(loss_W, self.params['b{}'.format(str(i+1))])

        return grads
    
    def gradient(self, x, t):
        
        self.loss(x, t)
        dout = 1
        dout = self.lastlayer.backward(dout)
        
        layers = list(self.layers.values())
        layers.reverse()
        for layer in layers:
            dout = layer.backward(dout)
            
        grads = {}
        for i in range(self.layer_number):
            grads['W{}'.format(str(i+1))] = self.layers['Affine{}'.format(str(i+1))].dW
            grads['b{}'.format(str(i+1))] = self.layers['Affine{}'.format(str(i+1))].db

        return grads

def main():
    (x_train, t_train), (x_test, t_test) = load_mnist(normalize=True, one_hot_label=True)

    network = NetWork() #Layer Initialization

    iters_num = 10000
    train_size = x_train.shape[0]
    batch_size = 100
    learning_rate = 0.1
    train_loss_list = []
    train_acc_list = []
    test_acc_list = []

    iter_per_epoch = max(train_size / batch_size, 1)
    epoch_number = 0
    epoch_number_list = []
    key_list = []
    
    print('learning start!!')
    for i in range(network.layer_number):
        key_list.append('W{}'.format(str(i+1)))
        key_list.append('b{}'.format(str(i+1)))

    for i in range(iters_num):
        batch_mask = np.random.choice(train_size, batch_size)
        x_batch = x_train[batch_mask]
        t_batch = t_train[batch_mask]
    
        grad = network.gradient(x_batch, t_batch)
        
        for key in key_list:
            network.params[key] -= learning_rate * grad[key] #learning
        
        loss = network.loss(x_batch, t_batch)                  
        train_loss_list.append(loss)
        
        if i%iter_per_epoch == 0:
            epoch_number += 1
            epoch_number_list.append(epoch_number)
            train_acc = network.accuracy(x_train, t_train)
            test_acc = network.accuracy(x_test, t_test)
            train_acc_list.append(train_acc)
            test_acc_list.append(test_acc)
            print('-------- ' + str(epoch_number) + 'th roop --------')
            print('train data accuracy : ' + str(train_acc))
            print('test data accuracy : ' + str(test_acc))
            print()
    
    

    test_acc_max = max(test_acc_list)
    if test_acc_max > 0.9:
        print('recognition accuracy is larger than 90%....')
        time.sleep(2)
        print('Learning finished successfully!!!')  
        
    print()
    print('--------test start--------')
    
    random_data_number = np.random.choice(train_size, 1)
    random_data = x_train[random_data_number]
    random_data_reshape = np.resize(random_data, (28, 28))
    answer_array = t_train[random_data_number]
    answer = np.argmax(answer_array)
    
    character = ''
    for y in range(28):
        line = ''
        for x in range(28):
            gray = random_data_reshape[y][x]
            if gray > 0.5:
                character = "W"
            elif gray > 0:
                character = "'"
            elif gray == 0:
                character = " "
            line += character
        print(line)
        
    print('(This number is shown in ascii style)')
    time.sleep(2.0)
    
    predict_answer = np.argmax(network.predict(random_data))
    print('I think that this image shows ' + str(predict_answer) + '.')
    
    your_answer = input("Which number do you predict? ")
    print('Answer is ' + str(answer) + '.')
    if int(your_answer) == answer:
        if predict_answer == answer:
            print('We answered successfully!')
        else:
            print('Oops... I lost you... I have to study more deeply...')
    else:
        if predict_answer == answer:
            print("I'm smarter than you! Study harder for entrance exam of graduate school!(;;)")
        else:
            print("We shall not pass the entrance exam of graduate school...(;;)")
            
    time.sleep(3.0)
            
    plt.figure(1)
    plt.subplot(2,1,1)
    plt.plot(epoch_number_list, train_acc_list)
    plt.title('Train Accuracy')
    plt.subplot(2,1,2)
    plt.plot(epoch_number_list, test_acc_list)
    plt.subplots_adjust(wspace=1, hspace=1)
    plt.title('Test Accuracy')  
    
    plt.figure(2)
    plt.imshow(random_data_reshape)
    plt.title('Test figure')
    
if __name__ == "__main__":
    main()
