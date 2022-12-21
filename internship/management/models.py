from django.db import models

# Create your models here.

class Login(models.Model):
    Loginid=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)

    def __str__(self) -> str:
       return self.Loginid

class CollegeSuper(models.Model):
    Co_id=models.AutoField(primary_key=True)
    CO_name=models.CharField(max_length=50)
    CO_addrss=models.CharField(max_length=50)
    CO_email=models.CharField(max_length=50)
    CO_pno=models.CharField(max_length=10)
    CO_prn=models.CharField(max_length=15)
    CO_gender=models.CharField(max_length=1)
    

    def __str__(self):
        return self.CO_name

class company(models.Model):
    C_id=models.AutoField(primary_key=True)   
    C_name=models.CharField(max_length=50)

    def __str__(self):
        return self.C_name

class compper(models.Model):
  P_id=models.AutoField(primary_key=True)
  P_fname=models.CharField(max_length=50)
  P_lname=models.CharField(max_length=50)
  P_email=models.CharField(max_length=70)
  P_pnol=models.CharField(max_length=11)
  P_gender=models.CharField(max_length=1)
  PC=models.ForeignKey(company,on_delete=models.DO_NOTHING)  

  def __str__(self):
    return self.P_fname+" "+self.P_lname      

# class faccom(models.Model):
#       f_id=models.AutoField(primary_key=True)
#       f_name=models.CharField(max_length=20)

class Student(models.Model):
    S_id=models.AutoField(primary_key=True)        
    S_fname=models.CharField(max_length=30)
    S_mname=models.CharField(max_length=30)
    S_lname=models.CharField(max_length=30)
    S_email=models.CharField(max_length=30)
    S_address=models.CharField(max_length=50)
    S_prn=models.CharField(max_length=15)
    S_geneder=models.CharField(max_length=1)
    S_contact=models.CharField(max_length=10,)
    SCO=models.ForeignKey(CollegeSuper,on_delete=models.DO_NOTHING,null=True,blank=True)
    SC=models.ForeignKey(company,on_delete=models.DO_NOTHING,null=True,blank=True)
    comper=models.ForeignKey(compper,on_delete=models.DO_NOTHING,null=True,blank=True)
    S_m=models.BooleanField(default=False)
    S_e=models.BooleanField(default=False)
    S_cm=models.BooleanField(default=False)
    S_ce=models.BooleanField(default=False)
    CE_C=models.BooleanField(default=False)
    CE_S=models.BooleanField(default=False)
    PE_S=models.BooleanField(default=False)
    PE_C=models.BooleanField(default=False)

    

    def __str__(self):
      return (self.S_fname + " " + self.S_lname)




class mideterm(models.Model):
 domainandtech=models.IntegerField()
 presentation=models.IntegerField()
 communication=models.IntegerField()
 questionans=models.IntegerField()
 total=models.IntegerField()
 SM=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
 SF=models.IntegerField()

 class Meta:
        unique_together = (("SM", "SF"),)
 
def __str__(self) -> str:
    return (self.SM.S_fname + " " + self.SM.S_lname)


class Endterm(models.Model):
 implemen=models.IntegerField()
 observa=models.IntegerField()
 present=models.IntegerField()
 communic=models.IntegerField()
 qanda=models.IntegerField()
 E_total=models.IntegerField()
 SE=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
 SEF=models.IntegerField()
 class Meta:
        unique_together = (("SE", "SEF"),)

 def __str__(self) -> str:
    return (self.SE.S_fname + " " + self.SE.S_lname)
    


class comeval(models.Model):
 problem=models.IntegerField()
 collect=models.IntegerField()
 Team=models.IntegerField()
 oralwrit=models.IntegerField()
 punctuality=models.IntegerField()
 CE_total=models.IntegerField()
 CE=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
 CEF=models.IntegerField()
 


 class Meta:
        unique_together = (("CE", "CEF"),)

 def __str__(self) -> str:
    return (self.CE.S_fname + " " + self.CE.S_lname)


class progresseval(models.Model):
 Taskperfo=models.IntegerField()
 workcomplete=models.IntegerField()
 Weekreport=models.IntegerField()
 repowrit=models.IntegerField()
 
 PE_total=models.IntegerField()
 PE=models.ForeignKey(Student,on_delete=models.DO_NOTHING)
 PEF=models.IntegerField()
 


 class Meta:
        unique_together = (("PE", "PEF"),)

 def __str__(self) -> str:
    return (self.PE.S_fname + " " + self.PE.S_lname)

