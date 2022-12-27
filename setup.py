from setuptools import setup, find_packages

setup(
  name = 'ema_mindspore',
  packages = find_packages(exclude=[]),
  version = '0.0.1',
  license='MIT',
  description = 'Easy way to keep track of exponential moving average for MindSpore',
  author = 'Yufeng Lyu',
  author_email = 'lvyufeng@cqu.edu.cn',
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/lvyufeng/ema_mindspore',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'exponential moving average'
  ],
#   install_requires=[
#     'mindspore>=2.0.0',
#   ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
  ],
)