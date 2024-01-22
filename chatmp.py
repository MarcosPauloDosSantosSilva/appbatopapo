import flet as  flet

def main (pagina):

    titulo = flet.Text ("Chatpapo-mp")
    pagina.add(titulo)

    nome_usuario = flet.TextField(label="Escreva seu Nome")

    

    def enviar_msg_tunel(informaçoes):
        chat_conversa.controls.append(flet.Text(informaçoes))

        pagina.update()

    pagina.pubsub.subscribe(enviar_msg_tunel)

    chat_conversa = flet.Column()
    

    def enviar_mesagem(evento):
        # colocar o nome do usuario na msg
        texto_conversa = f"{nome_usuario.value}: {campo_mesagem.value}"
        

        pagina.pubsub.send_all(texto_conversa)
       
        #limpar campo msg
        campo_mesagem.value=""

        pagina.update()
    campo_mesagem = flet.TextField(label="Escreva sua mensagem", on_submit=enviar_mesagem)
    botao_enviar_msg = flet.ElevatedButton("Enviar", on_click=enviar_mesagem)
    linha_mensagem = flet.Row([campo_mesagem, botao_enviar_msg])

    def entrar_chat(evento):
        popupchat.open = False

        pagina.remove(botao_iniciar)

        pagina.add(chat_conversa)

        pagina.add(linha_mensagem)
        texto_entrou = f"{nome_usuario.value}: Entrou no chat..."
        pagina.pubsub.send_all(texto_entrou)
              
        pagina.update()
    
    popupchat = flet.AlertDialog(open=False,
                                  modal=True, 
                                  title=flet.Text("Seja bem Vindo"),
                                  content=nome_usuario,
                                  actions=[flet.ElevatedButton("Entrar", on_click=entrar_chat)]

                                  )

    def iniciar_chat(evento):
        pagina.dialog = popupchat
        popupchat.open = True
        pagina.update()

    botao_iniciar = flet.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
    pagina.add(botao_iniciar)



flet.app(main, view=flet.WEB_BROWSER)