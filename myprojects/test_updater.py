from manimlib.imports import *

class addition(Scene):
    def construct(self):
        text = TexMobject("\\frac{d}{dx} ( ", "f", "+", "g", ")", "=",
                          "\\frac{d}{dx}", #6
                          "f",
                          "+",
                          "\\frac{d}{dx}", #9
                          "g")
        text[1].set_color(YELLOW)
        text[7].set_color(YELLOW)
        text[3].set_color(GREEN)
        text[10].set_color(GREEN)
        text.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        
        self.play(Write(text[0:5]))
        self.wait(0.5)
        self.play(Write(text[5]))
        self.wait(0.5)
        self.play(Transform(text[0].copy(), text[6]), run_time = 1)
        self.play(Transform(text[1].copy(), text[7]), run_time = 1, path_arc=-np.pi)
        self.play(Write(text[8]))
        self.play(Transform(text[0].copy(), text[9]), run_time = 1)
        self.play(Transform(text[3].copy(), text[10]), run_time = 1, path_arc=-np.pi)
        self.wait()

class constant_multiplication(Scene):
    def construct(self):
        d = ""
        text = TexMobject("\\frac{d}{dx}", "c", "\\cdot", "u", "=",
                          "c", #5
                          "\\frac{d}{dx}",
                          "u")
        text[1].set_color(YELLOW)
        text[5].set_color(YELLOW)
        text[3].set_color(GREEN)
        text[7].set_color(GREEN)
                          
        text.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        self.play(Write(text[0:4]))
        self.wait(0.5)
        self.play(Write(text[4]))
        self.wait(0.5)
        self.play(Transform(text[1].copy(), text[5]), run_time = 1, path_arc=-np.pi)
        self.play(Transform(text[0].copy(), text[6]), run_time = 1)
        self.play(Transform(text[2].copy(), text[7]), run_time = 1)
        self.wait()
    
