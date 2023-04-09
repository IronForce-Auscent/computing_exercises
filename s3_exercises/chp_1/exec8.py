"""
An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos in an order from the user. Then your program
should compute and display the total weight of the order
"""
def order_mass_calculator(widget_count: int, gizmo_count: int):
  widget, gizmo = 75, 122
  print(f"The total weight of the order is {(widget_count * widget) + (gizmo_count * gizmo)}")