from django.db import models

class client(models.Model):
    AREA = (
        ('Mixing', 'Mixing'),
        ('Hot Prep', 'Hot Prep'),
        ('Cold Prep', 'Cold Prep'),
        ('Tire Building', 'Tire Building'),
        ('Curing', 'Curing'),
        ('Final Finishing', 'Final Finishing', )
    )

    PLANT = (
        ('PLT', 'PLT'),
        ('TT', 'TT'),
        ('SHARED', 'SHARED')
    )

    name = models.CharField(max_length=100,null=True)
    area = models.CharField(max_length=100,null=True,choices=AREA)
    plant = models.CharField(max_length=100, null=True,choices=PLANT)
    dept = models.CharField(max_length=100,null=True)
    email = models.EmailField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tbl_client"

class changerequest(models.Model):
    request = models.CharField(max_length=100,null=True)
    description = models.CharField(max_length=400,null=True)
    status = models.CharField(max_length=15,null=True)
    requestedby = models.ForeignKey(client, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.request

    class Meta:
        db_table = "tbl_changerequest"