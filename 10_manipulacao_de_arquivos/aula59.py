"""
Criando email e disparando pdf
"""


import os
import smtplib
from email.message import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Função para criar o PDF
def criar_pdf(nome_arquivo, texto):
    doc = SimpleDocTemplate(nome_arquivo, pagesize=letter)
    styles = getSampleStyleSheet()
    style_normal = styles['Normal']
    style_normal.textColor = colors.black
    conteudo = []
    paragrafos = texto.split("\n\n")
    for paragrafo in paragrafos:
        p = Paragraph(paragrafo, style_normal)
        conteudo.append(p)
    doc.build(conteudo)

# Função para enviar o email
def enviar_email(para, assunto, corpo, anexo):
    msg = EmailMessage()
    msg.set_content(corpo)
    msg['Subject'] = assunto
    msg['From'] = 'seu_email@gmail.com'
    msg['To'] = para

    with open(anexo, 'rb') as arquivo_anexo:
        anexo_dados = arquivo_anexo.read()
        msg.add_attachment(anexo_dados, maintype='application', subtype='pdf', filename=os.path.basename(anexo))

    servidor = smtplib.SMTP('smtp.gmail.com', 587)
    servidor.starttls()
    servidor.login('juliozulu2008@gmail.com', 'dnxl jayh xcex wxqk')
    servidor.send_message(msg)
    servidor.quit()

