import c4d
import math


def threelayer():
	# With these seettings you should be getting 6 layers
	object_name = "3-layer Attractor"

	# Growth Parameters
	n = 81500  # Number of points to run for
	ns = 2700
	delta = 0.002  # Growth rate
	factorx = 200  # Growth factor in x dimension
	factory = 200  # Growth factor in x dimension
	factorz = 150  # Growth factor in x dimension

	# Attractor Parameters
	x0 = -0.04  # Initial x coordinate
	y0 = -15.8  # Initial y coordinate
	z0 = -1.4  # Initial z coordinate
	a1 = -4.1
	a2 = 1.2
	a3 = 13.45
	c1 = 2.76
	c2 = 0.6
	c3 = 13.13
	d = 1.6

	# Create fresh spline object
	spline = c4d.SplineObject(n, c4d.SPLINETYPE_LINEAR)
	spline.SetName(object_name)

	# Initialize coordinates
	x = x0
	y = y0
	z = z0

	# Calculate constants
	b = ((d * a2 * a2 * c3 * c3) / (32 * a3 * a3 * c2 * c2)) * math.sqrt((- a3 * c2) / (a1 * c1))
	c = ((a2 * a2 * c3 * c3) / (4 * a3 * c2) - (a3 * c1 + a1 * c2) * b / d) / a2

	for i in range(n):
		# Calculate next step
		dx = a1 * x - a2 * y + a3 * z
		dy = -d * x * z + b
		dz = c1 * x * y + c2 * y * z + c3 * z + c

		# Add next step to current location
		x = x + delta * dx
		y = y + delta * dy
		z = z + delta * dz

		# Grow spline
		spline.SetPoint(i, c4d.Vector(x * factorx, y * factory, z * factorz))

	return spline


# Main function
def main():
	spline = threelayer()
	doc.InsertObject(spline)
	doc.SetActiveObject(spline)
	c4d.EventAdd()
