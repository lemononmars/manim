from manimlib.imports import *

class Thai(Scene):
    def construct(self):
        # available fonts are:
        # KhanaRatsadon, TH SarabunPSK, 2005_iannnnnnCPU, Prompt, TH Charm of AU, Chulabhorn Likit Text
        title1 = Text("รัฐบาลส้นตีน", font="Chulabhorn Likit Text").set_color(Color("#d3dde9"))
        title1.scale(2)
        #title1.add_background_rectangle(color='white')

        n = 20
        titles = [title1]
        for i in range(0,n):
            newtitle = title1.copy()
            newtitle.set_color(random_bright_color())
            newtitle.move_to(np.array([np.random.uniform(-6,7), np.random.uniform(-3,4), 0]))
            titles.append(newtitle)

        self.play(AnimationGroup(*[
            DrawBorderThenFill(t, rate_func = linear, run_time = 1)
            for t in titles
            ],
            lag_ratio = 1
        ))