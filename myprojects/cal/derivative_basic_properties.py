from manimlib.imports import *

class scalar_multiplication(Scene):
    def construct(self):
        t = Text("1. การคูณด้วยค่าคงที่", font="TH Sarabun New")
        t.scale(3)
        t.to_edge(UP)
        self.play(Write(t))
        text = tex_scalar_mul()
                          
        text.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        self.play(Write(text[0:6]))
        self.wait(0.5)
        self.play(Write(text[6]))
        self.wait(0.5)
        self.play(Transform(text[2].copy(), text[7]), run_time = 1, path_arc=-np.pi)
        self.play(Transform(text[0].copy(), text[8]), run_time = 1)
        self.play(Transform(text[4].copy(), text[9]), run_time = 1, path_arc=-np.pi)
        self.wait()
        
class addition(Scene):
    def construct(self):
        t = Text("2. อนุพันธ์ของผลบวกฟังก์ชัน", font="TH Sarabun New")
        t.scale(3)
        t.to_edge(UP)
        self.play(Write(t))
        
        text = tex_add()
        text.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        
        self.play(Write(text[0:6]))
        self.wait(0.5)
        self.play(Write(text[6]))
        self.wait(0.5)
        self.play(Transform(text[0].copy(), text[7]), run_time = 1)
        self.play(Transform(text[2].copy(), text[8]), run_time = 2, path_arc=-np.pi)
        self.play(Write(text[9]))
        self.play(Transform(text[0].copy(), text[10]), run_time = 1)
        self.play(Transform(text[4].copy(), text[11]), run_time = 2, path_arc=-np.pi)
        self.wait()

class multiplication(Scene):
    def construct(self):
        t = Text("3. อนุพันธ์ของผลคูณฟังก์ชัน", font="TH Sarabun New")
        t.scale(3)
        t.to_edge(UP)
        self.play(Write(t))
        
        text = tex_mul()
        text.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        
        self.play(Write(text[0:6]))
        self.wait(0.5)
        self.play(Write(text[6]))
        self.wait(0.5)
        self.play(Transform(text[2].copy(), text[7]), run_time = 1, path_arc=-np.pi)
        self.play(Transform(text[0].copy(), text[8]), run_time = 1)
        self.play(Transform(text[4].copy(), text[9]), run_time = 1, path_arc=-np.pi)
        self.play(Write(text[10]))
        self.play(Transform(text[4].copy(), text[11]), run_time = 1, path_arc=-np.pi)
        self.play(Transform(text[0].copy(), text[12]), run_time = 1)
        self.play(Transform(text[2].copy(), text[13]), run_time = 1, path_arc=-np.pi)
        self.wait()

class division(Scene):
    def construct(self):
        t = Text("4. อนุพันธ์ของผลหารฟังก์ชัน", font="TH Sarabun New")
        t.scale(3)
        t.to_edge(UP)
        self.play(Write(t))
        
        text = tex_div()
        text.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        
        self.play(Write(text[0:6]))
        self.wait(0.5)
        self.play(Write(text[6]))
        self.wait(0.5)
        self.play(Transform(text[4].copy(), text[7]), run_time = 1, path_arc=np.pi)
        self.play(Transform(text[0].copy(), text[8]), run_time = 1)
        self.play(Transform(text[2].copy(), text[9]), run_time = 1, path_arc=-np.pi)
        self.play(Write(text[10]))
        self.play(Transform(text[2].copy(), text[11]), run_time = 1, path_arc=-np.pi)
        self.play(Transform(text[0].copy(), text[12]), run_time = 1)
        self.play(Transform(text[4].copy(), text[13]), run_time = 1, path_arc=np.pi)
        self.play(Write(text[14]))
        self.play(Transform(text[4].copy(), text[15]), run_time = 1, path_arc=np.pi)
        self.play(Write(text[16]))
        self.wait()

class composite(Scene):
    def construct(self):
        t = Text("5. อนุพันธ์ของฟังก์ชันประกอบ (กฎลูกโซ่)", font="TH Sarabun New")
        t.scale(2)
        t.to_edge(UP)
        self.play(Write(t))
        
        text = tex_comp()
        text.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        h = text.get_height()
        
        self.play(Write(text[0:6]))
        self.wait(0.5)
        self.play(Write(text[6]))
        self.wait(0.5)
        self.play(ReplacementTransform(text[0].copy(), text[7]), run_time = 1)
        self.play(ReplacementTransform(text[4].copy(), text[8]), run_time = 1, path_arc=-np.pi)
        self.wait(0.5)
        self.play(ReplacementTransform(text[2].copy(), text[9]), ReplacementTransform(text[2].copy(), text[11]), run_time = 1, path_arc=-np.pi)
        self.wait(0.5)
        self.play(ReplacementTransform(text[4].copy(), text[10]), run_time = 1, path_arc=-np.pi)
        self.play(Write(text[12]))
        self.play(ReplacementTransform(text[0].copy(), text[13]), run_time = 1)
        self.play(ReplacementTransform(text[4].copy(), text[14]), run_time = 1, path_arc=-np.pi)
        self.wait()

        abb1 = TexMobject("\\frac{d}{dx} ( ", "f", "\\circ","g", ") = \\frac{d}{d", "g", "}", "f(", "g", ")", "\\cdot \\frac{d}{dx}", "g")
        abb1.set_height(h)

        for i in [1,7,9]:
            abb1[i].set_color(YELLOW)
        for i in [3,5,8,11]:
            abb1[i].set_color(BLUE)

        abb2 = TexMobject("(", "f", "\\circ", "g", ")' = ", "f'(", "g", ")", "\\cdot", "g'")
        abb2.set_height(h)

        for i in [1,5,7]:
            abb2[i].set_color(YELLOW)
        for i in [3,6,9]:
            abb2[i].set_color(BLUE)
        
        self.play(ReplacementTransform(text, abb1), run_time = 2)
        self.wait(2)
        self.play(Transform(abb1, abb2), run_time = 2)
        self.wait(2)

