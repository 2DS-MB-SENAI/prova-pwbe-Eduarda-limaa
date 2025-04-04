from django.db import models

class Medico(models.Model):
    nome= models.CharField(max_length=20, null=True)
    especialidade= models.CharField(max_length=20, choices= [('Nutri', 'Nutricionista'), ('Derm', 'Dermatologista') ])
    crm= models.CharField(max_length= 30, null=True, unique=True)
    email= models.EmailField(blank= True, null= True)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    paciente= models.CharField(max_length=20)
    data= models.DateTimeField()
    medico= models.ForeignKey(Medico, on_delete=models.CASCADE)
    status= models.CharField(max_length=20, choices=[('Agen', 'Agendado'), ('R', 'Realizado'), ('C', 'Cancelado')])

    def __str__(self):
        return f" {self.paciente} Sua consulta será com: {self.medico}, será no dia: {self.data}. E ta com o status: {self.status}"