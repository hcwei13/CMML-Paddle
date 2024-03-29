#encoding=utf8
# Copyright (c) 2021 PaddlePaddle Authors. All Rights Reserved.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import numpy as np

def cal_single_instance(x, y):
    idx = np.argsort(x)  # 升序排列
    y = y[idx]
    loc = x.shape[0]
    for i in range(x.shape[0]):
        if y[i] == 1:
            loc -= i
            break
    return loc


def coverage(x, y):
    """
    :param x: the predicted outputs of the classifier, the output of the ith instance for the jth class is stored in x(i,j)
    :param y: the actual labels of the test instances, if the ith instance belong to the jth class, y(i,j)=1, otherwise y(i,j)=0
    :return: the coverage
    """
    n, d = x.shape
    if x.shape[0] != y.shape[0]:
        print("num of  instances for output and ground truth is different!!")
    if x.shape[1] != y.shape[1]:
        print("dim of  output and ground truth is different!!")
    cover = 0
    for i in range(n):
        cover += cal_single_instance(x[i], y[i])
    cover = cover / n - 1
    return cover


