from collections import defaultdict

from .models import LogAuditoriaResposta, Resposta, RespostaEscolha


def calcular_classificacao(score_geral: float) -> str:
    if score_geral <= 49:
        return "Artesanal (Reativo)"
    if score_geral <= 79:
        return "Eficiente (Proativo)"
    if score_geral <= 90:
        return "Eficaz (Otimizado)"
    return "Estratégico"


def gerar_relatorio(avaliacao):
    respostas = (
        Resposta.objects.filter(avaliacao=avaliacao)
        .select_related("questao__categoria")
        .order_by("questao__categoria__nome")
    )

    total = respostas.count()
    total_sim = respostas.filter(resposta=RespostaEscolha.SIM).count()
    score_geral = round((total_sim / total) * 100, 2) if total else 0
    classificacao = calcular_classificacao(score_geral)

    por_categoria = defaultdict(lambda: {"total": 0, "sim": 0})
    plano_acao = []

    for r in respostas:
        categoria = r.questao.categoria.nome
        por_categoria[categoria]["total"] += 1
        if r.resposta == RespostaEscolha.SIM:
            por_categoria[categoria]["sim"] += 1
        if r.resposta == RespostaEscolha.NAO and r.providencia:
            plano_acao.append(r)

    score_categoria = []
    for categoria, dados in por_categoria.items():
        score = round((dados["sim"] / dados["total"]) * 100, 2) if dados["total"] else 0
        score_categoria.append({"categoria": categoria, "score": score, "total": dados["total"]})

    return {
        "total_respondido": total,
        "score_geral": score_geral,
        "classificacao": classificacao,
        "score_categoria": sorted(score_categoria, key=lambda x: x["categoria"]),
        "plano_acao": plano_acao,
    }


def registrar_log_resposta(resposta: Resposta, usuario):
    nome_arquivo = resposta.evidencia_arquivo.name if resposta.evidencia_arquivo else ""
    LogAuditoriaResposta.objects.create(
        resposta_registro=resposta,
        usuario=usuario,
        resposta=resposta.resposta,
        evidencia_descricao=resposta.evidencia_descricao,
        evidencia_arquivo_nome=nome_arquivo,
        providencia=resposta.providencia,
    )


def progresso_avaliacao(avaliacao):
    total_questoes = avaliacao.total_questoes()
    respondidas = avaliacao.total_respostas()
    percentual = round((respondidas / total_questoes) * 100, 1) if total_questoes else 0
    return {"total_questoes": total_questoes, "respondidas": respondidas, "percentual": percentual}
