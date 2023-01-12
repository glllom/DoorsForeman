from django.db import models
from django.utils import timezone
from django.core.validators import validate_image_file_extension, MaxValueValidator


class DoorType(models.Model):
    name = models.CharField(max_length=16, help_text="שם הדלת",
                            verbose_name="שם הדלת:", unique=True, null=False, )
    image = models.ImageField(upload_to='images/door_types/', default='',
                              help_text="תמונת הדלת", verbose_name="סקיצה:", blank=True,
                              validators=[validate_image_file_extension])

    height_calculation = models.DecimalField(max_digits=4, decimal_places=1, help_text="הפחתה בגובה",
                                             verbose_name="הפחתה בגובה:", null=False, default=0,
                                             validators=[MaxValueValidator(0)])

    width_calculation = models.DecimalField(max_digits=4, decimal_places=1, help_text="הפחתה ברוחב",
                                            verbose_name="הפחתה ברוחב:", null=False, default=0,
                                            validators=[MaxValueValidator(0)])

    def __str__(self):
        return self.name


class Lock(models.Model):
    name = models.CharField(max_length=16, help_text="סוג המנעול", unique=True,
                            verbose_name="סוג המנעול:")
    compatible_doors = models.ManyToManyField('DoorType', help_text="דלתות מתאימות",
                                              verbose_name="סוגי דלתות תואמים:", blank=True)

    def __str__(self):
        return self.name


class Hinge(models.Model):
    name = models.CharField(max_length=16, help_text="סוג הצירים",
                            verbose_name="", unique=True)
    compatible_doors = models.ManyToManyField('DoorType', help_text="דלתות מתאימות",
                                              verbose_name="סוגי דלתות תואמים:", blank=True)

    def __str__(self):
        return self.name


class EngravingType(models.Model):
    name = models.CharField(max_length=16, help_text="", unique=True,
                            verbose_name="דוגמת החריטה")
    compatible_doors = models.ManyToManyField('DoorType', help_text="דלתות מתאימות",
                                              verbose_name="סוגי דלתות תואמים:", blank=True)

    image = models.ImageField(upload_to='images/engraving_types', default='',
                              help_text="תמונת החריטה", verbose_name="תמונת החריטה:")

    def __str__(self):
        return self.name


class Structure(models.Model):
    description = models.TextField(max_length="100", help_text="", verbose_name="תיאור המבנה:")
    compatible_doors = models.ManyToManyField('DoorType', help_text="דלתות מתאימות", blank=True,
                                              verbose_name="סוגי דלתות תואמים:")
    compatible_engraving = models.ManyToManyField('EngravingType', help_text="", blank=True,
                                                  verbose_name="סוגי דלתות תואמים:")
    image = models.ImageField(upload_to='images/structure',
                              help_text="תמונה", verbose_name="תמונה", blank=True)

    def __str__(self):
        return self.description


class Order(models.Model):
    id = models.IntegerField(verbose_name="מספר הזמנה", primary_key=True,
                             unique=True, help_text="")
    customer = models.CharField(max_length=16, help_text="",
                                verbose_name="לקוח")
    phone = models.CharField(max_length=16, help_text="",
                             verbose_name="טלפון", blank=True)
    address = models.CharField(max_length=64, help_text="",
                               verbose_name="כתובת", blank=True)
    date = models.DateField(default=timezone.now)
    casing = models.CharField(max_length=10, choices=(('regular', 'רגילות'), ('adjustable', 'מתכוונן')),
                              verbose_name="הלבשות",
                              help_text="")
    comment = models.TextField(max_length="100", help_text="", verbose_name="הערות", blank=True)
    door_type = models.ForeignKey('DoorType', on_delete=models.CASCADE,
                                  help_text="", verbose_name="סוג הדלתות")
    engraving = models.ForeignKey('EngravingType', on_delete=models.CASCADE,
                                  help_text="", verbose_name="דוגמא")
    lock = models.ForeignKey('Lock', on_delete=models.CASCADE,
                             help_text="", verbose_name="מנעול")
    hinges = models.ForeignKey('Hinge', on_delete=models.CASCADE,
                               help_text="", verbose_name="צירים")

    def __str__(self):
        return str(self.id) + ' ' + self.customer


class DoorsGroupInstance(models.Model):
    order = models.ForeignKey('Order', help_text="", on_delete=models.CASCADE,
                              verbose_name="")
    door_type = models.ForeignKey('DoorType', on_delete=models.CASCADE,
                                  help_text="", verbose_name="סוג הדלתות")
    engraving = models.ForeignKey('EngravingType', on_delete=models.CASCADE,
                                  help_text="", verbose_name="דוגמא")
    lock = models.ForeignKey('Lock', on_delete=models.CASCADE,
                             help_text="", verbose_name="מנעול")
    hinges = models.ForeignKey('Hinge', on_delete=models.CASCADE,
                               help_text="", verbose_name="צירים")


class DoorInstance(models.Model):
    group = models.ForeignKey('DoorsGroupInstance', on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1, verbose_name="מספר דלתות")
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="גובה",
                                 help_text="")
    width = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="רוחב",
                                help_text="")
    frame = models.DecimalField(max_digits=3, decimal_places=1, verbose_name="משקוף", default='10',
                                help_text="", blank=True)
    direction = models.CharField(max_length=4, choices=(('R', 'R'), ('L', 'L')),
                                 verbose_name="כיוון",
                                 help_text="")
    comment = models.TextField(max_length="1000", help_text="הערות", verbose_name="הערות", blank=True)

    def __str__(self):
        return f"{self.group.order.id}_{self.number}, |{self.width}x{self.height}/" \
               f"{self.frame} {self.direction}    {self.group.door_type.name},"

    class Meta:
        ordering = ["number"]
