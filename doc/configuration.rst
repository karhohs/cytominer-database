Configuration
=============

.. code-block:: ini

	[filenames]
	image = image.csv
	object = object.csv
	experiment = Experiment.csv
	reference_pattern = Cells.csv

	[metadata]
	plate = Metadata_Barcode
	well = Metadata_Well

	[qualities]
	count_cell_clump = Metadata_isCellClump
	count_debris = Metadata_isDebris
	count_low_intensity = Metadata_isLowIntensity
