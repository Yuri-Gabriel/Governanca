from django import forms

from .models import Avaliacao, Empresa, Questao, Resposta


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ["nome", "cnpj", "setor"]


class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ["categoria", "texto", "ativa"]


class AvaliacaoForm(forms.ModelForm):
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
