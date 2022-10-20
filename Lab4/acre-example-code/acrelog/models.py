from django.db import models

# Types

TILLAGE_TYPES = [
	('till', 'Till'),
	('plow', 'Plow'),
	('rip', 'Rip'),
	('chisel', 'Chisel'),
	('rock pick', 'Rock Pick'),
	('disc', 'Disc')
]

TERMINATE_TYPES = [
	('terminate', 'Terminate'),
	('plow under', 'Plow Under'),
	('turn', 'Turn'),
	('mow', 'Mow'),
	('cut', 'Cut')
]

FERTILIZER_TYPES = [
	('fertilize', 'Fertilize'),
	('spray', 'Spray'),
	('inject', 'Inject'),
	('spread', 'Spread'),
	('sidedress', 'Sidedress')
]

TREATMENT_TYPES = [
	('treat', 'Treat'),
	('spray', 'Spray'),
	('apply', 'Apply'),
	('spread', 'Spread')
]

HARVEST_TYPES = [
	('harvest', 'Harvest'),
	('combine', 'Combine'),
	('reap', 'Reap'),
	('pick', 'Pick'),
	('glean', 'Glean'),
	('shell', 'Shell')
]

PLANTING_TYPES = [
	('planting', 'Planting'),
	('seed', 'Seed'),
	('transplant', 'Transplant'),
	('sow', 'Sow'),
	('fill in', 'Fill In')
]


# Classes

class Field(models.Model):
	field_name = models.CharField(max_length=200)
	field_id = models.CharField(max_length=20, default='NA')
	field_notes = models.CharField(max_length=1000, default='NA')
	def __str__(self):
		return self.field_name


class Tillage(models.Model):
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	tillage_name = models.CharField(max_length=200)
	tillage_notes = models.CharField(max_length=1000, default='NA')
	tillage_type = models.CharField(choices=TILLAGE_TYPES, max_length=100)
	tillage_date = models.DateTimeField('date of action')
	tillage_performer = models.CharField(max_length=100, default='NA')
	tillage_implement = models.CharField(max_length=100, default='NA')
	tillage_location = models.CharField(max_length=100, default='entire field')
	def __str__(self):
		return self.tillage_name

class Terminate(models.Model):
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	terminate_name = models.CharField(max_length=200)
	terminate_notes = models.CharField(max_length=1000, default='NA')
	terminate_type = models.CharField(choices=TERMINATE_TYPES, max_length=100)
	terminate_date = models.DateTimeField('date of action')
	terminate_performer = models.CharField(max_length=100, default='NA')
	terminate_implement = models.CharField(max_length=100, default='NA')
	terminate_location = models.CharField(max_length=100, default='entire field')
	def __str__(self):
		return self.terminate_name

class Fertilizer(models.Model):
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	fertilizer_name = models.CharField(max_length=200)
	fertilizer_notes = models.CharField(max_length=1000, default='NA')
	fertilizer_type = models.CharField(choices=FERTILIZER_TYPES, max_length=100)
	fertilizer_date = models.DateTimeField('date of action')
	fertilizer_performer = models.CharField(max_length=100, default='NA')
	fertilizer_chemical = models.CharField(max_length=100, default='NA')
	fertilizer_rate = models.FloatField('T/ha')
	fertilizer_location = models.CharField(max_length=100, default='entire field')
	def __str__(self):
		return self.fertilizer_name

class Treatment(models.Model):
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	treatment_name = models.CharField(max_length=200)
	treatment_notes = models.CharField(max_length=1000, default='NA')
	treatment_type = models.CharField(choices=TREATMENT_TYPES, max_length=100)
	treatment_date = models.DateTimeField('date of action')
	treatment_performer = models.CharField(max_length=100, default='NA')
	treatment_chemical = models.CharField(max_length=100, default='NA')
	treatment_rate = models.FloatField('T/ha')
	treatment_location = models.CharField(max_length=100, default='entire field')
	def __str__(self):
		return self.treatment_name

class Harvest(models.Model):
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	harvest_name = models.CharField(max_length=200)
	harvest_notes = models.CharField(max_length=1000, default='NA')
	harvest_type = models.CharField(choices=HARVEST_TYPES, max_length=100)
	harvest_date = models.DateTimeField('date of action')
	harvest_performer = models.CharField(max_length=100, default='NA')
	harvest_crop = models.CharField(max_length=100, default='NA')
	harvest_rate = models.FloatField('T/ha')
	harvest_location = models.CharField(max_length=100, default='entire field')
	def __str__(self):
		return self.harvest_name

class Install(models.Model):
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	install_name = models.CharField(max_length=200)
	install_notes = models.CharField(max_length=1000, default='NA')
	install_date = models.DateTimeField('date of action')
	install_performer = models.CharField(max_length=100, default='NA')
	install_location = models.CharField(max_length=100, default='entire field')
	def __str__(self):
		return self.install_name

class Planting(models.Model):
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	planting_name = models.CharField(max_length=200)
	planting_notes = models.CharField(max_length=1000, default='NA')
	planting_type = models.CharField(choices=PLANTING_TYPES, max_length=100)
	planting_date = models.DateTimeField('date of action')
	planting_performer = models.CharField(max_length=100, default='NA')
	planting_crop = models.CharField(max_length=100, default='NA')
	planting_rate = models.FloatField('seeds/m2')
	planting_location = models.CharField(max_length=100, default='entire field')
	def __str__(self):
		return self.planting_name