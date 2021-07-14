from manimlib.imports import *
from time import perf_counter

class MusicVideo(Scene):
    def construct(self):
        background = ImageMobject("Yukiho")
        background.set_width(FRAME_WIDTH)
        background.to_edge(UP, buff = 0)
        self.add_sound("Mebuki")
        
        hw = FRAME_HEIGHT*np.sqrt(3)/2
        hh = FRAME_HEIGHT/2
        hex_pos = [hh*UP + hw*LEFT, hh*DOWN + hw*RIGHT, hh*UP + hw*RIGHT, hh*DOWN + hw*LEFT, ORIGIN]
        hexes = VGroup()
        for i in range(5):
            newhex = RegularPolygon(6).set_opacity(1).set_height(FRAME_HEIGHT).set_color(Color("#d3dde9"))
            newhex.move_to(hex_pos[i])
            hexes.add(newhex)
        
        self.add(hexes)
        self.add(background)
        self.wait(0.2)
        self.play(AnimationGroup(
            *[ApplyMethod(h.set_opacity, 0, run_time = 1) for h in hexes],
            lag_ratio = 0.5
        ))
        self.remove(hexes) 

        song_title = Text("芽吹の季", font = "Yu Gothic UI Bold", stroke_width = 3, stroke_color = BLACK)
        song_title.shift(2*DOWN).scale(2.5)
        singer = Text("萩原雪歩", font = "Yu Gothic UI Bold").set_color(Color("#d3dde9"))
        singer.set_stroke(BLACK, width = 3).scale(1.5)
        title = VGroup(song_title, singer).arrange(DOWN)
        title.to_edge(DOWN)

        title_time = [6.1, 6.6, 7.5, 8]
        singer_time =  [8.8, 9.4, 10.3, 10.9]
        for i in range(len(title_time)):
            self.wait(title_time[i] - self.time)
            self.play(DrawBorderThenFill(song_title[i]), run_time = 0.2)
        for i in range(len(singer_time)):
            self.wait(singer_time[i] - self.time)
            self.play(DrawBorderThenFill(singer[i]), run_time = 0.2)
        self.wait(3)
        self.play(FadeOut(title))

        lyrics= [
            ("微かに眩しい　ひとり暗がりの中で",17),
            ("土を濡らし", 25), 
            ("怯えていたけれど", 29.5),
            ("いつか芽吹く事も夢見てた", 34),
            ("想いは高い空へ（溶け消えてく）", 40.5),
            ("あと少しの一歩で春なのに", 46),
            ("思い切り泣いたあの日々も", 52),
            ("底にしまったあの種もいつか…",55),
            ("溢れる涙が花を咲かす！",61),
            ("心地よい風感じたら",68),
            ("見えなかった景色　そこに広がってる",73),
            ("沢山の光を浴びて",79),
            ("私なりの詩で　もっと咲かせよう",84),
            ("季節は変わりゆく",91),
            ("ほらね　雪解けは芽吹の季",94),
            ("澄み渡る空　ひとり陽だまりの中で",116), 
            ("呼吸ひとひら",124),
            ("目に見えてた息は",128),
            ("光となり　風と消えた",133),
            ("水面に写る花は（揺れ動いて）",139),
            ("それでも負けずに上を向いて",145),
            ("まっすぐな気持ちを届けたい",151),
            ("きっと平気　もう何も怖くない",154),
            ("満ちてく自信が花を咲かす！",159),
            ("心地よい風感じたら",167),
            ("見えていた景色も　彩られてゆく",172),
            ("沢山の勇気抱いて",178),
            ("私でも出来ること　もっと見つけよう",183),
            ("季節は巡りゆく",190),
            ("でもね　前向いて咲いていたい",193),
            ("a late bloomer say yeah",198),
            ("a late bloomer say yeah",204),
            ("一歩一歩ずつ",210),
            ("私なりに伝えたい",213),
            (f'"ありがとう”を',217),
            ("時は経ち　いつかは",231),
            ("儚く散りゆく　次のために",236),
            ("そんな気持ちは今はさよなら",242),
            ("ただ空に向かって", 248),
            ("出来るだけ背伸びをして",251),
            ("Ah…",257),
            ("心地よい風感じたら",261),
            ("見えなかった景色　そこに広がってる",266),
            ("沢山の光を浴びて",272),
            ("私なりの詩で　もっと咲かせよう",278),
            ("季節は変わりゆき ほらね",284),
            ("雪解けは芽吹の季",289),
            ("そのまま強く咲き誇ろう",295),
            ("輝きに包まれながら…",309)
        ]

        # Yu Gothic UI Bold
        snowflake = ImageMobject("snowflake")
        lyric = Text("", font = "Century Gothic Bold")
        for i in range(len(lyrics)):
            ly, time = lyrics[i]
            self.wait(time - self.time) # wait until the first time stamp
            lyric = Text(ly, font = "Yu Gothic Bold").scale(1.5)
            lyric.set_color(Color("#d3dde9"))
            lyric.set_stroke(BLACK, width = 3)

            # special word
            if time == 284:
                lyric[6:10].set_color(BLUE_A)
            lyric.to_edge(DOWN)

            self.add(snowflake)
            self.play(AnimationGroup(
                MoveAlongPath(snowflake, Line(lyric.get_left(), lyric.get_right()), run_time = np.maximum(1.5,0.1*len(ly))),
                Write(lyric), run_time = 0.2*len(ly)),
                lag_ratio = 0
            )
            self.play(FadeOut(snowflake), run_time = 0.2)

            # add kagayaki at the end
            if time == 309:
                light = Dot(color = WHITE).set_opacity(0.2).set_height(0.2).to_edge(UP).shift(UP)
                lights = [light.copy() for _ in range(30)]

                for l in lights:
                    l.shift((np.random.rand()*14 - 7)*RIGHT)
                    l.set_opacity(0.2 + np.random.rand()*0.1)
                    l.set_height(0.2 + np.random.rand()*0.1)
                    self.add(l)
                def update_function(mobject, alpha):
                    mobject.shift(0.1*DOWN*alpha + 0.01*LEFT*np.sin(np.pi*alpha/2))
                self.play(AnimationGroup(
                    *[UpdateFromAlphaFunc(
                    mobject = l, update_function = update_function, run_time = 4)
                    for l in lights],
                    lag_ratio = 0.1
                ))
                for l in lights:
                    self.remove(l)

            display_time = 7 # show at most 7 seconds
            if i < len(lyrics)-1:
                display_time = np.minimum(lyrics[i+1][1] - self.time - 0.5, 6.5)
            else:
                display_time = 0
            self.wait(display_time)
            self.play(FadeOut(lyric), run_time = 0.5)
        self.wait(1)


