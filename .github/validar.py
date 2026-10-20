#!/usr/bin/env python3
"""Confere a estrutura da skill humanizador-pt.
Uso: python3 .github/validar.py [caminho da pasta da skill]
Sem argumento, usa a pasta acima de .github. Sai com codigo 1 se houver falha."""
import os, re, sys, unicodedata

repo = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
falhas, avisos, ok = [], [], []

def falha(m): falhas.append(m)
def aviso(m): avisos.append(m)
def passou(m): ok.append(m)

def ler(p):
    with open(p, encoding="utf-8") as f:
        return f.read()

# 0. arquivos obrigatorios e inesperados
for obrig in ["SKILL.md", "README.md", "LICENSE", ".gitignore"]:
    (passou if os.path.isfile(os.path.join(repo, obrig)) else falha)(f"arquivo obrigatorio: {obrig}")
todos = []
for raiz, dirs, files in os.walk(repo):
    dirs[:] = [d for d in dirs if d not in (".git", ".github")]
    for f in files:
        todos.append(os.path.join(raiz, f))
for p in todos:
    rel = os.path.relpath(p, repo)
    base = os.path.basename(p)
    if base in (".DS_Store",) or base.endswith((".log", ".tmp")):
        falha(f"arquivo que nao deve subir: {rel}")
    elif not (base in ("LICENSE", ".gitignore") or base.endswith(".md")):
        aviso(f"extensao inesperada: {rel}")
    if "_dev" in rel.split(os.sep):
        falha(f"conteudo de _dev dentro do repo: {rel}")

# 1. SKILL.md: frontmatter
skill = ler(os.path.join(repo, "SKILL.md"))
m = re.match(r"^---\n(.*?)\n---\n", skill, re.S)
if not m:
    falha("SKILL.md sem frontmatter")
else:
    fm = m.group(1)
    nome = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    desc = re.search(r"^description:\s*(.+)$", fm, re.M)
    (passou if nome and nome.group(1) == os.path.basename(os.path.abspath(repo)) else falha)("name igual ao nome da pasta")
    if desc:
        d = desc.group(1).strip()
        if len(d) >= 2 and d[0] == d[-1] == '"':
            d = d[1:-1]
        (passou if len(d) <= 1024 else falha)(f"description <= 1024 caracteres ({len(d)})")
        (passou if not re.search(r"[<>]", d) else falha)("description sem angulos")
        # Limite assumido: 1024 (especificacao e API). A central de ajuda cita 200; se um upload falhar, rever.
        passou(f"description com {len(d)} caracteres (limite assumido 1024)")
    else:
        falha("description ausente")
    # YAML valido: valor sem aspas nao pode ter ": " nem " #" (quebra o frontmatter)
    for linha in fm.splitlines():
        mm = re.match(r"^([A-Za-z_-]+):\s+(.*)$", linha)
        if mm and mm.group(2) and mm.group(2)[0] not in "\"'|>[{":
            (falha if (": " in mm.group(2) or " #" in mm.group(2)) else passou)(f"frontmatter YAML valido: {mm.group(1)}")
    try:
        import yaml
        yaml.safe_load(fm)
        passou("frontmatter lido por parser YAML")
    except ImportError:
        pass
    except Exception as e:
        falha(f"frontmatter nao e YAML valido: {str(e).splitlines()[0]}")
    for proibido in ["allowed-tools", "hooks", "disable-model-invocation"]:
        (passou if proibido not in fm else falha)(f"frontmatter sem {proibido}")
n_linhas = skill.count("\n") + 1
(passou if n_linhas <= 80 else falha)(f"SKILL.md enxuto ({n_linhas} linhas, limite 80)")

# 2. referencias do SKILL.md existem
refs = set(re.findall(r"`(references/[^`\s]+)`", skill))
for r in sorted(refs):
    alvo = os.path.join(repo, r)
    (passou if os.path.exists(alvo) else falha)(f"referencia existe: {r}")

