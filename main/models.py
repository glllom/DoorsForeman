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

    covering_out_height_calculation = models.DecimalField(max_digits=4, decimal_places=1, help_text="הפחתה בגובה",
                                                          verbose_name="הפחתה בגובה:", null=False, default=0,
                                                          validators=[MaxValueValidator(0)])

    covering_out_width_calculation = models.DecimalField(max_digits=4, decimal_places=1, help_text="הפחתה ברוחב",
                                                         verbose_name="הפחתה ברוחב:", null=False, default=0,
                                                         validators=[MaxValueValidator(0)])

    covering_into_height_calculation = models.DecimalField(max_digits=4, decimal_places=1, help_text="הפחתה בגובה",
                                                           verbose_name="הפחתה בגובה:", null=False, default=0,
                                                           validators=[MaxValueValidator(0)])

    covering_into_width_calculation = models.DecimalField(max_digits=4, decimal_places=1, help_text="הפחתה ברוחב",
                                                          verbose_name="הפחתה ברוחב:", null=False, default=0,
                                                          validators=[MaxValueValidator(0)])

    binder_calculation = models.DecimalField(max_digits=4, decimal_places=1, help_text="הפחתה ברוחב",
                                             verbose_name="הפחתה ברוחב:", null=False, default=0,
                                             validators=[MaxValueValidator(0)])

    def __str__(self):
        return self.name


class Lock(models.Model):
    name = models.CharField(max_length=16, help_text="סוג המנעול", unique=True,
                            verbose_name="סוג המנעול:")
    compatible_doors = models.ManyToManyField('DoorType', help_text="דלתות מתאימות",
                                              verbose_name="סוגי דלתות תואמים:", blank=True)
    index = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Hinge(models.Model):
    name = models.CharField(max_length=16, help_text="סוג הצירים",
                            verbose_name="", unique=True)
    compatible_doors = models.ManyToManyField('DoorType', help_text="דלתות מתאימות",
                                              verbose_name="סוגי דלתות תואמים:", blank=True)
    index = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Accessories(models.Model):
    name = models.CharField(max_length=16, help_text="",
                            verbose_name="", unique=True)
    compatible_doors = models.ManyToManyField('DoorType', help_text="דלתות מתאימות",
                                              verbose_name="סוגי דלתות תואמים:", blank=True)
    index = models.CharField(max_length=16)

    def __str__(self):
        return self.name


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
    comment = models.TextField(max_length="100", help_text="", verbose_name="הערות", blank=True)
    door_type = models.ForeignKey('DoorType', on_delete=models.CASCADE,
                                  help_text="", verbose_name="סוג הדלתות")
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

    lock = models.ForeignKey('Lock', on_delete=models.CASCADE,
                             help_text="", verbose_name="מנעול")
    hinges = models.ForeignKey('Hinge', on_delete=models.CASCADE,
                               help_text="", verbose_name="צירים")


DIRECTION = [
    ('ימינה פנימה', 'ימינה פנימה'),
    ('שמאלה פנימה', 'שמאלה פנימה'),
    ('ימינה החוצה', 'ימינה החוצה'),
    ('שמאלה החוצה', 'שמאלה החוצה'),
]


class DoorInstance(models.Model):
    group = models.ForeignKey('DoorsGroupInstance', on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    quantity = models.IntegerField(default=1, verbose_name="מספר דלתות")
    height = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="גובה",
                                 help_text="")
    width = models.DecimalField(max_digits=4, decimal_places=1, verbose_name="רוחב",
                                help_text="")
    direction = models.CharField(max_length=16, choices=DIRECTION,
                                 verbose_name="כיוון",
                                 help_text="")
    mezuzah = models.BooleanField(verbose_name="מזוזה", default=False)
    closer = models.BooleanField(verbose_name="מחזיר שמן", default=False)
    comment = models.TextField(max_length="1000", help_text="הערות", verbose_name="הערות", blank=True)

    def __str__(self):
        return f"{self.group.order.id}_{self.number}, |{self.width}x{self.height}/" \
               f"{self.direction}    {self.group.door_type.name},"

    class Meta:
        ordering = ["number"]
