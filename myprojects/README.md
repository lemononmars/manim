Hello Math Animator
=================================

Here are my codes for Manim. Feel free to explore and reuse them all.

Cool Effect
======================
A reddit use asks if Manim can animate text as 
https://zulko.github.io/moviepy/examples/moving_letters.html

And sure enough you can! See the example below and find the corresponding code in ``cool_effect.py`` [Here](cool_effect.py)
![Image](media/EffectExamples.gif)

Lyric Video
======================
It turns out you can make a lyric video! [``song.py``](song.py)

![YouTube](https://www.youtube.com/watch?v=AQQIctTGeJA)

Ignoring fancy animations, there's one main trick here. ``time.perf_counter()`` is for compiler, not for animation. You have to jump forward to a specific timestamp using ``self.wait(timestamp - self.time)``.