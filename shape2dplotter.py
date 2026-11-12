from circle import Circle
from rectangle import Rectangle

from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle as MplRectangle
from matplotlib.patches import Circle as MplCircle

class Shape2DPlotter:
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

        axes.autoscale_view(True) # Autoscale to fit all patches

        max_extent = Shape2DPlotter._get_max_extent(axes.get_xlim(), axes.get_ylim()) # Use furthest number from 0 to ensure (0, 0) stay centered

        axes.axhline(0, color="black")
        axes.axvline(0, color="black")
        
        # Equalize aspect ratio to prevent distorted shapes
        axes.set(aspect="equal", box_aspect=1, xlim=(-max_extent, max_extent), ylim=(-max_extent, max_extent))

        return fig, axes

    @staticmethod
    def _get_max_extent(x_limits: tuple[float, float], y_limits: tuple[float, float]) -> float:
        if type(x_limits) is not tuple or type(y_limits) is not tuple:
            raise TypeError("Input must be tuples.")

        if len(x_limits) != 2 or len(y_limits) != 2:
            raise ValueError("Tuple must contain exactly two values.")

        for value in *x_limits, *y_limits:
            if not isinstance(value, int | float) or isinstance(value, bool):
                raise TypeError(f"Value must be float or int, not {type(value).__name__}.")

        furthest_coordinate = max((*x_limits, *y_limits), key=abs)
        max_extent = abs(furthest_coordinate)

        if max_extent == 0:
            raise ValueError("Max extent must be greater than 0, not 0.")
        
        return max_extent