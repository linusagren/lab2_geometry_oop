from circle import Circle
from rectangle import Rectangle

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle as MplRectangle
from matplotlib.patches import Circle as MplCircle

class Shape2DPlotter():
    @staticmethod
    def plot2d(*shapes: Circle | Rectangle) -> tuple[plt.Figure, plt.Axes]:
        for shape in shapes:
            if not isinstance(shape, Circle | Rectangle):
                raise TypeError(f"Shape must be a Circle or Rectangle object, not {type(shape).__name__}")
    
        fig, axes = plt.subplots()

        for shape in shapes:
            if isinstance(shape, Rectangle):
                axes.add_patch(
                    MplRectangle(
                        xy=(shape.x - (shape.width / 2), shape.y - (shape.height / 2)), # x, y in Shape objects represent the center. Subtract half of width and height to match bottom-left
                        width=shape.width,
                        height=shape.height,
                        facecolor="none",
                        edgecolor="black"
                        )
                    )

            if isinstance(shape, Circle):
                axes.add_patch(
                    MplCircle(
                        xy=(shape.x, shape.y),
                        radius=shape.radius,
                        facecolor="none",
                        edgecolor="blue"
                        )
                    )

        # Equalize aspect ratio to prevent distorted shapes
        axes.autoscale_view(True)
        axes.set(aspect="equal")

        return fig, axes