class summary(Scene):
    def construct(self):
        t = Text("สรุปสมบัติทั้งหมดของอนุพันธ์", font="TH Sarabun New")
        t.scale(2)
        t.to_edge(UP)
        t.set_color(GREEN)
        self.play(Write(t))
        
        t1 = tex_scalar_mul()
        t2 = tex_add()
        
        group1 = VGroup(t1, t2).arrange(DOWN)
        group1.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        
        self.play(Write(t1))
        self.play(Write(t2))
        self.wait(3)
        self.play(FadeOut(group1))
        t3 = tex_mul()
        t4 = tex_div()
        
        group2 = VGroup(t3, t4).arrange(DOWN)
        group2.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        self.play(Write(t3))
        self.play(Write(t4))
        self.wait(3)
        self.play(FadeOut(group2))
        
        t5 = tex_comp()
        t5.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
        self.play(Write(t5))
        self.wait(3)
        self.play(FadeOut(t5))

        group3 = VGroup(t1, t2, t3, t4, t5).arrange(DOWN)
        group3.to_edge(UP)
        group3.set_height(FRAME_HEIGHT - 2.5 * LARGE_BUFF)
        self.play(Write(group3))
        self.wait(5)
        
def tex_add():
    text = TexMobject("\\frac{d}{dx}", "( ", "f", #2
                          "+", "g", #4
                          ")(x)","=", "\\frac{d}{dx}", "f(x)", #8
                          "+", "\\frac{d}{dx}", "g(x)" #11
                          )
    text[2].set_color(YELLOW)
    text[8].set_color(YELLOW)
    text[4].set_color(BLUE)
    text[11].set_color(BLUE)
    return text

def tex_scalar_mul():
    text = TexMobject("\\frac{d}{dx}", "(", "c", #2
                          "\\cdot", "f", #4
                          ")(x)", "=", "c", #7
                          "\\frac{d}{dx}", "f(x)") #9
    text[2].set_color(YELLOW)
    text[7].set_color(YELLOW)
    text[4].set_color(BLUE)
    text[9].set_color(BLUE)
    return text

def tex_mul():
    text = TexMobject("\\frac{d}{dx}", "(", "f", #2
                          "\cdot", "g", #4
                          ")(x)", "=", "f(x)", #7
                          "\\frac{d}{dx}", "g(x)", #9
                          "+", "g(x)", #11
                          "\\frac{d}{dx}", "f(x)") #13
    text[2].set_color(YELLOW)
    text[7].set_color(YELLOW)
    text[13].set_color(YELLOW)
    text[4].set_color(BLUE)
    text[9].set_color(BLUE)
    text[11].set_color(BLUE)
    return text

def tex_div():
    text = TexMobject("\\frac{d}{dx}", "\\left({", "f", #2
                          "\\over", "g", #4
                          "}\\right)(x)", "=", "{g(x)", #7
                          "\\frac{d}{dx}", "f(x)", #9
                          "-", "f(x)", #11
                          "\\frac{d}{dx}", "g(x)", #13
                          "\\over", "g(x)", #15
                          "^2}") 
    text[2].set_color(YELLOW)
    text[9].set_color(YELLOW)
    text[11].set_color(YELLOW)
    text[4].set_color(BLUE)
    text[7].set_color(BLUE)
    text[13].set_color(BLUE)
    text[15].set_color(BLUE)
    return text

def tex_comp():
    text = TexMobject("\\frac{d}{dx}", "(", "f", #2
                          "\\circ", "g", #4
                          ")(x)", "=", "\\frac{d}{d", "g(x)}", #8
                          "f(", #9
                          "g(x)", #10
                          ")", "\cdot", "\\frac{d}{dx}", "g(x)") #14
    text[2].set_color(YELLOW)
    text[9].set_color(YELLOW)
    text[11].set_color(YELLOW)
    text[4].set_color(BLUE)
    text[8].set_color(BLUE)
    text[10].set_color(BLUE)
    text[14].set_color(BLUE)
    return text
