# Bad Apple in terminal using Python

### Please note, this is a fork from the original creator [Koteikar](https://github.com/Koteikar)
#### You can see his video [here](https://www.youtube.com/watch?v=ikyKLfB4cfg&ab_channel=AndrewDanylyshyn)

![](images/git-preview.gif)

## Getting Started

### Prerequisites

For this project you'll need these packages to install:
* opencv-python
* fpstimer
* playsound
* pynput
* tqdm 

### Installing packages with pip

To install these packages write to console this code:


```python
pip install -r requirements.txt
```

### Installing packages with poetry

First you need to spawn your venv with poetry
```python
poetry shell 
```
Then install the dependencies

```python
poetry install
```

## Size of window

The code is support any size of window, but if you want to run it full screen,
make sure that the size of text is set to 100%, or image will be asymmetric.
To check the size of text you need to go to settings > system > display > change the size of text. 
![](images/img_1.png)

### Running this code

To run this code print in terminal:
```python
python main.py
```
If you run code for the first time, frames will be generated from the video (which are stored in the frames folder), but you can monitor the progress through the console, this only needs to be generated the first time. After that, the integrity of the frames is only checked to ensure that nothing is missing.

## Built With

* [Python 3.11.5](https://www.python.org/)
* [opencv-python](https://opencv.org/)
* [fpstimer](https://pypi.org/project/fpstimer/)
* [playsound](https://pypi.org/project/playsound/)
* [tqdm](https://pypi.org/project/tqdm/)


## Authors

* **Andrew Danylyshyn** - *Initial work* - [Koteikar](https://github.com/Koteikar)
* **Adriano Warmling** - *Adaptations* - [Tsujjii](https://github.com/tsujjii)


## Acknowledgments from [Koteikar](https://github.com/Koteikar)

I'm extremely grateful to ZEN, for creating of Touhou.

I must also thank [あにら](https://www.nicovideo.jp/watch/sm8628149), for creating of video.
___
NOTE: Also, remember to see the original work 😉
