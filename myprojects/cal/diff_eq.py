from manim import *

class linear_first_order(Scene):
    def construct(self):
        title = Text("สมการเชิงเส้นอันดับ 2 ระดับขั้น 1", font="TH Sarabun New")
        title.set_color_by_gradient([GREEN, BLUE])
        title.set(width = self.camera.frame_width - 2*MED_LARGE_BUFF)
        title.to_edge(UP)
        self.play(Write(title))

        t2 = Text("สมการลักษณะเฉพาะ", font="TH Sarabun New")
        t3 = Text("รากของสมการลักษณะเฉพาะ", font="TH Sarabun New")
        t4 = Text("ผลเฉลยทั่วไป", font="TH Sarabun New")
        t5 = Text("ค่าคงตัวใด ๆ", font="TH Sarabun New")
        
        eq1 = MathTex("a",
                          "y''",
                          "+",
                          "b",
                          "y'",
                          "+",
                          "c",
                          "y",
                          "= 0",
                         tex_to_color_map={"a": YELLOW, "b": RED, "c": BLUE})

        eq2 = MathTex("a",
                          "m^2",
                          "+",
                          "b",
                          "m",
                          "+",
                          "c",
                          "= 0",
                         tex_to_color_map={"a": YELLOW, "b": RED, "c": BLUE})

        eq3 = MathTex("m = ",
                         "m_1",
                         ",",
                         "m_2")
        eq3[1].set_color(GREEN)
        eq3[3].set_color(PINK)

        eq4 = MathTex("y = ",
                         "A_1",
                         "e^",
                         "{m_1",
                         "x}+",
                         "A_2",
                         "e^",
                         "{m_2",
                         "x}")
        eq4[3].set_color(GREEN)
        eq4[7].set_color(PINK)
        
        group = VGroup(eq1, eq2, eq3, eq4).arrange(DOWN)  
        group.set(width = self.camera.frame_width - 5 * LARGE_BUFF)
        group.to_edge(DOWN)

        t2.next_to(eq2, UP)
        t3.next_to(eq3, UP)
        t4.next_to(eq4, UP)
        t5.next_to(eq4, UP)

        framebox1 = SurroundingRectangle(eq1, buff = .1)
        framebox2 = SurroundingRectangle(eq2, buff = .1)
        framebox3 = SurroundingRectangle(eq3, buff = .1)
        framebox4 = SurroundingRectangle(eq4, buff = .1)
        framebox5 = SurroundingRectangle(eq4[1], buff = .1)
        framebox6 = SurroundingRectangle(eq4[5], buff = .1)
        
        arrow1 = Arrow(t5.get_bottom(), eq4[1].get_top(), buff = 0.1)
        arrow2 = Arrow(t5.get_bottom(), eq4[5].get_top(), buff = 0.1)
        
        arrow1.set_color(YELLOW)
        arrow2.set_color(YELLOW)
        
        # scene sequence
        self.play(Write(eq1))
        self.wait(0.5)
        self.play(Create(framebox1))
        self.wait(0.5)
        self.play(FadeOut(framebox1))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq1.copy(), eq2))
        self.wait(0.5)
        self.play(Write(t2), Create(framebox2))
        self.wait(0.5)
        self.play(FadeOut(t2), FadeOut(framebox2))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq2.copy(), eq3))
        self.wait(0.5)
        self.play(Write(t3), Create(framebox3))
        self.wait(0.5)
        self.play(FadeOut(t3), FadeOut(framebox3))
        self.wait(0.5)
        
        self.play(ReplacementTransform(eq3.copy(), eq4))
        self.wait(0.5)
        self.play(Write(t4), Create(framebox4))
        self.wait(0.5)
        self.play(FadeOut(t4), FadeOut(framebox4))
        self.wait(0.5)
        self.play(Create(framebox5), Create(framebox6))
        self.play(Write(t5), GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(0.5)
        self.play(FadeOut(t5), FadeOut(arrow1), FadeOut(arrow2), FadeOut(framebox5), FadeOut(framebox6))
        self.wait(0.5)

        self.play(ScaleInPlace(eq1, 1.2), ScaleInPlace(eq4,1.2), FadeOut(eq2), FadeOut(eq3))

        arrow3 = Arrow(eq1.get_bottom(), eq4.get_top(), buff = 0.1)
        arrow3.set_color(YELLOW)
        self.play(GrowArrow(arrow3))
        self.wait(3)