# Texto para o PDF
texto_para_pdf = """
Resumo do Livro O Pequeno Príncipe\n"
         "O autor do livro é o personagem principal da história, que assume também o papel de narrador, "
         "contando sobre o fatídico dia em que o seu avião teria caído no meio do deserto do Saara.\n"
         "\n"
         "Lá, o personagem principal adormece e, ao acordar, se depara com o Pequeno Príncipe, que pede para que ele "
         "desenhe um cordeiro numa folha de papel.\n"
         "\n"
         "O protagonista é frustrado em relação aos seus desenhos, pois nunca ninguém conseguia interpretar as suas "
         "artes da forma correta.\n"
         "\n"
         "Ao longo da história, o Pequeno Príncipe vai narrando as suas aventuras para o protagonista.\n"
         "\n"
         "O jovem estaria a procura de um carneiro para comer as árvores que estariam crescendo em excesso em sua terra, um asteroide conhecido por B 612, que teria apenas uma rosa vermelha e três vulcões, sendo um deles inativo.\n"
         "\n"
         "Ao ouvir as aventuras do Pequeno Príncipe, o protagonista vai percebendo como as pessoas deixam de dar valor as pequenas coisas da vida conforme vão crescendo.\n"
         "\n"
         "Primeira edição de O pequeno príncipe publicada nos Estados Unidos em 1943.\n"
         "Primeira edição de O pequeno príncipe publicada nos Estados Unidos, em 1943 (Imagem: Fondation JMP/LPP)\n"
         "Análise de Frases do Livro O Pequeno Príncipe\n"
         "A parábola do \"Pequeno Príncipe\" debate, entre outras questões filosóficas, a perda da inocência e fantasia ao longo dos anos, conforme as pessoas vão crescendo e abandonando a infância.\n"
         "\n"
         "Descubra abaixo as frases mais importantes que norteiam a obra e dão a ela uma profundidade ímpar:\n"
         "\n"
         "\"O essencial é invisível aos olhos, e só se pode ver com o coração.\"\n"
         "\n"
         "Esta obra literária aborda em várias partes o valor das coisas. Através desta afirmação da Raposa, podemos concluir que o verdadeiro valor de algo ou de alguém não pode ser visto com uma visão superficial.\n"
         "\n"
         "Para conhecer o que é essencial é preciso ver com o coração, ou seja, tirar tempo para conhecer, olhar sem preconceito e sem discriminar.\n"
         "\n"
         "\"Foi o tempo que dedicaste à tua rosa que a fez tão importante.\"\n"
         "\n"
         "Esta frase descreve o laço afetivo existente entre o Pequeno Príncipe e a Rosa. Podemos concluir com esta frase que o que torna as coisas ou pessoas importantes é o tempo que nós investimos nelas. Quanto mais tempo, mais importante se torna nas nossas vidas.\n"
         "\n"
         "\"Se tu vens, por exemplo, às quatro da tarde, desde às três eu começarei a ser feliz.\"\n"
         "\n"
         "Com esta declaração, a Raposa expressa o carinho que sente pelo Pequeno Príncipe.\n"
         "\n"
         "O mesmo acontece entre pessoas que gostam uma da outra, existe esse sentimento de antecipação quando se sabe que vai haver um encontro.\n"
         "\n"
         "\"As pessoas são solitárias porque constroem muros ao invés de pontes.\"\n"
         "\n"
         "As duas estruturas mencionadas (muros e pontes) servem para designar atitudes no contexto da interação social.\n"
         "\n"
         "Os muros servem para criar uma separação entre dois lugares, enquanto as pontes têm a função oposta, ou seja, são construídas para conectar dois lugares. Assim, quem é solitário se afasta das outras pessoas, construindo muros e não pontes.\n"
         "\n"
         "\"É loucura odiar todas as rosas porque uma te espetou.\"\n"
         "\n"
         "Esta frase revela o perigo e a insensatez de generalizar, julgar e avaliar uma pessoa por alguma coisa que aconteceu no passado. Isso também pode ser aplicado ao tópico da discriminação e preconceito racial.\n"
         "\n"
         "Só porque alguém foi magoado por uma pessoa de uma determinada classe, raça, gênero ou grupo social, não significa que todas as pessoas são iguais.\n"
         "\n"
         "\"Tu te tornas eternamente responsável por aquilo que cativas.\"\n"
         "\n"
         "O fenômeno de “cativar” algo ou alguém é amplamente abordado neste livro. Esta frase explica que, quando é formado um relacionamento (seja ele amoroso ou de amizade), as pessoas se cativam e ao cativar, são responsáveis por ela. Isso significa que o amor ou amizade requerem responsabilidade.\n"
         "\n"
         "O Pequeno Príncipe cativou a Rosa e por esse motivo tornou-se responsável por ela, dando resposta aos seus desejos e caprichos.\n"
         "\n"
         "Personagens do Livro O Pequeno Príncipe\n"
         "O Pequeno Príncipe\n"
         "O personagem que dá o nome ao livro é um dos dois protagonistas da história. Esta criança vem do asteroide 325 (conhecido na Terra como B-612) e deixa a sua casa e a sua querida rosa para viajar pelo Universo.\n"
         "\n"
         "Nos vários planetas que visita, tem contacto pela primeira vez com adultos e fica espantado com o comportamento adulto e com as suas incoerências.\n"
         "\n"
         "O Pequeno Príncipe representa a infância inconsciente dentro de cada adulto, simbolizando sentimentos de amor, esperança e inocência.\n"
         "\n"
         "O Piloto\n"
         "Assume o protagonismo da história juntamente com o Pequeno Príncipe e tem a função de narrador.\n"
         "\n"
         "Quando era criança, o piloto tinha o sonho de ser um artista, mas foi desencorajado por adultos à sua volta. Apesar disso, o piloto faz vários desenhos para o Pequeno Príncipe e revela que a sua visão do mundo é mais parecida com a de uma criança.\n"
         "\n"
         "O piloto simboliza a atitude de perseguir e lutar pelos sonhos. A sua busca pelo poço no deserto revela a importância de aprender as lições através da exploração pessoal.\n"
         "\n"
         "A Rosa\n"
         "Elemento que é objeto do amor do Pequeno Príncipe, mas graças ao seu comportamento contraditório faz com que ele parta em viagem.\n"
         "\n"
         "A Rosa tem uma atitude melodramática e orgulhosa e é simultaneamente convencida e ingênua. O Pequeno Príncipe cede aos seus caprichos e, como cuida muito bem da Rosa, a sua memória faz com que queira regressar ao seu lar.\n"
         "\n"
         "Ela simboliza, portanto, o amor que deve ser cultivado e cuidado. Apresenta características humanas, tanto boas como más.\n"
         "\n"
         "A Raposa\n"
         "Aparece na história de forma repentina e misteriosa e estabelece um relacionamento de amizade com o Pequeno Príncipe.\n"
         "\n"
         "Apesar de pedir para ser domada pelo seu amigo, a raposa atua não só como pupila, mas como sua tutora, ensinando-lhe valiosas lições.\n"
         "\n"
         "Representa a sabedoria pois ensina valiosas lições ao rapazinho, sendo as mais importantes: só o coração consegue ver corretamente; o tempo que o Pequeno Príncipe passou longe do seu planeta fez com que valorizasse mais a Rosa; o amor implica uma responsabilidade.\n"
         "\n"
         "Conheça mais sobre a personagem lendo o artigo Significado da Raposa de O Pequeno Príncipe.\n"
         "\n"
         "O Carneiro e a Caixa\n"
         "Quando o Pequeno Príncipe pediu ao Piloto para desenhar um carneiro, não ficou satisfeito com o resultado. Assim, o Piloto desenhou uma caixa, afirmando que dentro dela vivia o carneiro que o Pequeno Príncipe tinha pedido para desenhar.\n"
         "\n"
         "A caixa simboliza o poder da imaginação, capaz de ajudar a contornar problemas que aparecem no dia a dia.\n"
         "\n"
         "O Pequeno Príncipe fica preocupado que o carneiro coma a sua Rosa. Por esse motivo, o carneiro representa a dualidade da entrega do amor: dá prazer, mas também pode ser uma porta para o sofrimento.\n"
         "\n"
         "Elefante dentro da Jiboia\n"
         "Este é um desenho feito pelo Piloto e que é revelado ao Pequeno Príncipe.\n"
         "\n"
         "Inicialmente os adultos não entendiam o desenho e o confundiam com um chapéu, porque a jiboia que comeu o elefante assumiu a sua forma. Para explicar o desenho, o Piloto fez uma segunda versão, um raio X que revela o elefante dentro da jiboia.\n"
         "\n"
         "Esta ilustração pretende demonstrar que nem sempre aquilo que vemos é a realidade. Assim como o primeiro desenho parecia para muitos um chapéu, na vida muitas coisas não são o que parecem à primeira vista.\n"
         "\n"
         "A Serpente\n"
         "Este é o primeiro personagem que o Pequeno Príncipe encontra na Terra.\n"
         "\n"
         "É possível fazer um paralelismo com a serpente do livro e a serpente da Bíblia, que convenceu Adão e Eva a comer o fruto proibido, o que resultou na expulsão do Éden. A cobra de Saint-Exupéry é responsável por enviar o Pequeno Príncipe à sua casa através da sua mordida venenosa.\n"
         "\n"
         "Ela representa o fenômeno da morte e, apesar de falar por enigmas, não requer tanta interpretação como outros personagens porque fala com franqueza.\n"
         "\n"
         "O Rei\n"
         "O Pequeno Príncipe encontra o Rei no primeiro planeta que visita. Apesar de pensar que ele governa todo o Universo, o seu poder é vazio porque ele só pode dar ordens as coisas que aconteceriam mesmo sem que ele mandasse. Ele faz tudo para que o Pequeno Príncipe fique com ele, mas, como não consegue, o nomeia seu embaixador quando ele vai embora.\n"
         "\n"
         "O rei é mandão, mas tem um bom coração e ensina a lição que “é preciso exigir de cada um o que cada um pode dar”.\n"
         "\n"
         "O Bêbado\n"
         "Elemento envolvido em tristeza que afirma que bebe para esquecer a vergonha de beber.\n"
         "\n"
         "O Pequeno Príncipe fica com pena dele, mas ao mesmo tempo fica intrigado com a sua atitude perante a vida.\n"
         "\n"
         "O bêbado representa a ignorância e as pessoas que tentam fugir da realidade ou resolver um determinado problema através de um vício.\n"
         "\n"
         "O Homem de Negócios\n"
         "Completamente envolvido nos seus cálculos, o Homem de Negócios quase não nota a presença do Pequeno Príncipe. Este personagem se apropria das estrelas, afirmando ser mais rico desse jeito.\n"
         "\n"
         "O Pequeno Príncipe entende que a sua lógica é parecida com a do Bêbado e afirma que não vale a pena ser dono de alguma coisa se não se cuida delas.\n"
         "\n"
         "O homem de negócios tem a função de caricatura dos adultos, que muitas vezes estão tão envolvidos nos seus negócios que não conseguem aproveitar a vida. É o único personagem criticado abertamente pelo Pequeno Príncipe.\n"
         "\n"
         "O Acendedor de Lampiões\n"
         "Inicialmente o Pequeno Príncipe pensa que é apenas mais uma pessoa com comportamento ridículo e sem propósito. No entanto, ao verificar a devoção e empenho no seu trabalho, chega a admirá-lo.\n"
         "\n"
         "O homem tem a tarefa de acender o lampião de noite e apagá-lo de dia, mas o planeta gira muito rápido e o Sol se põe a cada minuto, o que faz com que o seu trabalho seja extenuante.\n"
         "\n"
         "O Acendedor de Lampiões simboliza as pessoas que cumprem determinadas tarefas sem pensamento crítico, muitas vezes fazendo coisas sem sentido ou sem entender porquê.\n"
         "\n"
         "O Geógrafo\n"
         "Um homem com bastante conhecimento geográfico e que escreve vários livros. Não obstante a sua inteligência sobre outros lugares, não conhece nada sobre o seu próprio planeta, afirmando que não é a sua função explorá-lo. É ele que recomenda ao Pequeno Príncipe uma visita ao planeta Terra.\n"
         "\n"
         "Quando o Geógrafo revela que não estuda as flores porque elas não duram para sempre, o Pequeno Príncipe fica preocupado e se arrepende de tê-la deixado.\n"
         "\n"
         "O Astrônomo\n"
         "O astrônomo turco foi o primeiro humano a descobrir o asteroide B-612, a casa do Pequeno Príncipe. Quando este personagem fez esta descoberta, ninguém acreditou porque ele vestia roupas típicas turcas. No entanto, foi ouvido quando, anos mais tarde, fez a apresentação com roupas ocidentais.\n"
         "\n"
         "O astrônomo turco representa o problema da xenofobia e racismo na sociedade, onde pessoas são julgadas de acordo com a sua roupa, raça ou local de nascimento.\n"
         "\n"
         "O Vaidoso\n"
         "É o único habitante no seu planeta e tem uma enorme necessidade de ser reconhecido e elogiado pelos outros.\n"
         "\n"
         "Ele pergunta se o Pequeno Príncipe o admira e pede para que ele diga que é o mais inteligente, o mais bonito e o mais rico do planeta, o que é estranho para o protagonista, já que o vaidoso é a única pessoa existente por ali.\n"
         "\n"
         "Este personagem ensina que nós não podemos depender dos elogios dos outros para encontrarmos o nosso valor.
"""

# Nome do arquivo PDF
nome_arquivo_pdf = "resumo_do_livro_o_pequeno_principe.pdf"

# Criar o PDF
criar_pdf(nome_arquivo_pdf, texto_para_pdf)

# Enviar o email com o PDF anexado
email_destino = 'juliocddossantos@outlook.com'
assunto_email = 'Resumo do Livro O Pequeno Príncipe'
corpo_email = 'Por favor, encontre em anexo o resumo do livro O Pequeno Príncipe.'
enviar_email(email_destino, assunto_email, corpo_email, nome_arquivo_pdf)

print(f'O email com o PDF foi enviado com sucesso para {email_destino}.')

