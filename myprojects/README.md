Hello Math Animator
=================================

Here are my codes for Manim. Feel free to explore and reuse them all.

Cool Effect
======================
A reddit use asks if Manim can animate text as 
https://zulko.github.io/moviepy/examples/moving_letters.html

And sure enough you can! See the example below and find the corresponding code in [``cool_effect.py``](cool_effect.py)

<img src="media/EffectExamples.gif" alt="cool effect animation gif" width="600"/>

Lyric Video
======================
It turns out you can make a lyric video! [``song.py``](song.py)

<a href="https://www.youtube.com/watch?v=AQQIctTGeJA " target="_blank"><img src="media/lyricvideo.png" 
alt="lyric video using Manim" width="400"/></a>

Ignoring fancy animations, there's one main trick here. ``time.perf_counter()`` is for compiler, not for animation. You have to jump forward to a specific timestamp using ``self.wait(timestamp - self.time)``.