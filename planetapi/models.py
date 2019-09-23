from mongoengine import Document, StringField, IntField, ValidationError

class Planet(Document):
    _id = IntField(primary_key=True)
    nome = StringField(max_length=200, unique=True, required=True)
    clima = StringField(required=True)
    terreno = StringField(required=True)

    def json(self):
        planet_dict = {
            "id": self._id,
            "nome": self.nome,
            "clima": self.clima,
            "terreno": self.terreno
        }
        return planet_dict

    def clean(self):
        if str(self.nome).strip() == '':
            raise ValidationError('Campo nome não pode ser nulo')
        if str(self.clima).strip() == '':
            raise ValidationError('Campo clima não pode ser nulo')
        if str(self.terreno).strip() == '':
            raise ValidationError('Campo terreno não pode ser nulo')




