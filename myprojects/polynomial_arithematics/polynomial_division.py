from manimlib.imports import *

class poly_sum_ex1(Scene):
    def construct(self):
        title = Text("ผลบวกพหุนาม ตัวอย่างที่ 1", font="TH Sarabun New")
        title.scale(2).set_color(GREEN)
        title.to_edge(UP)
        self.add(title)

        # Scene 1: show equations
        text1 = Text("จงหาผลบวกของ", font="TH Sarabun New").scale(1.5)
        text2 = Text("และ", font="TH Sarabun New").scale(1.5)
        
        poly1 = TexMobject("2x^2","+","3x","-","4")
        poly2 = TexMobject("3x^2", "-","2x","+","1")

        group1 = VGroup(text1, poly1, text2, poly2).arrange(RIGHT)
        group1.to_edge(UP).shift(DOWN)

        # scene 1: animate question
        self.play(Write(group1))
        self.wait(0.5)
        self.play(Indicate(poly1))
        self.play(Indicate(poly2))

        # Scene 2: express the sum and recolor

        term1 = TexMobject("(","2x^2","+","3x","-","4",")","+","(", "3x^2", "-","2x","+","1",")")
        term2 = TexMobject("(","2x^2","+","3x","+","(-4)",")","+","(", "3x^2", "+","(-2)x","+","1",")")
        #                   0    1     2   3    4    5    6    7   8    9       10    11    12   13 14

        term1.to_edge(LEFT).shift(UP)
        term2.to_edge(LEFT).shift(UP)
        eq1 = TexMobject("(","2x^2","+","3x^2",")","+","(","3x","+","(-2)x",")","+","(","(-4)","+","1",")")
        eq2 = TexMobject("(","2","+","3",")","x^2","+","(","3","+","(-2)",")","x","+","(","(-4)","+","1",")")
        #                 0   1   2   3   4    5    6   7   8   9    10   11  12   13  14   15    16  17  18
        eq3 = TexMobject("5","x^2","+","1","x","+","(-3)")
        eq4 = TexMobject("5","x^2","+","x","-","3")

        eqsign1 = TexMobject("=").to_edge(LEFT)
        eqsign2 = TexMobject("=").to_edge(LEFT).shift(DOWN)
        eqsign3 = TexMobject("=").to_edge(LEFT).shift(2*DOWN)
        eqsign4 = TexMobject("=").to_edge(LEFT).shift(3*DOWN)

        eq1.next_to(eqsign1, RIGHT)
        eq2.next_to(eqsign2, RIGHT)
        eq3.next_to(eqsign3, RIGHT)
        eq4.next_to(eqsign4, RIGHT)

        framebox1 = SurroundingRectangle(term2[1], buff = .1)
        framebox2 = SurroundingRectangle(term2[3], buff = .1, color = BLUE)
        framebox3 = SurroundingRectangle(term2[5], buff = .1, color = RED)
        framebox4 = SurroundingRectangle(term2[9], buff = .1)
        framebox5 = SurroundingRectangle(term2[11], buff = .1, color = BLUE)
        framebox6 = SurroundingRectangle(term2[13], buff = .1, color = RED)

        '''
        # scene 2: equation 1
        '''
        self.play(Write(term1[0]), Write(term1[6]))
        self.play(ReplacementTransform(poly1.copy(), term1[1:6]))
        self.play(Write(term1[7]))
        self.play(Write(term1[8]), Write(term1[14]))
        self.play(ReplacementTransform(poly2.copy(), term1[9:14]))
        #self.wait(1)
        self.play(Indicate(term1[4:6]))
        #self.wait(1)
        self.play(Indicate(term1[10:12]))
        #self.wait(1)
        self.play(ReplacementTransform(term1, term2))

        #
        # eq1: copy x^2 term
        #
        self.play(Write(eqsign1))

        # emphasize x^2
        self.play(ShowCreationThenFadeOut(framebox1))
        term2[1].set_color(YELLOW)
        self.play(ShowCreationThenFadeOut(framebox4))
        term2[9].set_color(YELLOW)

        # write parentheses
        self.play(Write(eq1[0]), Write(eq1[4]))
        eq1[1].set_color(YELLOW)
        eq1[3].set_color(YELLOW)

        # move the terms
        self.play(ReplacementTransform(term2[1].copy(), eq1[1]), path_arc=-np.pi)
        self.play(Write(eq1[2]))
        self.play(ReplacementTransform(term2[9].copy(), eq1[3]), path_arc=-np.pi)
        #self.wait(0.5)

        #
        # eq1: copy x term
        #

        self.play(ShowCreationThenFadeOut(framebox2))
        self.play(term2[3].set_color, BLUE, run_time=1)
        #self.wait(0.5)
        self.play(ShowCreationThenFadeOut(framebox5))
        self.play(term2[11].set_color, BLUE, run_time=1)

        self.play(Write(eq1[5]))
        self.play(Write(eq1[6]), Write(eq1[10]))
        eq1[7].set_color(BLUE)
        eq1[9].set_color(BLUE)

        self.play(ReplacementTransform(term2[3].copy(), eq1[7]), path_arc=-np.pi)
        #self.wait(0.5)
        self.play(Write(eq1[8]))
        self.play(ReplacementTransform(term2[11].copy(), eq1[9]), path_arc=-np.pi)
        #self.wait(0.5)

        #
        # eq1: copy constant
        #
        self.play(ShowCreationThenFadeOut(framebox3))
        self.play(term2[5].set_color, RED, run_time=1)
        #self.wait(0.5)
        self.play(ShowCreationThenFadeOut(framebox6))
        self.play(term2[13].set_color, RED, run_time=1)

        self.play(Write(eq1[11]))
        self.play(Write(eq1[12]), Write(eq1[16]))
        eq1[13].set_color(RED)
        eq1[15].set_color(RED)

        self.play(ReplacementTransform(term2[5].copy(), eq1[13]), path_arc=-np.pi)
        #self.wait(0.5)
        self.play(Write(eq1[14]))
        self.play(ReplacementTransform(term2[13].copy(), eq1[15]), path_arc=-np.pi)
        #self.wait(0.5)

        '''
        # scene 2: equation 2
        '''
        self.play(Write(eqsign2))
        self.play(ReplacementTransform(eq1[0:5].copy(), eq2[0:6]))
        #self.wait(0.5)
        self.play(Write(eq2[6]))
        self.play(ReplacementTransform(eq1[7:12].copy(), eq2[7:13]))
        #self.wait(0.5)
        self.play(Write(eq2[13]))
        self.play(ReplacementTransform(eq1[14:].copy(), eq2[14:]))
        #self.wait(0.5)
        '''
        # scene 3: equation 3
        '''
        self.play(Write(eqsign3))
        self.play(ReplacementTransform(eq2[0:6].copy(), eq3[0:2]))
        #self.wait(0.5)
        self.play(Write(eq3[2]))
        self.play(ReplacementTransform(eq2[7:13].copy(), eq3[3:5]))
        #self.wait(0.5)
        self.play(Write(eq3[5]))
        self.play(ReplacementTransform(eq2[14:].copy(), eq3[6]))
        #self.wait(0.5)

        '''
        # scene 4: equation 4
        '''
        self.play(Write(eqsign4))
        self.play(ReplacementTransform(eq3.copy(), eq4))

        frameboxfinal = SurroundingRectangle(eq4, buff = .1)
        self.play(ShowCreation(frameboxfinal))
        self.wait(1)

