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
    CO_prn=models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.CO_name

class company(models.Model):
    C_id=models.AutoField(primary_key=True)   
    C_name=models.CharField(max_length=50)
    C_email=models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.C_name


class Student(models.Model):
    S_id=models.AutoField(primary_key=True)        
    S_fname=models.CharField(max_length=30)
    S_mname=models.CharField(max_length=30)
    S_lname=models.CharField(max_length=30)
    S_email=models.CharField(max_length=30)
    S_address=models.CharField(max_length=50,null=True,blank=True)
    S_prn=models.CharField(max_length=15,null=True,blank=True)
    S_geneder=models.CharField(max_length=1)
    S_contact=models.CharField(max_length=10,null=True,blank=True)
    SCO=models.ForeignKey(CollegeSuper,on_delete=models.DO_NOTHING,null=True,blank=True)
    SC=models.ForeignKey(company,on_delete=models.DO_NOTHING,null=True,blank=True)
    S_m=models.BooleanField(default=False)
    S_e=models.BooleanField(default=False)
    S_cm=models.BooleanField(default=False)
    S_ce=models.BooleanField(default=False)
    

    def __str__(self):
      return (self.S_fname + " " + self.S_lname)


class mideterm(models.Model):
 domainandtech=models.IntegerField()
 profesethi=models.IntegerField()
 interpersonatl=models.IntegerField()
 presentation=models.IntegerField()
 communication=models.IntegerField()
 taskcompleted=models.IntegerField()
 questionans=models.IntegerField()
 total=models.IntegerField()
 SM=models.ForeignKey(Student,on_delete=models.DO_NOTHING, primary_key = True)

 def __str__(self) -> str:
    return (self.SM.S_fname + " " + self.SM.S_lname)


class Endterm(models.Model):
 background=models.IntegerField()
 scopeandobj=models.IntegerField()
 implemen=models.IntegerField()
 observa=models.IntegerField()
 domain=models.IntegerField()
 present=models.IntegerField()
 communic=models.IntegerField()
 interper=models.IntegerField()
 profess=models.IntegerField()
 qanda=models.IntegerField()
 E_total=models.IntegerField()
 SE=models.ForeignKey(Student,on_delete=models.DO_NOTHING,primary_key = True)

 def __str__(self) -> str:
    return (self.SE.S_fname + " " + self.SE.S_lname)
    

class Cmideterm(models.Model):
 C_domainandtech=models.IntegerField()
 C_profesethi=models.IntegerField()
 C_interpersonatl=models.IntegerField()
 C_presentation=models.IntegerField()
 C_communication=models.IntegerField()
 C_taskcompleted=models.IntegerField()
 C_questionans=models.IntegerField()
 C_total=models.IntegerField()
 C_SM=models.ForeignKey(Student,on_delete=models.DO_NOTHING,primary_key = True)

 def __str__(self) -> str:
    return (self.C_SM.S_fname + " " + self.C_SM.S_lname)


class CEndterm(models.Model):
 C_background=models.IntegerField()
 C_scopeandobj=models.IntegerField()
 C_implemen=models.IntegerField()
 C_observa=models.IntegerField()
 C_domain=models.IntegerField()
 C_present=models.IntegerField()
 C_communic=models.IntegerField()
 C_interper=models.IntegerField()
 C_profess=models.IntegerField()
 C_qanda=models.IntegerField()
 C_E_total=models.IntegerField()
 C_SE=models.ForeignKey(Student,on_delete=models.DO_NOTHING, primary_key = True)

 def __str__(self) -> str:
    return (self.C_SE.S_fname + " " + self.C_SE.S_lname)



