# SMLE- Simplify Machine Learning Enviroments

![GitHub stars](https://img.shields.io/github/stars/blkdmr/smle?style=social) ![GitHub forks](https://img.shields.io/github/forks/blkdmr/smle?style=social)

A simple framework that takes care of the boring stuff in ML projects.

# Features

## Configuration

A smle.yaml file will be automatically parsed, and configuration variables will be passed to your entrypoint.
No more need to hardcode your hyperparameters!

## Logging and tracking

Your configuration parameters and all the print statement will be automatically redirected not only to a log file, that will be
stored on your local system to help you store multiple experiments result, but also on remote logging systems, that will help you to look
at the experiment result and progress using your mobile devices.

If you want to use the remote logging sysyem, register to https://wandb.ai/

# Installation

To install the framework

```
pip install smle
```

# Usage

to init the framework you can use the smle cli tools

```
smle init
```

and this will create an empty template

Alternatively, you can adapt your code by simply

```
from smle import SMLE

app = SMLE()

@app.entrypoint
def main(args):

    # Your code

if __name__ == "__main__":
    app.run()
```

**Important!!** The `args` pametered is a map based on a `smle.yaml` file that the SMLE framework need in order to be executed.
An example is automatically generate by the `smle init` command.
Otherwhise, you can create an empty template by just

```
smle create yaml
```

In the yaml template, you will found and example of SMLE section, which contains some important field.

**VERY VERY IMPORTANT**
Look closely at the wandb section. The api key configuration is still under development, and right now,
you api key will we exposed if you upload the logs or the .yaml file to git or to remote storage system.

You can safely remove the wandb section if you dont want to use this feature.

# How to contribute

### Very important

- WTFD (Writing the fabulous documentation)
- **Improve the user key management (e.g. wandb key) with .env files**
- Multiple yaml file support

### Less important

- ML template creation
- NN creation, training and testing tools
- Email notification after event
- Data exploration tools
- Result analysis tools (e.g. diagrams, confusion matrix, ecc.)
- Tensorboard (and similar) support
- Testing

