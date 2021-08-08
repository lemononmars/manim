# Manim collection

I have a collection of Manim codes [here](https://github.com/lemononmars/manim/tree/master/myprojects). Feel free to explore and reuse them all. 

Below are some featured codes.

## Exponential Sum
[``exponential_sum.py``](exponential_sum.py)

<img src="media/exponential_sum.gif" alt="exponential sum animation gif" width="600"/>

## Cool Effect
You can create text animations as seen [here](https://zulko.github.io/moviepy/examples/moving_letters.html).

See the example below and find the corresponding code in [``cool_effect.py``](test/cool_effect.py)

<img src="media/EffectExamples.gif" alt="cool effect animation gif" width="600"/>

## Lyric Video
It turns out you can make a lyric video! [``song.py``](for_fun/song.py)

<a href="https://www.youtube.com/watch?v=AQQIctTGeJA " target="_blank"><img src="media/lyricvideo.png" 
alt="lyric video using Manim" width="600"/></a>

Ignoring fancy animations, there's one main trick here. ``time.perf_counter()`` is for compiler, not for animation. You have to jump forward to a specific timestamp using ``self.wait(timestamp - self.time)``.
