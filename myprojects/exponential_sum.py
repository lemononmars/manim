#!/usr/bin/env python
from manim import *

# create new classes so that we can have it memorize its index
class LinkedLine(Line):
    def __init__(self, index = 0, **kwargs):
      self.index = index
      super().__init__(**kwargs)

class Trace(VMobject):
    def __init__(self, index = 0, **kwargs):
      self.index = index
      super().__init__(**kwargs)

class Pic(Scene):
   def construct(self):
      NUM_LINES = 20

      #starting configurations
      line_widths = [1/(1.2**x)*RIGHT for x in range(0,NUM_LINES)]
      Lines = [LinkedLine(start = ORIGIN, end = 5*RIGHT).to_edge(LEFT)]
      Traces = [VMobject()] #add a dummy object so that indices match with lines
      for i in range(1, NUM_LINES):
         Lines.append(
            LinkedLine(
               start = Lines[-1].get_end(), 
               end = Lines[-1].get_end() + line_widths[i], 
               index = i)
         )
         Traces.append(
            Trace(index = i).set_points_as_corners([Lines[-1].get_end(), Lines[-1].get_end()])
         )

      Lines_Group = VGroup(*Lines).set_submobject_colors_by_gradient(GREEN, ORANGE)
      Traces_Group = VGroup(*Traces).set_submobject_colors_by_gradient(GREEN, ORANGE)
      self.add(Lines_Group, Traces_Group)
      Lines_ref = Lines_Group.copy()

      # update each line
      def line_update_function(mob):
         prev_end = Lines_Group[mob.index-1].get_end()
         mob.become(Lines_ref[mob.index])
         mob.put_start_and_end_on(prev_end, prev_end + line_widths[mob.index])
         mob.rotate(
            theta_tracker.get_value() * mob.index, about_point = prev_end
         )

      # update each trace
      def trace_update_function(mob):
         newmob = mob.copy()
         newmob.add_points_as_corners([Lines[mob.index].get_end()])
         mob.become(newmob)
      
      # add updaters to the appropriate objects
      for i in range(1, NUM_LINES):
         Lines_Group[i].add_updater(line_update_function)
         Traces[i].add_updater(trace_update_function)

      # animate!
      theta_tracker = ValueTracker(0)
      self.play(ApplyMethod(theta_tracker.set_value, 2*PI), run_time=10)
      self.wait(1)