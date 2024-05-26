# Titulo: Chatm
# Botão de iniciar Chat
    # popup (janela da frente da tela)
    # Titulo: Bem vindo ao Chatm
    # campo de texto -> Escreva seu nome no Chat
    # Botão: Entrar no Chat
        # Sumir com o titulo Chatm
        # Fechar a janela (popup)
        # Carregar chat
            # As mensagens que ja foram enviadas (chat)
            # Campo: Digite sua mensagem
            # Botão de enviar

# FERRAMENTAS USADAS
# Ferramenta para criar site (flet)

# importar o flet

import flet as ft

# Criar a função principal do seu aplicativo
def main(pagina):
    # Criar todas as funcionalidades

    # tarefas
    # 1º Criar o elemento
    titulo = ft.Text("Chatm")
    titulo_janela = ft.Text("Bem vindo ao Chat")
    
    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        chat.controls.append(mensagem)
        pagina.update()
    
    pagina.pubsub.subscribe(enviar_mensagem_tunel)    

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value
        nome_usuario = campo_nome_usuario.value
        mensagem = ft.Text(f"{nome_usuario}: {texto_mensagem}")
        pagina.pubsub.send_all(mensagem)
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem)
        mensagem = ft.Text(f"{campo_nome_usuario.value} entrou no Chat")
        pagina.pubsub.send_all(mensagem)
        pagina.update()

    campo_nome_usuario = ft.TextField(label="Escreva seu nome no Chat", on_submit=entrar_chat)
    botao_entrar = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    janela = ft.AlertDialog(
        title=titulo_janela, 
        content=campo_nome_usuario, 
        actions=[botao_entrar])

    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar Chat", on_click=iniciar_chat)

    # 2º Adicionar os elementos na página
    pagina.add(titulo)
    pagina.add(botao_iniciar)

# Por o aplicativo pra rodar
ft.app(main, view=ft.WEB_BROWSER)