# 3. indice x arquivos de estilo
est_dir = os.path.join(repo, "references", "estilos")
indice = ler(os.path.join(est_dir, "indice.md"))
linhas = re.findall(r"^\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|", indice, re.M)
nums = [int(n) for n, _, _ in linhas]
(passou if nums == list(range(1, len(nums) + 1)) else falha)(f"numeracao do indice continua 1..{len(nums)}")
(passou if len(linhas) == 38 else falha)(f"indice com 38 estilos (achou {len(linhas)})")
arquivos_idx = {a for _, _, a in linhas}
arquivos_dir = {f for f in os.listdir(est_dir) if f.endswith(".md") and f != "indice.md"}
(passou if arquivos_idx == arquivos_dir else falha)("indice e pasta de estilos listam os mesmos arquivos")
for a in sorted(arquivos_idx - arquivos_dir): falha(f"indice cita arquivo inexistente: {a}")
for a in sorted(arquivos_dir - arquivos_idx): falha(f"arquivo fora do indice: {a}")

# 4. cada estilo: titulo com numero certo e secoes obrigatorias
for n, nome_estilo, arq in linhas:
    p = os.path.join(est_dir, arq)
    if not os.path.isfile(p):
        continue
    t = ler(p)
    titulo = t.splitlines()[0]
    if not titulo.startswith(f"# {n}. "):
        falha(f"{arq}: titulo deveria comecar com '# {n}. ' (achou: {titulo})")
    for sec in ["## O que é", "## Use quando", "## Evite", "## Fidelidade"]:
        if sec not in t:
            falha(f"{arq}: falta secao '{sec}'")
    if "Amostra" not in t:
        falha(f"{arq}: sem amostra")
    if arq != "pessoa-tres-vozes.md" and "## Traços de forma" not in t:
        falha(f"{arq}: falta '## Traços de forma'")
    if arq != "pessoa-tres-vozes.md" and "Fato-base:" not in t:
        falha(f"{arq}: amostra sem fato-base")
    if len(t.split()) < 150:
        aviso(f"{arq}: descricao curta ({len(t.split())} palavras)")
passou("verificacao por estilo executada em %d arquivos" % len(linhas))

# 5. caracteres ocultos, BOM, links relativos, dados pessoais, segredos
trav = []
for p in todos:
    if not p.endswith(".md") and os.path.basename(p) not in ("LICENSE", ".gitignore"):
        continue
    rel = os.path.relpath(p, repo)
    bruto = open(p, "rb").read()
    if bruto.startswith(b"\xef\xbb\xbf"):
        falha(f"{rel}: BOM")
    t = bruto.decode("utf-8")
    for i, ch in enumerate(t):
        if unicodedata.category(ch) in ("Cf", "Cc") and ch not in "\n\t":
            falha(f"{rel}: caractere oculto U+{ord(ch):04X} na posicao {i}")
    if "—" in t or "–" in t:
        trav.append((rel, t.count("—") + t.count("–")))
    for l in re.findall(r"\]\(([^)]+)\)", t):
        if l.startswith(("http", "#")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), l))):
            falha(f"{rel}: link relativo quebrado {l}")
    for l in re.findall(r"`(\.\./[^`\s]+)`", t):
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(p), l))):
            falha(f"{rel}: caminho relativo quebrado {l}")
    padrao_local = r"/Users/|C:\\\\" if rel == ".gitignore" else r"/Users/|C:\\\\|_dev"
    if re.search(padrao_local, t):
        falha(f"{rel}: caminho local ou referencia a _dev")
    if rel != "LICENSE" and re.search(r"\bSergio\b", t):
        aviso(f"{rel}: nome pessoal no texto")
    if re.search(r"(sk-[A-Za-z0-9]{20,}|api[_-]?key\s*[:=]\s*\S{8,}|token\s*[:=]\s*\S{12,}|ghp_[A-Za-z0-9]{20,})", t, re.I):
        falha(f"{rel}: possivel segredo")
passou("varredura de caracteres ocultos, links, caminhos locais e segredos executada")
for rel, n in trav:
    aviso(f"{rel}: {n} travessao(oes), confirmar que sao exemplos de padrao")

print(f"OK ({len(ok)})")
for m in ok: print("  +", m)
print(f"AVISOS ({len(avisos)})")
for m in avisos: print("  ~", m)
print(f"FALHAS ({len(falhas)})")
for m in falhas: print("  !", m)
sys.exit(1 if falhas else 0)
