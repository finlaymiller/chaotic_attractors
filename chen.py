import c4d

"""
	Other initial coordinates:
	x	35.0	-10.33913519761
	y	3.0		-11.10031188035
	z	28.0	23.84877914089
"""


def chen():
	object_name = "Chen Attractor"

	# Growth Parameters
	N = 20000
	delta = 0.002
	factor = 5

	# Attractor Parameters
	x0 = 1.0  # Initial x coordinate
	y0 = 1.0  # Initial y coordinate
	z0 = 1.0  # Initial z coordinate
	a = 35
	b = 3
	c = 28

	# Create fresh spline object
	spline = c4d.SplineObject(N, c4d.SPLINETYPE_LINEAR)
	spline.SetName(object_name)

	# Initialize coordinates
	x = x0
	y = y0
	z = z0

	for i in range(N):
		# Calculate next step
		dx = a * (y - x)
		dy = (c - a) * x - x * z + c * y
		dz = x * y - b * z

		# Add next step to current location
		x = x + delta * dx
		y = y + delta * dy
		z = z + delta * dz

		# Grow spline
		spline.SetPoint(i, c4d.Vector(x * factor, y * factor, z * factor))

	return spline


# Main function
def main():
	spline = chen()
	doc.InsertObject(spline)
	doc.SetActiveObject(spline)
	c4d.EventAdd()
