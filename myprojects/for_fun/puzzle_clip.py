from manimlib.imports import *
import numpy as np

class Puzzle(Scene):
    CONFIG={
		"camera_config":{
            "background_color":"#f8f1f1", #puzzle background theme
            "frame_height": 10.0,
            "frame_width": 10.0            
            }
	}

    def construct(self):
        # add logo and bottom layer 
        banner = ImageMobject(".\img\\bottom_banner.png").scale(0.47)
        banner.shift(4.6*DOWN)
        self.add_foreground_mobject(banner) 
        bgsquare = Square(side_length = 4, color = "#16c79a", fill_opacity = 1).to_corner(LEFT+UP).shift(UP*4+0.5*LEFT).rotate(TAU/8)
        # messed up due to dimension change.... there must be a better way.... 
        num = Text("25", font = "Impact").set_color(WHITE).scale(2).next_to(bgsquare).shift(2.8*LEFT+DOWN*1.2)
        bgsquare.set_z(1)
        num.set_z(-1)
        banner.set_z(1)
        self.add_foreground_mobjects(bgsquare, num)

        # make hexagonal grid 
        r = 4
        R = RIGHT*r
        UR = RIGHT*r/2 + UP*r*(np.sqrt(3))/2
        
        # add dot as first hint
        d = Dot(radius=0.1, color = "#16c79a", fill_opacity = 1)
        dot1 = d.copy().shift(R)
        dot2 = d.copy().shift(UR)
        dot3 = d.copy().shift(-R+UR)
        dot4 = d.copy().shift(-R)
        dot5 = d.copy().shift(-UR)
        dot6 = d.copy().shift(R-UR)
        
        dots = [dot1, dot2, dot3, dot4, dot5, dot6]
        self.add(*dots)
        self.play(AnimationGroup(*[ 
            ShowCreationThenFadeOut(d, run_time = 0.15)
            for d in dots
            ],
            lag_ratio = 0.1
        ))
        
        imA = ImageMobject(".\img\A.png")
        imB = ImageMobject(".\img\B.png")
        imC = ImageMobject(".\img\C.png")
        imD = ImageMobject(".\img\D.png")
        imE = ImageMobject(".\img\E.png")
        imF = ImageMobject(".\img\F.png")
        ims = [imA, imB, imC, imD, imE, imF]
        for i in ims:
            i.scale(1.2) 
        #TODO - use SVG instead?

        

        pathA = Line((-2)*R+2*UR, 2*R+(-2)*UR)
        pathB = Arc(radius = r, arc_center = UR-R, angle = 2*TAU, start_angle = TAU/6)
        pathC = Arc(radius = r, arc_center = R-UR, angle = 2*TAU, start_angle = -TAU/6)
        pathD = Arc(radius = r, arc_center = R, angle = 2*TAU, start_angle = 0)
        pathE = Line((-2)*R, 2*R)
        pathF = Arc(radius = r, arc_center = -R, angle = 2*TAU, start_angle = TAU/2)
        paths = [pathA, pathB, pathC, pathD, pathE, pathF]

        rates = [there_and_back, linear, linear, linear, there_and_back, linear]
        # DEBUG: display paths
        #self.add(*paths)
        #self.add(*ims)
        #self.wait(1)
        
        self.play(AnimationGroup(*[
            MoveAlongPath(x, y, rate_func = z, run_time = 6)
            for (x, y, z) in zip(ims, paths, rates)
            ],
            lag_ratio = 0.2
        ))
        self.wait(1)
        