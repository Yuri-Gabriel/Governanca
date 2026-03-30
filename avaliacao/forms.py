from django import forms
from django.contrib.auth import get_user_model

from .models import Avaliacao, CategoriaQuestao, Empresa, Questao, Resposta, UserRole

User = get_user_model()


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["nome", "cnpj", "setor"]


class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ["categoria", "texto", "ativa"]


class CategoriaQuestaoForm(forms.ModelForm):
    class Meta:
        model = CategoriaQuestao
        fields = ["nome", "descricao"]
        widgets = {
            "descricao": forms.Textarea(attrs={"rows": 3}),
        }


class AvaliacaoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["consultor_responsavel"].queryset = User.objects.filter(profile__role=UserRole.CONSULTOR)
        self.fields["participantes"].queryset = User.objects.exclude(profile__role=UserRole.ADMIN)

    class Meta:
        model = Avaliacao
        fields = ["empresa", "nome", "consultor_responsavel", "participantes", "status"]
        widgets = {
            "participantes": forms.CheckboxSelectMultiple,
        }


class RespostaForm(forms.ModelForm):
    class Meta:
        model = Resposta
        fields = ["resposta", "evidencia_descricao", "evidencia_arquivo", "providencia"]
        widgets = {
            "evidencia_descricao": forms.Textarea(attrs={"rows": 3}),
            "providencia": forms.Textarea(attrs={"rows": 3}),
        }
