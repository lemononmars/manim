from manim import *

class StreamOpening(Scene):

    def change_background_color(self, color_target):
        base_color = self.camera.background_color
        def update_bc(mob, alpha):
            self.camera.background_color = \
                interpolate_color(base_color, color_target, alpha)
        return UpdateFromAlphaFunc(Mobject(), update_bc)

    def construct(self):
        self.camera.background_color = YELLOW_A
        target_color = GREEN
        Pawn = ImageMobject("Trophy")

        self.play(FadeIn(Pawn), self.change_background_color(target_color), run_time = 5)
        self.wait()