## EMA - MindSpore

A simple way to keep track of an Exponential Moving Average (EMA) for MindSpore

## Install


### Install from pypi

```bash
$ pip install ema-pytorch
```

### Install from source

```bash
$ pip install git+https://github.com/lvyufeng/ema_mindspore
```

## Usage

```python
import numpy as np
import mindspore
from mindspore import Tensor
from ema_mindspore import EMA

# your neural network as a pytorch module

net = mindspore.nn.Dense(512, 512)

# wrap your neural network, specify the decay (beta)

ema = EMA(
    net,
    beta = 0.9999,              # exponential moving average factor
    update_after_step = 100,    # only after this number of .update() calls will it start updating
    update_every = 10,          # how often to actually update, to save on compute (updates every 10th .update() call)
)

# mutate your network, with SGD or otherwise

net.weight.set_data(Tensor(np.random.randn(net.weight.shape), net.weight.dtype))
net.bias.set_data(Tensor(np.random.randn(net.bias.shape), net.bias.dtype))

# you will call the update function on your moving average wrapper

ema.update()

# then, later on, you can invoke the EMA model the same way as your network

data = Tensor(np.random.randn(1, 512), mindspore.float32)

output = net(data)
# synchronize ema to net

ema.synchronize()
ema_output = net(data)

# desynchronize ema to net
ema.desynchronize()

```
