from django.db import migrations


QUESTOES_POR_CATEGORIA = {
    "Nível 1: Artesanal (Reativo)": [
        "As solicitações de suporte são feitas predominantemente de forma informal (conversa, chat pessoal) em vez de um canal centralizado?",
        "A maior parte do tempo da equipe de TI é gasta resolvendo problemas urgentes e imprevistos (“apagando incêndios”)?",
        "O conhecimento técnico sobre sistemas e infraestrutura reside apenas com indivíduos específicos, sem documentação formal?",
        "A empresa carece de um planejamento de TI para os próximos 12 meses?",
        "Os processos operacionais da TI são realizados manualmente, sem o apoio de ferramentas de integração?",
    ],
    "Nível 2: Eficiente (Proativo)": [
        "A TI utiliza processos baseados em frameworks de mercado, como o ITIL, para gerenciar incidentes?",
        "Existem ferramentas de monitoramento ativas que alertam a equipe antes que um problema afete o usuário final?",
        "Há um inventário atualizado e automatizado de todos os ativos de hardware e licenças de software?",
        "A organização possui políticas de segurança da informação documentadas e conhecidas pelos colaboradores?",
        "Já existe algum nível de integração automatizada entre os principais sistemas da empresa?",
    ],
    "Nível 3: Eficaz (Otimizado)": [
        "Os indicadores de desempenho da TI (KPIs) estão diretamente vinculados aos objetivos de negócio da empresa?",
        "Existe um processo de melhoria contínua onde as falhas são analisadas para gerar inovações nos processos?",
        "A gestão de riscos de TI é realizada periodicamente e reportada à diretoria?",
        "A infraestrutura de TI é monitorada continuamente com foco em alta disponibilidade e desempenho?",
        "A governança de TI está estabelecida e participa das decisões de investimentos da organização?",
    ],
    "Nível 4: Estratégico": [
        "A TI é consultada e participa ativamente da criação de novas estratégias ou produtos da empresa?",
        "A infraestrutura é altamente resiliente e capaz de escalar automaticamente conforme a demanda do negócio?",
        "Os processos de TI e de negócio são quase totalmente automatizados e integrados entre si?",
        "A tecnologia é utilizada de forma inovadora para criar diferenciais competitivos no mercado?",
        "Existe uma cultura consolidada de colaboração e compartilhamento de conhecimento entre a TI e as demais áreas?",
    ],
}


def seed_questoes(apps, schema_editor):
    CategoriaQuestao = apps.get_model("avaliacao", "CategoriaQuestao")
    Questao = apps.get_model("avaliacao", "Questao")

    for nome_categoria, perguntas in QUESTOES_POR_CATEGORIA.items():
        categoria, _ = CategoriaQuestao.objects.get_or_create(
            nome=nome_categoria,
            defaults={"descricao": ""},
        )
        for texto in perguntas:
            Questao.objects.get_or_create(
                categoria=categoria,
                texto=texto,
                defaults={"ativa": True},
            )


def unseed_questoes(apps, schema_editor):
    CategoriaQuestao = apps.get_model("avaliacao", "CategoriaQuestao")
    Questao = apps.get_model("avaliacao", "Questao")

    for nome_categoria, perguntas in QUESTOES_POR_CATEGORIA.items():
        categoria = CategoriaQuestao.objects.filter(nome=nome_categoria).first()
        if not categoria:
            continue
        Questao.objects.filter(categoria=categoria, texto__in=perguntas).delete()
        if not Questao.objects.filter(categoria=categoria).exists():
            categoria.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("avaliacao", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_questoes, unseed_questoes),
    ]
