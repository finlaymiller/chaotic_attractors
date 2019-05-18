import c4d


def aizawa():
	object_name = "Aizawa Attractor"

	# Growth Parameters
	n = 100000  # Number of points to run for
	delta = 0.01  # Growth rate
	factor = 100  # Growth factor

	# Attractor Parameters
	x0 = 0.1  # Initial x coordinate
	y0 = 0.0  # Initial y coordinate
	z0 = 0.0  # Initial z coordinate
	a = 0.95
	b = 0.7
	c = 0.6
	d = 3.5
	e = 0.25
	f = 0.1

	# Create fresh spline object
	spline = c4d.SplineObject(n, c4d.SPLINETYPE_LINEAR)
	spline.SetName(object_name)

	# Initialize coordinates
	x = x0
	y = y0
	z = z0

	for i in range(n):
		# Calculate next step
		dx = (z - b) * x - d * y
		dy = (d * x) + (z - b) * y
		dz = c + (a * z) - ((z * z * z) / 3) - (x * x + y * y) * (1 + e * z) + (f * z * x * x * x)

		# Add next step to current location
		x = x + delta * dx
		y = y + delta * dy
		z = z + delta * dz

		# Grow spline
		spline.SetPoint(i, c4d.Vector(x * factor, y * factor, z * factor))

	return spline


# Main function
def main():
	spline = aizawa()
	doc.InsertObject(spline)
	doc.SetActiveObject(spline)
	c4d.EventAdd()
