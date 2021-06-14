from manimlib.imports import *

class Thai(Scene):
    def construct(self):
        # available fonts are:
        # KhanaRatsadon, TH SarabunPSK, 2005_iannnnnnCPU, Prompt, TH Charm of AU, 
        title1 = Text("มันคือ", font="KhanaRatsadon").set_color(Color("#d3dde9"))
        title2 = Text("แป้ง", font="KhanaRatsadon")
        title = VGroup(title1, title2).arrange(RIGHT)
        title2.shift(0.2*LEFT)
        #title1.add_background_rectangle(color='white')

        title.scale(4)#.set_color_by_gradient([BLUE, Color("#d3dde9")])
        #self.play(DrawBorderThenFill(title1))
        self.play(ShowCreation(title1))
        self.play(DrawBorderThenFill(title2))
        #self.play(ScaleInPlace(title2,10))
        #self.play(MoveToTarget(title1))