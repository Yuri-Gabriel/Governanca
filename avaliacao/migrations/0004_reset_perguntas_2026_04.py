from django.db import migrations


QUESTOES_POR_CATEGORIA = {
    "Alinhamento Estratégico": [
        "A TI participa do planejamento estratégico da organização?",
        "Projetos de TI são priorizados com base em objetivos estratégicos claros?",
        "Há indicadores que demonstram geração de valor da TI para o negócio?",
    ],
    "Cultura de TI": [
        "A equipe de TI compartilha conhecimento de forma estruturada?",
        "Existe cultura de inovação e melhoria contínua na TI?",
        "Há colaboração efetiva entre TI e demais áreas da empresa?",
    ],
    "Ferramentas de TI": [
        "A empresa utiliza ferramentas para monitoramento da infraestrutura e serviços?",
        "Existe automação relevante em rotinas operacionais ou integrações entre sistemas?",
        "Há gestão estruturada de ativos de TI com inventário atualizado?",
    ],
    "Gestão de Riscos": [
        "Riscos de TI e segurança da informação são identificados e tratados regularmente?",
        "Existe plano de continuidade, backup e recuperação testado periodicamente?",
        "Mudanças relevantes passam por análise de impacto e controles de risco?",
    ],
    "Governança de TI": [
        "Existem papéis, responsabilidades e decisões de TI formalmente definidos?",
        "A TI adota práticas ou frameworks reconhecidos (ex.: ITIL, COBIT, ISO 27001)?",
        "Há acompanhamento executivo dos resultados, riscos e investimentos de TI?",
    ],
    "Nível de Serviço": [
        "A área de TI possui SLAs ou metas de atendimento formalizadas?",
        "Os serviços críticos são monitorados continuamente quanto ao desempenho e disponibilidade?",
        "Usuários e áreas de negócio percebem consistência e previsibilidade nos serviços de TI?",
    ],
    "Processos de TI": [
        "Existem processos documentados para incidentes, mudanças e requisições?",
        "A TI mede e revisa periodicamente seus processos para melhoria contínua?",
        "As atividades críticas dependem mais do processo do que de pessoas específicas?",
    ],
}


def resetar_questoes(apps, schema_editor):
    Avaliacao = apps.get_model("avaliacao", "Avaliacao")
    CategoriaQuestao = apps.get_model("avaliacao", "CategoriaQuestao")
    Questao = apps.get_model("avaliacao", "Questao")

    # Limpeza solicitada: remove avaliações, questões e categorias existentes.
    Avaliacao.objects.all().delete()
    Questao.objects.all().delete()
    CategoriaQuestao.objects.all().delete()

    for nome_categoria, perguntas in QUESTOES_POR_CATEGORIA.items():
        categoria = CategoriaQuestao.objects.create(nome=nome_categoria, descricao="")
        for texto in perguntas:
            Questao.objects.create(categoria=categoria, texto=texto, ativa=True)


class Migration(migrations.Migration):
    dependencies = [
        ("avaliacao", "0003_empresa_owner"),
    ]

    operations = [
        migrations.RunPython(resetar_questoes, migrations.RunPython.noop),
    ]
