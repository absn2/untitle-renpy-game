# A janta SCRIPT

define b = Character(_("Bruna"), color="#c8ffc8")
define e = Character(_("Eu"), color="#F5FFFA")
define g = Character(_("Garçonete"), color="#A020F0")
image brunaSorrindo = im.Scale("bruna smile.png", 510, 700)
image brunaZangada = im.Scale("bruna zangada.png", 510, 700)
image brunaFinal = im.Scale("bruna final.png", 510, 700)
image garçoneteSorrindo = im.Scale("garçonetesorrindo.png", 400, 700)
image garçoneteMotel = im.Scale("garçoneteMotel.png", 500, 700)
default choiceExecute = False
default perderBruna = False


# The game starts here.

label start:
    
    play music "musica ambiente restaurante.mp3"
    scene black
    
    "Me lembro como se fosse ontem de um certo encontro que eu tive na aurora da minha juventude…"
    "Nos dias mais chuvosos onde o coração de um homem se sente fragilizado, fui a procura de alguém que me completasse em sites de relacionamentos online"
    "Dei \"match\" com uma garota interessante, dando uma olhada mais a fundo no perfil, descobri que ela era engenheira civil."
    "Talvez eu estivesse um tanto quanto nervoso ou ansioso, e com um pouco de irresponsabilidade, dormi demais e perdi o horário do nosso JANTAR."
    
    scene bg restaurant
    with fade

    show brunaSorrindo

    b "Nossa... você demorou muito tempo para chegar até aqui."

    b "Até pensei que você não iria vir..."
    
    b "Mas enfim, por que demorasse tanto?"
    
    menu:
        "Mentir":
            $ choiceExecute = True
        "Falar a verdade":
            $ choiceExecute = False
    if choiceExecute:
        e "Meu cachorro comeu as chave do carro, tive que esperar de 6 a 8 horas..e..err... e morreram 2 crianças."
        b "Âhn duas crianças? como isso aconteceu?"
        e "Digo.. nasceram duas crianças na rua ao lado"
        b "Só odeio uma coisa nas pessoas, falta de honestidade! Imprevistos acontecem, por favor me conte a verdade, não mordo!"
        e "Tudo bem, estava muito ansioso e não consegui dormir direito, não é todo dia que tenho a oportunidade de ter um encontro com alguém tão incrível quanto você."
    else:
        e "Estava muito ansioso e não consegui dormir direito, não é todo dia que tenho a oportunidade de ter um encontro com alguém tão incrível quanto você."

label inicioEncontro:
    b "Por um acaso você andou me \"stalkeando\"?"
    e "Hahahaha confesso que sim, você não deu nem uma olhadinha no meu perfil??"
    b "Vi sua foto e achei bonitinho, li a \“bio\” e só, gosto de conhecer as pessoas conversando com elas..."
    e "Entendo, mas como você pode ter certeza que elas não são más pessoas?"
    b "Como você pode ter certeza que EU não sou? as pessoas costumam mentir nos seus perfis..."
    "*Não entendi o que ela quis dizer.*"
    
    if choiceExecute:
        b "Só odeio uma coisa nas pessoas, falta de honestidade! Eu jamais mentiria para conseguir um encontro, você mentiu em algo?"
        e "Eu nunca mentiria no meu perfil..."
    else:
        b "Já esqueceu bobinho? odeio desonestidade, jamais mentiria para conseguir um encontro, você mentiu em algo?"
        e "Eu nunca mentiria no meu perfil..."

    hide brunaSorrindo
    
    scene black
    with fade
    
    "A conversa estava indo muito bem, nos sentamos parecíamos estar em sintonia, até que.."
    
    scene bg restaurant
    show brunaSorrindo at left
    show garçoneteSorrindo at right

    g "Posso anotar o pedido de vocês?"
    b "Qual o especial do dia?"
    "*Eu estava fissurado na garçonete*"
    g "O chefe fez um linguine, um tipo especial de massa italiana que está dando o que falar"
    b "Vou querer esse então, e você já decidiu qual?"

    menu:
        "Continuar olhando pra garçonete e fazer o pedido flertando com ela":
            jump flerteGarçonete
        "Esquecer a garçonete e pedir o mesmo que bruna":
            jump notFlerteGarçonete

label flerteGarçonete:
    e "Boa noite, moça gostos-… digo garçonete"
    g "hihihi boa noite também Mister."
    e "Vou querer esse filé à parmegiana, com essa porção de fritas por favor"
    g "Okay, Mister vou aqui e já trago"

    hide garçoneteSorrindo
    hide brunaSorrindo
    show brunaZangada
    b "Você pode me dizer o que foi isso!!?"
    
    menu:
        "Explicar que sentiu atração nela":
            $ perderBruna = False
        "Dar desculpa esfarrapada para não estragar noite":
            $ perderBruna = True
    
    if perderBruna:
        e "Tem um mapa?"
        b "nao entendi"
        e "Me perdi no brilho dos teus olhos e acabei me distraindo haha"
        b "Você é literalmente o pior tipo de homem que existe, desonesto, galinha e ainda por cima quando disse \“bonitinho\" queria dizer feio quero que você se foda seu merda"    
    
    e "Tipo, sem querer ofender né, mas ela me chamou muito mais atenção, acho que sou o pior tipo de homem, aquele que só vê pelas aparências desculpas, não queria estragar sua noite"
    b "Gostei muito da sua atitude de cavalheiro, vou embora, espero que vocês se fodam muito de noite, adeus."
    
    hide brunaZangada
    show garçoneteSorrindo
    
    g "ela foi embora.. que pena, aqui está seu pedido."
    e "Calma, não chegou todo meu pedido ainda"
    g "Como assim?"
    
    menu:
        "Faltou você que era a melhor parte do prato.":
            jump encontroGarçonete
        "Nada não, pensei muito alto":
            jump finalRuim1de5

