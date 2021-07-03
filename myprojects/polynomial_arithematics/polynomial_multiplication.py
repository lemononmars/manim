from manimlib.imports import *

class poly_mult_ex2(Scene):
    def construct(self):

        # Scene 1: show equations
        text1 = Text("จงหาผลคูณของ", font="TH Sarabun New").scale(1.5)
        text2 = Text("และ", font="TH Sarabun New").scale(1.5)
        
        poly1 = TexMobject("x^2","+","2x","-","4")
        poly2 = TexMobject("-3x", "+","5")

        group1 = VGroup(text1, poly1, text2, poly2).arrange(RIGHT)
        group1.to_edge(UP).shift(DOWN)
        text1.shift(0.15*DOWN) # shift manually....
        text2.shift(0.05*DOWN) # shift manually....
        poly2.shift(0.05*DOWN) # shift manually....

        # scene 1: animate question
        self.play(Write(group1))
        self.wait(0.5)
        self.play(Indicate(poly1))
        self.play(Indicate(poly2))
        self.wait(1)

        #
        # Scene 2: express the sum and recolor
        #
        term1 = TexMobject("(","x^2","+","2x","-","4",")","\\times","(","-3x", "+","5",")")
        term2 = TexMobject("(","x^2","+","2x","+","(-4)",")","\\times","(","(-3x)", "+","5",")")
        #                   0    1     2   3    4    5    6    7        8    9       10  11  12
        term1.to_edge(LEFT).shift(UP)
        term2.to_edge(LEFT).shift(UP)
 
        self.play(ReplacementTransform(poly1.copy(), term1[0:7]))
        self.play(Write(term1[7]))
        self.play(ReplacementTransform(poly2.copy(), term1[8:]))
        self.wait(1)

        fb = SurroundingRectangle(term1[4:6], buff = .1)
        self.play(ShowCreationThenFadeOut(fb))
        fb = SurroundingRectangle(term1[9], buff = .1)
        self.play(ShowCreationThenFadeOut(fb))
        self.wait(1)
        self.play(ReplacementTransform(term1, term2))
        self.wait(1)

        #
        # Scene 3: create table and move the terms to the header
        #

        row1 = TexMobject("\\times", "x^2", "2x", "(-4)")
        row2 = TexMobject("(-3x)", "(-3x)\\times(x^2)", "(-3x)\\times(2x)", "(-3x)\\times(-4)")
        row2s = TexMobject("(-3x)", "-3x^3", "-6x^2", "12x")
        row3 = TexMobject("5", "5\\times(x^2)", "5\\times(2x)", "5\\times(-4)")
        row3s = TexMobject("5", "5x^2", "10x", "-20")
        tex_table = [row1, row2, row3]
        tex_tables = [row1, row2s, row3s] #row1 isn't used here, but it's put so that the for loop works nicely

        # create a table structure
        topleft = LEFT*6
        for i in range (0, len(row1)):
            for j in range (0, 3):
                tex_table[j][i].move_to(topleft + RIGHT*3.5*i + DOWN*j)
                tex_tables[j][i].move_to(topleft + RIGHT*3.5*i + DOWN*j)
                
        # move original terms to the table
        hline = Line(topleft + LEFT + DOWN*0.5, topleft + RIGHT*12.5+ DOWN*0.5)
        vline = Line(topleft + RIGHT*1.5 + UP*0.5, topleft + RIGHT*1.5 + DOWN*2.5)
        self.play(ShowCreation(hline), ShowCreation(vline))
        self.wait(1)

        self.play(ReplacementTransform(term2[1].copy(),row1[1]))
        self.play(ReplacementTransform(term2[3].copy(),row1[2]))
        self.play(ReplacementTransform(term2[5].copy(),row1[3]))
        self.wait(1)
        self.play(ReplacementTransform(term2[9].copy(),row2[0]))
        self.play(ReplacementTransform(term2[11].copy(),row3[0]))
        self.wait(1)

        #
        #  scene 4 : animation on multiplication table
        #
        self.wait(1)
        framebox1 = SurroundingRectangle(tex_table[1][0], buff = .1)
        for i in range (1, 3):
            # create a box for the term in the first column (on the left)
            # for subsequent rows, move the box down
            if i == 1:
                self.play(ShowCreation(framebox1))
            else:
                frameboxtemp = framebox1
                framebox1 = SurroundingRectangle(tex_table[i][0], buff = .1)
                self.play(ReplacementTransform(frameboxtemp, framebox1))
            self.wait(0.5)
            framebox2 = SurroundingRectangle(tex_table[0][1], buff = .1)
            for j in range (1, len(row1)):
                # create a box for the term in the first row (on top)
                # for subsequent columns, move the box to the right
                if j == 1:
                    self.play(ShowCreation(framebox2))
                else:
                    frameboxtemp = framebox2
                    framebox2 = SurroundingRectangle(tex_table[0][j], buff = .1)
                    self.play(ReplacementTransform(frameboxtemp,framebox2))
                self.wait(0.5)
                framebox3 = SurroundingRectangle(tex_table[i][j], buff = .1, color = BLUE)
                # highlight the entry and show the product
                self.play(
                    ReplacementTransform(framebox1.copy(), framebox3), 
                    ReplacementTransform(framebox2.copy(), framebox3)
                )
                self.play(Write(tex_table[i][j]))
                self.wait(0.5)
                self.play(FadeOut(framebox3))
            self.play(FadeOut(framebox2))
        self.play(FadeOut(framebox1))

        #
        #  scene 5 : simplify the entries in the table
        #
        for i in range (1, 3):
            for j in range (1, len(row1)):
                framebox = SurroundingRectangle(tex_table[i][j], buff = .1, color = GREEN)
                self.play(ShowCreation(framebox))
                self.play(ReplacementTransform(tex_table[i][j], tex_tables[i][j]))
                self.play(FadeOut(framebox))
        self.wait(1)

        #
        #  scene 6 : collect the terms
        #
        
        ans1 = TexMobject("=","(-3x^3)", "+", "(-6x^2)", "+", "12x", "+", "5x^2", "+", "10x", "+", "(-20)")
        ans1.to_edge(BOTTOM + LEFT).shift(0.8*DOWN)
        
        ans1up = ans1.copy()
        ans1up.to_edge(LEFT).shift(2.5*UP)
        for i in range (0,2):
            for j in range (0,3):
                # write sign
                self.play(Write(ans1[6*i+2*j]))
                # move the term to the sign
                self.play(ReplacementTransform(tex_tables[i+1][j+1], ans1[6*i + 2*j +1]))
        self.wait(1)

        #
        #  scene 7 : clear the table and simplify
        #

        self.play(FadeOut(row1[1]), FadeOut(row1[2]), FadeOut(row1[3]), FadeOut(row2[0]), FadeOut(row3[0]), FadeOut(hline), FadeOut(vline))
        self.play(ReplacementTransform(ans1, ans1up))
        self.wait(1)
        
        ans2 = TexMobject("=", "(-3x^3)", "+", "(-x^2)", "+", "22x", "+", "(-20)")
        ans2.to_edge(LEFT).shift(DOWN)

        self.play(Write(ans2[0]))
        # x^3
        ans1up[1].set_color(YELLOW)
        ans2[1].set_color(YELLOW)
        self.wait(0.5)
        self.play(ReplacementTransform(ans1up[1].copy(), ans2[1]))
        self.play(Write(ans2[2]))
        self.wait(1)
        # x^2
        ans1up[3].set_color(GREEN)
        ans1up[7].set_color(GREEN)
        ans2[3].set_color(GREEN)
        self.wait(0.5)
        self.play(ReplacementTransform(ans1up[3].copy(), ans2[3]), ReplacementTransform(ans1up[7].copy(), ans2[3]))
        self.play(Write(ans2[4]))
        self.wait(1)
        # x
        ans1up[5].set_color(RED)
        ans1up[9].set_color(RED)
        ans2[5].set_color(RED)
        self.wait(0.5)
        self.play(ReplacementTransform(ans1up[5].copy(), ans2[5]), ReplacementTransform(ans1up[9].copy(), ans2[5]))
        self.play(Write(ans2[6]))
        self.wait(1)
        # 1
        ans1up[11].set_color(BLUE)
        ans2[7].set_color(BLUE)
        self.wait(0.5)
        self.play(ReplacementTransform(ans1up[11].copy(), ans2[7]))
        self.wait(1)

        # simplify
        ans3 = TexMobject("=", "-3x^3", "-", "x^2", "+", "22x", "-", "20")
        ans3.to_edge(LEFT).shift(DOWN*2)
        
        self.play(Write(ans3[0]))
        self.wait(0.5)
        self.play(ReplacementTransform(ans2[1:].copy(), ans3[1:]))
        self.wait(1)
        frameboxfinal = SurroundingRectangle(ans3[1:], buff = .1)
        self.play(ShowCreation(frameboxfinal))
        self.wait(2)