class poly_sum_ex2(Scene):
    def construct(self):
        title = Text("ผลบวกพหุนาม ตัวอย่างที่ 1", font="TH Sarabun New")
        title.scale(2).set_color(GREEN)
        title.to_edge(UP)
        self.add(title)

        # Scene 1: show equations
        text1 = Text("จงหาผลบวกของ", font="TH Sarabun New").scale(1.5)
        text2 = Text("และ", font="TH Sarabun New").scale(1.5)
        
        poly1 = TexMobject("2x^2","+","3x","-","4")
        poly2 = TexMobject("3x^2", "-","2x","+","1")

        group1 = VGroup(text1, poly1, text2, poly2).arrange(RIGHT)
        group1.to_edge(UP).shift(DOWN)

        # scene 1: animate question
        self.play(Write(group1))
        self.wait(0.5)
        self.play(Indicate(poly1))
        self.play(Indicate(poly2))

        # Scene 2: express the sum and recolor

        term1 = TexMobject("(","2x^2","+","3x","-","4",")","+","(", "3x^2", "-","2x","+","1",")")
        term2 = TexMobject("(","2x^2","+","3x","+","(-4)",")","+","(", "3x^2", "+","(-2)x","+","1",")")
        #                   0    1     2   3    4    5    6    7   8    9       10    11    12   13 14

        term1.to_edge(LEFT).shift(UP)
        term2.to_edge(LEFT).shift(UP)
        eq1 = TexMobject("(","2x^2","+","3x^2",")","+","(","3x","+","(-2)x",")","+","(","(-4)","+","1",")")
        eq2 = TexMobject("(","2","+","3",")","x^2","+","(","3","+","(-2)",")","x","+","(","(-4)","+","1",")")
        #                 0   1   2   3   4    5    6   7   8   9    10   11  12   13  14   15    16  17  18
        eq3 = TexMobject("5","x^2","+","1","x","+","(-3)")
        eq4 = TexMobject("5","x^2","+","x","-","3")

        eqsign1 = TexMobject("=").to_edge(LEFT)
        eqsign2 = TexMobject("=").to_edge(LEFT).shift(DOWN)
        eqsign3 = TexMobject("=").to_edge(LEFT).shift(2*DOWN)
        eqsign4 = TexMobject("=").to_edge(LEFT).shift(3*DOWN)

        eq1.next_to(eqsign1, RIGHT)
        eq2.next_to(eqsign2, RIGHT)
        eq3.next_to(eqsign3, RIGHT)
        eq4.next_to(eqsign4, RIGHT)

        framebox1 = SurroundingRectangle(term2[1], buff = .1)
        framebox2 = SurroundingRectangle(term2[3], buff = .1, color = BLUE)
        framebox3 = SurroundingRectangle(term2[5], buff = .1, color = RED)
        framebox4 = SurroundingRectangle(term2[9], buff = .1)
        framebox5 = SurroundingRectangle(term2[11], buff = .1, color = BLUE)
        framebox6 = SurroundingRectangle(term2[13], buff = .1, color = RED)

        '''
        # scene 2: equation 1
        '''
        self.play(Write(term1[0]), Write(term1[6]))
        self.play(ReplacementTransform(poly1.copy(), term1[1:6]))
        self.play(Write(term1[7]))
        self.play(Write(term1[8]), Write(term1[14]))
        self.play(ReplacementTransform(poly2.copy(), term1[9:14]))
        #self.wait(1)
        self.play(Indicate(term1[4:6]))
        #self.wait(1)
        self.play(Indicate(term1[10:12]))
        #self.wait(1)
        self.play(ReplacementTransform(term1, term2))

        #
        # eq1: copy x^2 term
        #
        self.play(Write(eqsign1))

        # emphasize x^2
        self.play(ShowCreationThenFadeOut(framebox1))
        term2[1].set_color(YELLOW)
        self.play(ShowCreationThenFadeOut(framebox4))
        term2[9].set_color(YELLOW)

        # write parentheses
        self.play(Write(eq1[0]), Write(eq1[4]))
        eq1[1].set_color(YELLOW)
        eq1[3].set_color(YELLOW)

        # move the terms
        self.play(ReplacementTransform(term2[1].copy(), eq1[1]), path_arc=-np.pi)
        self.play(Write(eq1[2]))
        self.play(ReplacementTransform(term2[9].copy(), eq1[3]), path_arc=-np.pi)
        #self.wait(0.5)

        #
        # eq1: copy x term
        #

        self.play(ShowCreationThenFadeOut(framebox2))
        self.play(term2[3].set_color, BLUE, run_time=1)
        #self.wait(0.5)
        self.play(ShowCreationThenFadeOut(framebox5))
        self.play(term2[11].set_color, BLUE, run_time=1)

        self.play(Write(eq1[5]))
        self.play(Write(eq1[6]), Write(eq1[10]))
        eq1[7].set_color(BLUE)
        eq1[9].set_color(BLUE)

        self.play(ReplacementTransform(term2[3].copy(), eq1[7]), path_arc=-np.pi)
        #self.wait(0.5)
        self.play(Write(eq1[8]))
        self.play(ReplacementTransform(term2[11].copy(), eq1[9]), path_arc=-np.pi)
        #self.wait(0.5)

        #
        # eq1: copy constant
        #
        self.play(ShowCreationThenFadeOut(framebox3))
        self.play(term2[5].set_color, RED, run_time=1)
        #self.wait(0.5)
        self.play(ShowCreationThenFadeOut(framebox6))
        self.play(term2[13].set_color, RED, run_time=1)

        self.play(Write(eq1[11]))
        self.play(Write(eq1[12]), Write(eq1[16]))
        eq1[13].set_color(RED)
        eq1[15].set_color(RED)

        self.play(ReplacementTransform(term2[5].copy(), eq1[13]), path_arc=-np.pi)
        #self.wait(0.5)
        self.play(Write(eq1[14]))
        self.play(ReplacementTransform(term2[13].copy(), eq1[15]), path_arc=-np.pi)
        #self.wait(0.5)

        '''
        # scene 2: equation 2
        '''
        self.play(Write(eqsign2))
        self.play(ReplacementTransform(eq1[0:5].copy(), eq2[0:6]))
        #self.wait(0.5)
        self.play(Write(eq2[6]))
        self.play(ReplacementTransform(eq1[7:12].copy(), eq2[7:13]))
        #self.wait(0.5)
        self.play(Write(eq2[13]))
        self.play(ReplacementTransform(eq1[14:].copy(), eq2[14:]))
        #self.wait(0.5)
        '''
        # scene 3: equation 3
        '''
        self.play(Write(eqsign3))
        self.play(ReplacementTransform(eq2[0:6].copy(), eq3[0:2]))
        #self.wait(0.5)
        self.play(Write(eq3[2]))
        self.play(ReplacementTransform(eq2[7:13].copy(), eq3[3:5]))
        #self.wait(0.5)
        self.play(Write(eq3[5]))
        self.play(ReplacementTransform(eq2[14:].copy(), eq3[6]))
        #self.wait(0.5)

        '''
        # scene 4: equation 4
        '''
        self.play(Write(eqsign4))
        self.play(ReplacementTransform(eq3.copy(), eq4))

        frameboxfinal = SurroundingRectangle(eq4, buff = .1)
        self.play(ShowCreation(frameboxfinal))
        self.wait(1)