label encontroGarçonete:
    hide garçoneteSorrindo
    scene black
    with fade
    play music "romanticSong.mp3"       
    g "eu largo daqui a trinta minutos"
    e "vou fazendo a reserva no motel.."
    e "okay, te espero na saida"
    "Então, terminei meu prato de parmegiana e esperei ela nos fundos do restaurante"
    "Levei ela pro melhor motel da cidade…"
    "Eros"
    scene bg motel
    with fade
    show garçoneteMotel
    g "Nossa que local maravilhoso"
    
    menu:
        "Peço para ela tirar a roupa":
            jump finalNeutro2de5
        "Digo para ela que vou no banheiro primeiro":
            jump finalRuim3de5


label finalRuim1de5:
    scene black
    with fade
    
    play music "end_song.mp3"
    
    "E assim que terminou a noite, depois de saborear meu prato de filé à parmegiana, fui para minha casa, liguei no netflix e fiquei assistindo rick and morty…."
    "sozinho… sozinho para sempre"
    e "Alexa, toca a música mais triste de todos os tempos"
    "tem certeza mestre?"
    
    play music "sad_song.mp3"
    
    "sim"
    "....."
    "{b}BAD ENDING{\b}"

    jump end

label finalNeutro2de5:

    hide garçoneteMotel
    scene bg beijo
    with fade

    "Ela começa a tirar toda sua roupa, muito bonita e deliciosa, eu como um cavalheiro ajudo-lá e desfrutamos muito do melhor jeito brasileiro."

    scene bg beijo 2

    "Transamos a noite inteira, nossa e como era bom."
    "Sua pele macia e esplendorosa como um arco íris e seu amor pelo meu pinto."
    g "Nossa essa noite foi de fuder"
    e "Isso mesmo, gostei muito de você."
    scene bg final    

    g "Tome aqui meu numero"

    play music "end_song.mp3"
    scene black
    with fade
    
    "Depois desse dia eu pensei que ia ter finalmente um amor verdadeiro, porém fui ela me deu o numero errado e nunca mais a vi na minha vida."
    "Destruiu toda minha confiança, e meu ser."
    "Até hoje sonho com essa transa."
    "{b}NEUTRAL ENDING{\b}"

    jump end
    
label finalRuim3de5:
    
    play music "end_song.mp3"
    scene black
    with fade
    
    "Quando sai do banho, e voltei para meu quarto, ela tinha roubado todos meus pertences, estava um pobre um zero à esquerda, ela tinha pego todo meu esforço de anos e jogado no lixo"
    "Também fui um otário desperdicei o amor da minha vida, se eu pudesse voltar atrás…"
    "{b}BAD ENDING{\b}"

    jump end


label notFlerteGarçonete:
    e "Ahn? éhhh… vou querer o mesmo que a dama"

    hide garçoneteSorrindo
    hide brunaSorrindo
    scene black
    with fade

    "Devoramos o jantar parecíamos leões devorando gazelas"

    scene bg restaurant
    show brunaSorrindo

    b "A garçonete tinha razão esse jantar estava divino. o que vamos comer de sobremesa?"
    e "Que tal pularmos a sobremesa e irmos lá pra casa?"
    b "Hmm parece uma boa ideia.."
    "Paguei a conta dei uma gorjeta generosa para aquela gostosa da garçonete"
    
    hide brunaSorrindo
    scene bg casa
    show brunaSorrindo

    play music "romanticSong.mp3"
    
    b "bom aqui estamos o que você quer fazer?"
    
    menu:
        "Por que enrolar tanto se podemos pular para parte que fazemos amor?":
            jump finalRuim4de5
        "Poderíamos jogar fifa e quem tomasse um gol tirava duas partes da roupa e quem fizesse apenas uma o que acha?":
            jump finalBom5de5
label finalRuim4de5:
    
    b "Claro, mas primeiro onde fica o banheiro?"
    e "Fica no final do corredor, estarei esperando aqui no sofá"
    b "Tenho uma surpresinha pra você rs já volto"
    
    scene black
    with fade
    play music "end_song.mp3"
    
    "......"
    "Acordei deitado no chão da sala, ela roubou meu ps4"
    "{b}BAD ENDING{\b}"
    
    jump end

label finalBom5de5:
    
    play music "end_song.mp3"
    
    e "você sabe jogar não é?"
    b "claro que sei!!"
    
    e "ok acredito em você"
    
    hide brunaSorrindo
    scene black
    with fade
    
    "***Jogamos apenas uma partida, quer dizer tentamos.. o jogo estava 3x3 e estávamos ambos seminus***"

    scene bg casa
    with fade
    show brunaFinal

    e "nossa o seu corpo é simplesmente maravilhoso"
    b "olha só o seu, que delicia, e esse…"

    scene endingbom

    "fizemos amor a noite inteira, estava apaixonado, afinal de contas o que mais poderia querer, uma mulher bonita, inteligente e engenheira, umas das profissões mais complexas"
    e "deveríamos fazer isso novamente"
    b "qual parte? rs"

    scene closetoend

    e "todas, adorei passar esse tempo com você, quero te conhecer por inteiro."
    b "snif snif essa é a coisa mais linda que já ouvi na minha vida eu também quero te conhecer por inteiro"

    scene black
    with fade

    "E foi assim crianças que eu conheci sua mãe!!!"
    "{b}GOOD ENDING{\b}"

label end:
    return







 
