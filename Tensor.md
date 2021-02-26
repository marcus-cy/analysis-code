Pytorch：

### Tensor

```torch.tensor(array)```

- 同 Numpy中的ndarry数组，可互相转换

​       tensor和`Numpy array`数组在CPU上可以共用一块内存区域, 改变其中一个另一个也会随之改变

​        ``` torch.from_numpy(n) ``` ,``` t.numpy()```

- 新的张量将继承已有张量的数据属性(结构、类型), 也可以重新指定新的数据类型

  torch.ones_like(x_data)   # 保留 x_data 的属性
  torch.rand_like(x_data, dtype=torch.float)   # 重写 x_data 的数据类型

- 判断当前环境GPU是否可用, 然后将tensor导入GPU内运行
```
if torch.cuda.is_available():
    tensor = tensor.to('cuda')
```

### 神经网络训练
训练 NN 分为两个步骤：

- 正向传播：在正向传播中，NN 对**正确的输出**进行最佳猜测。 它通过其每个函数运行输入数据以进行猜测。

- 反向传播：在反向传播中，NN 根据其**猜测中的误差**调整其参数。 它通过从输出向后遍历，收集有关函数参数（梯度）的误差导数并使用梯度下降来优化参数来实现。 